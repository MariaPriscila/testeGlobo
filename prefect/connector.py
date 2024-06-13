import sys
from prefect_sqlalchemy import SqlAlchemyConnector, ConnectionComponents, SyncDriver
from dotenv import load_dotenv
import os

env = os.getenv("PREFECT_ENV_FILE", sys.path[0]+"/.env")
load_dotenv(env)

connector = SqlAlchemyConnector(
    connection_info=ConnectionComponents(
        driver=SyncDriver.POSTGRESQL_PSYCOPG2,
        username=os.getenv("USERNAME"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE"),
        host=os.getenv("HOST"),
        port=5432
    )
)
connector.save(os.getenv("PREFECT_BLOCK_NAME"), overwrite=True)