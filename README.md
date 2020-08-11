# API for the Zappit app

Simple API for service like Reddit.

## How to install

Should use a virtual environment for the best project isolation. Activate venv and install dependencies:

```bash
pip install -r requirements.txt
```

Pass env variables into .env:

```.env
POSTGRES_DB=db name
POSTGRES_USER=postgres user
POSTGRES_PASSWORD=postgres password
DEBUG=true if needed
SECRET_KEY=exrtra secret key
```

## How to run

```bash
docker-compose up
```
