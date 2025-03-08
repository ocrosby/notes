import marimo

__generated_with = "0.11.14"
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


@app.cell
def _(mo):
    mo.md(
        r"""
        # Schemas

        A client connection to the server can only access data in a single database, the one specified in the connection request.

        A database contains one or more named `schemas`, which in turn contain tables. Schemas also contain other kinds of named objects including:

        - data types
        - functions
        - operators

        Within one schema, two objects of the same type cannot have the same name. Furthermore, tables, squences, indcexes, views, materialized views, and foreign tables share the same namespace, so that, for example an index and a table must have different names if they are in the same schema. The same object can be used in different schemas without conflict; for example, both sschema1 and myschema can contain tables named mytable. Unlike databases, schemas are not rigidly separated: a user can access objects in any of the schemas in the database they are connected to, if they have privileges to do so,

        There are several reasons why one my want to use schemas🥇

        - To allow many users to use one database without interfering with each other.
        - To organize database objects into logical groups to make them more manageable.
        - Third-party applications can ber put into separate schemas so they do not collide with the names of other objects.

        Schemas are analogous to directories at the operating system level, except that schemas cannot be nested.

        ## Creating a Schema

        ```sql
        CREATE SCHEMA myschema;
        ```

        To create or access object in a schema, write a qualified name consisting opf the schema name separated by a dot:

        ```sql
        schema.table
        ```

        To create a table in the new schema:

        ```sql
        CREATE TABLE myschema.mytable (
            ...
        );
        ```

        To drop a schema if it's empty (all objects in it have to be dropped), use:

        ```sql
        DROP SCHEMA myschema;
        ```

        To drop a schema including all contained objects, use:

        ```sql
        DROP SCHEMA myschema CASCADE;
        ```

        If you want to create a schema owned by someone else:

        ```sql
        CREATE SCHEMA schema_name AUTHORIZED user_name;
        ```

        To show the current search path:

        ```sql
        SHOW search_path;
        ```

        ---

        Default Output:

        ```plaintext
         search_path
        --------------
         "$user", public
        ```

        The first element specifies that a schema with the same name as the current user is to be searched. If no such schema exists, the entry is ignored. The second element refers to the public schema.

        The first schema in the search path that exists is the default location for creating new objects.

        To put our new schema in the path, we use:

        ```sql
        SET search_path TO myschema,public;
        ```

        Since myschema is fht efirst element in the path, new objects would by default be created in it.

        We could have also written:

        ```sql
        SET search_path TO myschema;
        ```

        Then we no longer have access to the public schema without explicit qualification.  There is nothing special about the public schema excep that it exists by default. It can be dropped, too.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        # Schemas and Priviledges

        By default, users cannot access any objects in schemas they do not own. To allow that, the owner of the schema must grant the USAGE privilege on the schema. By default, everyone has that privilege on the schema `public`. To allow users to make use of the objects in a schema, additional privileges might need to be grated as appropriate for the object.

        A user can also be allowed to create objects in someone else's schema. To allow that, the `CREATE` privilege on the schema needs to be granted. In databases upgraded from PostgreSQL 14 or earlier, everyone has that privilege on schema `public`. Some usage patterns call for revoking that privilege:

        ```sql
        REVOKE CREATE ON SCHEMA public FROM PUBLIC;
        ```

        The first "public" is the schema, the second "public" means "every user".
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # The System Catelog Schema

        In addition to `public` and user-created schemas, each database contains a `pg_catelog` schema, which contains the system tables and all the built-in data types, functions, operators. `pg_catelog` is always effectively part of the search path. If it is not named explicitly in th epath then it is implicitly searched before search path's schemas. This ensures that built-in names will always be findable. However, you can explicitly palce `pg_catalog` at the end of your search path if you prefer to have user-defined names override built-in names.

        Since system table names begin with pg_, it is best to avoid such names to ensure that you won't suffer a conflict if some future version defines a system table anmed the same as your table.
        """
    )
    return


@app.cell
def _(mo):
    mo.md("""# Usage Patterns""")
    return


@app.cell
def _(mo):
    mo.callout(r"""
    Schemas can be used to organize your data in many ways. A secure schema usaage pattern prevents untrusted users from changing the behavior of other users' queriies. When a database does not use a secure schema usage pattern, users wishing to securely query that database would take protective action at the beginning of each session. Specifically, they would begin each session by setting search_path to the empty string or otherwise removing schemas that are writable by non-superusers from the search_path. There are a few usage patterns easily supported by the default configuration
    """, kind="info")
    return


@app.cell
def _(mo):
    mo.accordion(
        {
            "Constrain ordinary users to user-private schemas": mo.md("""
    To implement this pattern, first ensure that no schemas have public CREATE privileges. Then, for every user needing to create non-temporary objects, create a schema with the same name as that user, for example CREATE SCHEMA alice AUTHORIZATION alice. (Recall that the default search path starts with $user, which resolves to the user name. Therefore, if each user has a separate schema, they access their own schemas by default.) This pattern is a secure schema usage pattern unless an untrusted user is the database owner or has been granted ADMIN OPTION on a relevant role, in which case no secure schema usage pattern exists.

    In PostgreSQL 15 and later, the default configuration supports this usage pattern. In prior versions, or when using a database that has been upgraded from a prior version, you will need to remove the public CREATE privilege from the public schema (issue REVOKE CREATE ON SCHEMA public FROM PUBLIC). Then consider auditing the public schema for objects named like objects in schema pg_catalog.
        """),
            "Remove the public schema from the default search path": mo.md("""
    By modifying postgresql.conf or by issuing ALTER ROLE ALL SET search_path = "$user". Then, grant privileges to create in the public schema. Only qualified names will choose public schema objects. While qualified table references are fine, calls to functions in the public schema will be unsafe or unreliable. If you create functions or extensions in the public schema, use the first pattern instead. Otherwise, like the first pattern, this is secure unless an untrusted user is the database owner or has been granted ADMIN OPTION on a relevant role.        
            """),
            "Keep the default search path, and grant privileges to create in the public schema": mo.md("""
    All users access the public schema implicitly. This simulates the situation where schemas are not available at all, giving a smooth transition from the non-schema-aware world. However, this is never a secure pattern. It is acceptable only when the database has a single user or a few mutually-trusting users. In databases upgraded from PostgreSQL 14 or earlier, this is the default.        
            """),
        }
    )

    return


@app.cell
def _(mo):
    mo.md(r"""
    For any pattern, to install shared applications (tables to be used by everyone, additional functions provided by third parties, etc.), put them into separate schemas. Remember to grant appropriate privileges to allow the other users to access them. Users can then refer to these additional objects by qualifying the names with a schema name, or they can put the additional schemas into their search path, as they choose.
    """)
    return


if __name__ == "__main__":
    app.run()
