# Meditations & Perceptions
A web logging application built with python.

# The logical structure of this application
```
.
├── instance
├── meditations
│   ├── auth
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── views.py
│   ├── posts
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── views.py
│   ├── scripts
│   │   ├── entrypoint.sh
│   │   └── start.sh
│   ├── templates
│   │   ├── base.html
│   │   ├── edit.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── new_post.html
│   │   └── posts.html
│   ├── app.py
│   ├── config.py
│   ├── Dockerfile
│   ├── extensions.py
│   ├── __init__.py
│   ├── meditations.db
│   └── requirements.txt
├── tests
│   ├── conftest.py
│   ├── integration.py
│   └── unit.py
├── dev.env
├── docker-compose.yml
├── README.md
├── secrets.sh
└── start-containers.sh
```

## How to run locally
1. Clone this repository.

2. 
-  This service, when run locally, requires the following environment variables in the current shell context:
```
export FLASK_APP=meditations.app
export FLASK_ENV=development
export SQLALCHEMY_DATABASE_URI="sqlite:///meditations.db"
```
-  If you are going to use the docker compose orchestration, please also set the following environment variables:
```
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=IAmCalledPasswordButMakeMeAPhrase
export POSTGRES_PORT=5432  # You might want to change this if you already have a postgres instance running on this port.
```
-  Optionally, place the above 6 lines of code in a shell script (e.g. `secrets.sh`) and source the file:
```
$ source secrets.sh
```

3.
-  If running outside of the container orchestration, just execute the following command:
```
$ flask run
```

-  In the base directory, run the `start_containers.sh` script (It's very simple. Feel free to inspect that and also the subsequent `meditations/start.sh` script for the meditations container):
```
$ ./start_containers.sh
```

4. Navigate to any URL defined in the API layer (OpenAPI docs to come soon!). For example:
 - `localhost:5000/home`
