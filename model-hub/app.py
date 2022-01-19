import uuid

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "modelhubdb"
app.config["MONGO_URI"] = "mongodb://localhost:27017/modelhubdb"

mongo = PyMongo(app)


@app.route("/models", methods=["GET"])
def get_all_models():
    print("retrieving all models")
    model = mongo.db.models
    output = []
    for s in model.find():
        output.append(
            {
                "name": s["name"],
                "model_url": s["model_url"],
                "internal_model_id": s["internal_model_id"],
                "version": s["version"],
                "description": s["description"],
                "author": s["author"],
                "namespace": s["namespace"],
                "ludwig_version": s["ludwig_version"],
            }
        )

    return jsonify({"result": output})


@app.route("/models/<path:model_url>", methods=["GET"])
def get_one_model(model_url):
    model = mongo.db.models
    s = model.find_one({"model_url": model_url})
    if s:
        output = {
            "name": s["name"],
            "model_url": s["model_url"],
            "description": s["description"],
            "version": s["version"],
            "ludwig_version": s["ludwig_version"],
            "internal_model_id": s["internal_model_id"],
            "author": s["author"],
            "namespace": s["namespace"],
        }
    else:
        output = "No such model"
    return jsonify({"result": output})


@app.route("/models", methods=["POST"])
def add_model():
    model = mongo.db.models
    model_url = request.json["model_url"]
    name = request.json["name"]
    description = request.json["description"]
    version = request.json["version"]
    ludwig_version = request.json["ludwig_version"]
    internal_model_id = uuid.uuid4()
    author = request.json["author"]
    namespace = request.json["namespace"]

    model_id = model.insert(
        {
            "name": name,
            "model_url": model_url,
            "description": description,
            "version": version,
            "ludwig_version": ludwig_version,
            "internal_model_id": internal_model_id,
            "author": author,
            "namespace": namespace,
        }
    )

    new_model = model.find_one({"_id": model_id})
    output = {
        "name": new_model["name"],
        "model_url": new_model["model_url"],
        "description": new_model["description"],
        "version": new_model["version"],
        "ludwig_version": new_model["ludwig_version"],
        "internal_model_id": new_model["internal_model_id"],
        "author": new_model["author"],
        "namespace": new_model["namespace"],
    }

    return jsonify({"result": output})


if __name__ == "__main__":
    app.run(debug=True)
