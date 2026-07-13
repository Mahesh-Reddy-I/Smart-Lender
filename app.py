from flask import Flask, render_template, request
from utils.predicator import predict_loan

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict")
def predict():
    return render_template("predict.html")


@app.route("/submit", methods=["POST"])
def submit():

    # -----------------------
    # Read Form Data
    # -----------------------

    gender = request.form["gender"]
    married = request.form["married"]
    dependents = request.form["dependents"]
    education = request.form["education"]
    self_employed = request.form["self_employed"]

    applicant_income = float(request.form["applicant_income"])
    coapplicant_income = float(request.form["coapplicant_income"])
    loan_amount = float(request.form["loan_amount"])
    loan_term = float(request.form["loan_term"])
    credit_history = float(request.form["credit_history"])
    property_area = request.form["property_area"]

    # -----------------------
    # Manual Encoding
    # -----------------------

    gender = 1 if gender == "Male" else 0

    married = 1 if married == "Yes" else 0

    education = 0 if education == "Graduate" else 1

    self_employed = 1 if self_employed == "Yes" else 0

    property_mapping = {
        "Rural": 0,
        "Semiurban": 1,
        "Urban": 2
    }

    property_area = property_mapping[property_area]

    dependents_mapping = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3+": 3
    }

    dependents = dependents_mapping[dependents]

    # -----------------------
    # Feature Order
    # -----------------------

    features = [
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area
    ]

    prediction = predict_loan(features)

    if prediction == 1:
        result = "Loan Approved ✅"
    else:
        result = "Loan Rejected ❌"

    return render_template(
        "submit.html",
        prediction=result
    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)