import marimo

__generated_with = "0.11.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
        # Installing PostgresSQL

        I installed PostgresSQL using the [Postgresapp.com](https://postgresapp.com/).

        ## Setup your PATH

        Configure your `$PATH` to use the included command line tools:

        ```shell
        sudo mkdir -p /etc/paths.d
        sudo echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
        ```

        I also had to add the path to the tools to my `.zshrc` file.

        ```plaintext
        export PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"
        ```

        and then I had to re-initialize my shell to find psql.

        ```shell
        source ~/.zshrc
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        PostgreSQL server will be running on your Mac with these default settings:

        ```plaintext
        Host: localhost
        Port: 5432
        User: your system user name
        Database: same as user
        Password: none
        Connection URL: postgresql://localhost
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Creating a new database

        First, connect to the PostgresSQL server using the `psql` client tool:

        ```shell
        psql -U postgres
        ```

        Second, create a new database called `suppliers`:

        ```sql
        CREATE DATABASE suppliers;
        ```

        Third, exit the `psql`:

        ```shell
        exit
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # List Databases

        From the psql shell enter the following🥇

        ```shell
        \list
        ```

        or 

        ```shell
        \l
        ```

        or

        ```sql
        SELECT datname FROM pg_database;
        ```

        or

        ```sql
        SELECT datname FROM pg_database WHERE datistemplate = false;
        ```

        This last SQL command filters out the template databases.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""[PostgreSQL Python: Connect to PostgreSQL Database Server](https://neon.tech/postgresql/postgresql-python/connect)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Connecting to the PostgreSQL database from Python

        First, create a .env file to house your database settings

        ```plaintext
        POSTGRES_HOST=localhost
        POSTGRES_DB=suppliers
        POSTGRES_USER=postgres
        POSTGRES_PASSWORD=
        POSTGRES_PORT=5432
        ```

        By using the `.env`, you can change the PostgreSQL connection parameters when moving the code to different 
        environments such as testing or production.

        **Note: This file will need to be added to the .gitignore file to avoid committing sensitive information.**

        Second, create a new file called `constants.py` that will contain the defaults for the various settings

        ```python
        DEFAULT_POSTGRES_USER = "postgres"
        DEFAULT_POSTGRES_PASSWORD = ""
        DEFAULT_POSTGRES_HOST = "localhost"
        DEFAULT_POSTGRES_PORT = 5432
        DEFAULT_POSTGRES_DB = "postgres"    
        ```

        Third, create a new file called `connect.py` that will use the `.env` file to read the database configuration and connect to PostgreSQL:

        ```python    
        from typing import Dict, Any, Optional
        import os
        from dotenv import load_dotenv
        import psycopg2
        from psycopg2 import DatabaseError, OperationalError
        from constants import (
            DEFAULT_POSTGRES_USER,
            DEFAULT_POSTGRES_PASSWORD,
            DEFAULT_POSTGRES_HOST,
            DEFAULT_POSTGRES_PORT,
            DEFAULT_POSTGRES_DB,
        )

        # Load environment variables from the .env file
        load_dotenv()


        def get_db_config() -> Dict[str, Any]:
            port = os.getenv("POSTGRES_PORT")

            db_config = {
                "user": os.getenv("POSTGRES_USER", DEFAULT_POSTGRES_USER),
                "password": os.getenv("POSTGRES_PASSWORD", DEFAULT_POSTGRES_PASSWORD),
                "host": os.getenv("POSTGRES_HOST", DEFAULT_POSTGRES_HOST),
                "port": int(port) if port else DEFAULT_POSTGRES_PORT,
                "database": os.getenv("POSTGRES_DB", DEFAULT_POSTGRES_DB),
            }

            return db_config


        def connect(db_config: Optional[Dict[str, Any]] = None) -> Optional[psycopg2.extensions.connection]:
            if not db_config:
                db_config = get_db_config()

            try:
                # connecting to the PostgreSQL server
                with psycopg2.connect(**db_config) as conn:
                    print("Connected to the PostgreSQL server.")
                    return conn
            except (DatabaseError, OperationalError) as error:
                print(error)
                return None


        if __name__ == "__main__":
            connect()
        ```
        """
    )
    return


@app.cell
def _():
    from marimo.connect import connect
    return (connect,)


if __name__ == "__main__":
    app.run()
