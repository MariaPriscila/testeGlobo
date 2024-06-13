from http import HTTPStatus
import os
import sys
import uuid
from dotenv import load_dotenv
import httpx
from prefect import flow, task
from prefect_sqlalchemy import SqlAlchemyConnector

env = os.getenv("PREFECT_ENV_FILE", sys.path[0]+"/.env")
load_dotenv(env)
PREFECT_BLOCK_NAME=os.getenv("PREFECT_BLOCK_NAME")
requests_count=0

httpx_mock_client = httpx.Client(
    transport=httpx.MockTransport(
        lambda request: httpx.Response(
            HTTPStatus.REQUEST_TIMEOUT, content="Time out"
        )
    )
)
        
def get_httpx_client():
    global requests_count
    if requests_count == 0:
        requests_count+=1
        return httpx_mock_client
    
    requests_count+=1
    return httpx

@task(retries=2, retry_delay_seconds=5)
def get_wizards():
    url = f"https://wizard-world-api.herokuapp.com/Wizards"
    api_response = get_httpx_client().get(url)
    api_response.raise_for_status()
    wizards = api_response.json()
    for wizard in wizards:
        with SqlAlchemyConnector.load(PREFECT_BLOCK_NAME) as connector:
            connector.execute(
                "INSERT INTO wizard (id, first_name, last_name) VALUES (:id, :firstName, :lastName) ON CONFLICT DO NOTHING;",
                parameters=wizard,
            )

    return wizards

@task(
    name="Fetch elixir",
    task_run_name="Fetching-elixir-{wizard_elixir}",
    retries=2, retry_delay_seconds=5)
def get_elixir(wizard_elixir: dict):
    url = f"https://wizard-world-api.herokuapp.com/Elixirs/{wizard_elixir['id']}"
    api_response = httpx.get(url)
    api_response.raise_for_status()
    elixir_json = api_response.json()
    dto = elixir_json.copy()

    dto['ingredients'] = [uuid.UUID(ingredient['id']) for ingredient in dto['ingredients']]
    dto['inventors'] = [uuid.UUID(inventor['id']) for inventor in dto['inventors']]
    with SqlAlchemyConnector.load(PREFECT_BLOCK_NAME) as connector:
        connector.execute(
            """INSERT INTO elixir (id, name, effect, side_effects,characteristics, time,
                difficulty, ingredients, inventors, manufacturer) 
                VALUES (:id, :name, :effect, :sideEffects, :characteristics, :time,
                :difficulty, :ingredients, :inventors, :manufacturer)
                ON CONFLICT DO NOTHING;""",
            parameters=dto,
        )

    return elixir_json

@task(
    name="Fetch ingredient",
    task_run_name="Fetching-ingredient-{elixir_ingredient}",
    retries=2, retry_delay_seconds=5)
def get_ingredient(elixir_ingredient: dict):
    url = f"https://wizard-world-api.herokuapp.com/Ingredients/{elixir_ingredient['id']}"
    api_response = httpx.get(url)
    api_response.raise_for_status()
    ingredient_json = api_response.json()
    with SqlAlchemyConnector.load(PREFECT_BLOCK_NAME) as connector:
        connector.execute(
            "INSERT INTO ingredient (id, name) VALUES (:id, :name) ON CONFLICT DO NOTHING;",
            parameters=ingredient_json,
        )

    return ingredient_json

@flow(log_prints=True)
def fetch_wizard_api():
    wizards = get_wizards()
    for wizard in wizards:
        for wizard_elixir in wizard["elixirs"]:
            elixir = get_elixir(wizard_elixir)
            for elixir_ingredient in elixir["ingredients"]:
                get_ingredient(elixir_ingredient)

if __name__ == "__main__":
    fetch_wizard_api()