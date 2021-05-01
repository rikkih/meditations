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

## To Do:
 - Design compartments with Blueprints, such as a directory for `Users` and `Posts` with models, views.
 - Look at `networks` for `docker-compose` and easily allowing inter-container communications without environment variabling the container name.
 - Authorisation and logging in.
 - Flask Forms for Requests.
 - Use GitHub Issues for this bloody To Do section in the Readme.MD!!!
 - Add a CI pipeline with a testing suite for integration tests in a testing orchestrain suite.
 - Add a quick test command for unit tests.
 - Add flask db commands for local and docker compose environments with their respective dbs.
 - Argue whether connexion is a good tool to use for full stack development or whether this is better for backend API's.
