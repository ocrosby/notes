import marimo

__generated_with = "0.11.17"
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

        def connect_by_db_name(db_name: str) -> Optional[psycopg2.extensions.connection]:
            db_config = get_db_config(override_db=db_name)
            return connect(db_config=db_config)

        if __name__ == "__main__":
            connect()
        ```
        """
    )
    return


@app.cell
def _():
    from marimo_nb.connect import connect, connect_by_db_name, get_db_config
    return connect, connect_by_db_name, get_db_config


@app.cell
def _(mo):
    mo.md(r"""# Listing all of the databases""")
    return


@app.cell
def _(connect_by_db_name):
    def databases(conn):
        try:
            cur = conn.cursor()
            cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false")
            databases = cur.fetchall()
            for db in databases:
                yield db
            cur.close()
        except Exception as e:
            print(f"Error: {e}")

    for database in databases(connect_by_db_name("postgres")):
        print(database)
    return database, databases


@app.cell
def _(mo):
    database_name = mo.ui.text(placeholder="enter a db name here", label="Database Name", value="postgres")

    database_name
    return (database_name,)


@app.cell
def _():
    import psycopg2
    from psycopg2 import sql

    def database_exists(conn, db_name):
        try:
            cur = conn.cursor()
            cur.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [db_name])
            exists = cur.fetchone() is not None
            cur.close()
            return exists
        except Exception as e:
            print(f"Error: {e}")
            return False
    return database_exists, psycopg2, sql


@app.cell
def _(mo):
    mo.md(f"""
    ## Determine if a database exists by name
    """)
    return


@app.cell
def _(connect_by_db_name, database_exists, database_name):
    if database_exists(connect_by_db_name("postgres"), database_name.value):
        print(f"Database '{database_name.value}' exists.")
    else:
        print(f"Database '{database_name.value}' does not exist.")
    return


@app.cell
def _(mo):
    mo.md(r"""## List tables in the database""")
    return


@app.cell
def _():
    def list_tables_in_database(conn):
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            tables = cur.fetchall()
            for table in tables:
                print(table[0])
            cur.close()
        except Exception as e:
            print(f"Error: {e}")
    return (list_tables_in_database,)


@app.cell
def _(connect_by_db_name, database_name, list_tables_in_database):
    list_tables_in_database(connect_by_db_name(database_name.value))
    return


if __name__ == "__main__":
    app.run()
