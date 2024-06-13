import sys
from yoyo import read_migrations, get_backend
from dotenv import load_dotenv
import os

env = os.getenv("MIGRATOR_ENV_FILE", sys.path[0]+"/.env")
load_dotenv(env)

# Get database connection parameters from environment variables
DATABASE_URL = os.getenv('DATABASE_URL')

def main():
    # Initialize the backend using the specified database URL
    backend = get_backend(DATABASE_URL)

    # Read migration scripts from the migrations directory
    migrations = read_migrations('migrations')

    # Apply migrations
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))

if __name__ == '__main__':
    main()
