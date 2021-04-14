# Meditations & Perceptions
A web logging application built with python.

## How to run locally
1. Clone this repository.
2. Ensure `docker` and `docker-compose` are installed on your machine.
3. In the base directory, run the `start_container.sh` script:
 - `./start_containers.sh`
4. Navigate to any URL defined in the API layer (OpenAPI docs to come soon!). For example:
 - `localhost:5000/home`

## To Do:
 - Add `SQLALCHEMY_DATABASE_URI` environment variable populated with secrets.
 - Incorporate `Flask-Migrate` for database migrations.
 - Take a look at Miguel Grinber's Flask Mega Tutorial to see how he deals with FlaskSQLAlchemy and Flask's Application Factory Function.
