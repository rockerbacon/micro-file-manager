"""HTTP application for the program's REST API.

The module utilizes FastAPI.
Use uvicorn to start the server:
    uvicorn.run("api.server:app")
"""

from fastapi import FastAPI
from .routers import files, health


app = FastAPI()

app.include_router(files.router)
app.include_router(health.router)
