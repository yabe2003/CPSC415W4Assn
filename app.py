from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
SWAGGER_URL = "/swagger"
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
    return jsonify({
        "Message": "You made it!!!"
    })

@app.route("/access", methods=["GET"])
def access_get():
    name = request.args.get("name", "dipto")
    server = request.args.get("server", "server1")

    message = f"User {name} received access to server {server}"

    return jsonify({
        "Message": message
    })

@app.route("/access", methods=["POST"])
def access():
    data = request.get_json()
    name = data.get("name", "dipto")
    server = data.get("server", "server1")

    message = f"User {name} received access to server {server}"

    return jsonify({
        "Message": message
    })

@app.route("/access", methods=["PUT"])
def access_put():
    data = request.get_json()
    name = data.get("name", "dipto")
    server = data.get("server", "server1")

    message = f"User {name} updated access to server {server}"

    return jsonify({
        "Message": message
    })

@app.route("/access", methods=["DELETE"])
def access_delete():
    name = request.args.get("name", "dipto")
    server = request.args.get("server", "server1")

    message = f"User {name} access to server {server} has been revoked"

    return jsonify({
        "Message": message
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)