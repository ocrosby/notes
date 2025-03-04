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


if __name__ == "__main__":
    app.run()
