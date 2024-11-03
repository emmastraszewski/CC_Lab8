from flask import Flask, request, jsonify
from service import MealService
from models import Schema

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def hello():
    return "Welcome to the Weekly Meal Planner API!"

@app.route("/meals", methods=["GET"])
def list_meals():
    return jsonify(MealService().list())

@app.route("/meals", methods=["POST"])
def create_meal():
    return jsonify(MealService().create(request.get_json()))

@app.route("/meals/<day>", methods=["GET"])
def get_meal(day):
    return jsonify(MealService().get_by_day(day))

@app.route("/meals/<day>", methods=["PUT"])
def update_meal(day):
    return jsonify(MealService().update(day, request.get_json()))

@app.route("/meals/<day>", methods=["DELETE"])
def delete_meal(day):
    return jsonify(MealService().delete(day))

if __name__ == "__main__":
    Schema()
    app.run(debug=True, host='0.0.0.0', port=5000)