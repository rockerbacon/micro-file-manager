"""MinIO client configuration."""


from env import env
from minio import Minio


def _get_uri() -> str:
    return f"{env.MINIO_HOST}:{env.MINIO_PORT}"


def _get_access_key() -> str:
    return env.MINIO_USER


def _get_secret_key() -> str:
    return env.MINIO_PASSWORD


def _get_is_secure() -> bool:
    return env.MINIO_USE_TLS


minio_client = Minio(
    _get_uri(),
    access_key=_get_access_key(),
    secret_key=_get_secret_key(),
    secure=_get_is_secure(),
)
