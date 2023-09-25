# Micro File Manager
A simple file manager server utilizing FastAPI, MinIO and PostgreSQL, with file scanning capabilities provided by ClamAV.

### Requirements
- Docker
- Pyenv
- Pyenv-virtualenv
- libpq development files

IMPORTANT: all instructions and utilities provided in this repository assume a complete pyenv setup, including all the pyenv recommended configurations.

## Usage
The software is subdivided in two microservices:
- The manager itself, responsible for handling API requests and managing the files' data and metadata. Its source code is available in the [manager](/manager) folder.
- A file scanning extension, responsible for scanning files in search of possible security threats. This microservice is still a work-in-progress and its source code is not yet available.

Instructions on the usage of each microservice are provided in their respective README.md files: [manager/README.md](/manager/README.md), (no README for the scanner is available yet).

Docker compose files are also provided for easier deployment of the software and external dependencies. These are available in the [docker-compose](/docker-compose) folder, and each file contains brief comments on their general purpose.

