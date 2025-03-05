"""
This module connects to the PostgreSQL database server.
"""

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
    """Get the database configuration from environment variables"""
    port = os.getenv("POSTGRES_PORT")

    db_config = {
        "user": os.getenv("POSTGRES_USER", DEFAULT_POSTGRES_USER),
        "password": os.getenv("POSTGRES_PASSWORD", DEFAULT_POSTGRES_PASSWORD),
        "host": os.getenv("POSTGRES_HOST", DEFAULT_POSTGRES_HOST),
        "port": int(port) if port else DEFAULT_POSTGRES_PORT,
        "database": os.getenv("POSTGRES_DB", DEFAULT_POSTGRES_DB),
    }

    return db_config


def connect(
    db_config: Optional[Dict[str, Any]] = None,
) -> Optional[psycopg2.extensions.connection]:
    """Connect to the PostgreSQL database server"""
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
