from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("student_scores.csv")

@app.route("/")
def home():
    return "Student API is running. Use /students endpoint."

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)

