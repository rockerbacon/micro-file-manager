"""Health status router module."""

from fastapi import APIRouter, Response, status


router = APIRouter(prefix="/health")


@router.get("")
async def get() -> Response:
    """Confirms server is ready to handle requests.

    Returns:
        No content HTTP response
    """
    return Response(status_code=status.HTTP_204_NO_CONTENT)
