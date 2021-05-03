# Meditations & Perceptions
A web logging application built with python.

## How to run locally
1. Clone this repository.
2. Set the development environment variables:
 - `source dev.env`
2. Ensure `docker` and `docker-compose` are installed on your machine.
3. In the base directory, run the `start_container.sh` script (It's very simple. Feel free to inspect that and also the subsequent `meditations/start.sh` script for the meditations container):
 - `./start_containers.sh`
4. Navigate to any URL defined in the API layer (OpenAPI docs to come soon!). For example:
 - `localhost:5000/home`

