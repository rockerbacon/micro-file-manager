"""Main program for starting the API server."""

import uvicorn


def _main() -> None:
    uvicorn.run("api.server:app")


if __name__ == "__main__":
    _main()
