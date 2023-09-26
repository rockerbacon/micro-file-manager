"""Engine."""


from factories.env import get_env
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


env = get_env()


def get_connection_uri() -> str:
    """Returns a connection URI for PostgreSQL.

    Builds a URI based on environment configurations,
    for use with SQL Alchemy and Alembic.

    Returns:
        URI for connecting with the database.
    """
    return (
        "postgresql://"
        + env.POSTGRESQL_USER
        + ":"
        + env.POSTGRESQL_PASSWORD
        + "@"
        + env.POSTGRESQL_HOST
        + ":"
        + str(env.POSTGRESQL_PORT)
        + "/"
        + env.POSTGRESQL_DB
    )


postgres_engine = create_engine(get_connection_uri())
Session = sessionmaker(postgres_engine)
