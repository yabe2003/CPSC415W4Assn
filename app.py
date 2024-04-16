from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Correct the API URL to point to where the swagger.json file is hosted within your application.
# It should be reachable at http://localhost:8080/swagger.json if it's in the 'static' folder.
SWAGGER_URL = "/api/docs"  # More conventional API doc endpoint
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

@app.route("/")
def home():
    return jsonify({"Message": "You made it!!!"})

@app.route("/access", methods=["GET"])
def access_get():
    name = request.args.get("name", "dipto")
    server = request.args.get("server", "server1")
    message = f"User {name} received access to server {server}"
    return jsonify({"Message": message})

@app.route("/access", methods=["POST"])
def access_post():
    data = request.get_json()
    name = data.get("name", "dipto")
    server = data.get("server", "server1")
    message = f"User {name} received access to server {server}"
    return jsonify({"Message": message})

@app.route("/access", methods=["PUT"])
def access_put():
    data = request.get_json()
    name = data.get("name", "dipto")
    server = data.get("server", "server1")
    message = f"User {name} updated access to server {server}"
    return jsonify({"Message": message})

@app.route("/access", methods=["DELETE"])
def access_delete():
    name = request.args.get("name", "dipto")
    server = request.args.get("server", "server1")
    message = f"User {name}'s access to server {server} has been revoked"
    return jsonify({"Message": message})

if __name__ == "__main__":
    # Ensure you're running on the correct port and that it matches your Docker configuration.
    app.run(host="0.0.0.0", port=8080)  # Changed to 5000 to match common practice and potential Docker config.
