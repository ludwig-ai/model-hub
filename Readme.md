# Model Hub Readme
Welcome to the model-hub project, for now this is a very simple flask based api requiring mongo-db community edition to be installed locally in your environment.

# Running Model Hub
cd to model-hub internal directory and type in python3 app.py

# Current set of APIs
## get_all_models
Returns the current list of models in your mongo db instance

## get_one_model
Returns a single model based on the model url

## add_model
Add a model, specifically the following information about a model is needed:
* model_url (The url for the model used to query the model after its already authored)
* name (The name of the model)
* description (A brief description of the model)
* version (The version of the model, should have the major and minor version embedded)
* ludwig_version (This is a version internal to ludwig)
* author (The authors of the model)
* namespace  (The namespace where the model should reside)