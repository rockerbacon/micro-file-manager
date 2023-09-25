# File Manager
This micro service is the core of Micro File Manager and is responsible for:
- Handling user requests
- Managing file contents in MinIO
- Managing file metadata in PostgreSQL

## Running from source
The easiest way to run the file manager from source is to setup a virtual environment containing the source dependencies and executing [main.py](/manager/main.py) within this virtual environment. A [makefile](/manager/Makefile) is provided to simplify the virtual environment setup.

Refer to [docker-compose/local-deps.yaml](/docker-compose/local-deps.yaml) if you also need to run the external dependencies (PostreSQL, MinIO) on a local development environment.
The command `make postgres-upgrade` can be used to run all necessary DDL for the PostgreSQL database.

1. Setup the virtual environment:
```
$ make virtualenv
```

2. Run the manager:
```
$ python main.py
```

## Running with Docker
There are plans to support execution through Docker, but the necessary features have not yet been implemented.

## Navigating the project
This section focuses on briefly describing the software architecture and showing where each component is located in the file tree.

The project loosely follows a [ports and adapters](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) architectural pattern, with the main goal of avoiding coupling between the application and database technologies (PostgreSQL, MinIO).

For those familiar with the aforementioned pattern, a simple summary of the file structure is:
- The `domain` folder is self-explanatory and contains the application domain
- The `database` folder contains adapters for different database technologies
- The `interfaces` folder contains:
    - Ports for domain - database communication
    - Ports for API - domain communication
- The `api` folder contains an adapter for accessing the domain through the HTTP protocol

## Code Standards
This project enforces some code standards and includes automation tools for all of them. Developers can access these through make rules:

- **black auto formatting**: `make format`
- **flake8 style checking**: `make check-flake8`
- **mypy static type checking**: `make check-typing`
- **checking complete standard conformance**: `make check`
