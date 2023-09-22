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
