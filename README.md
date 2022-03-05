# Model_hub built on top of fastapi and mongodb

## Features

- Docker image with mongodb and fastapi local install
- Ability to create one model with the following payload:
{
    "_id": "6223f652abc1bffae909c245",
    "name": "ensemble_model",
    "model_url": "/saikat/testing/model",
    "description": "model_description",
    "version": "model_version",
    "ludwig_version": "1.0",
    "author": "saikat",
    "namespace": "ns_model"
}
Due to mongodb creating internal id you only need to specify the rest of the fields
Sample url is an http POST action with the following url: http://localhost:8000/api/models with the above parms except id passed in as json

- Ability to retrieve all the models, sample url is here GET http://localhost:8000/api/models
- Ability to retrieve one model based on the model_url , sample url is here GET http://localhost:8000/api/models/one/model?model_url=/saikat/testing/model

## Installation and usage

- Create env from template: `cp example.env .env` (only once), this will create a path for the local mongodb collection
- Run docker stack `docker-compose up --build` to build the image and run both fastapi and mongodb locally and then access using the endpoints above

### FastAPI Bug with retrieving a single model based on model_url
- For retrieving a model based on the model_url we need to come up with a better url structure but wont be able to use path params due to the fact that they contain slashes, issue documented here: https://github.com/tiangolo/fastapi/issues/1750


## TODO

- Delete
- Setup mongo and fastapi instance on linux foundation
- Make the get based on model_url have a better url structure
- unit tests
- end to end integration tests
- code cleanup for cleaner mongo install
- local testing by ludwig committers--bug fixes due to this
