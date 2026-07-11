from flask import Flask, render_template, request

app = Flask(__name__)


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("home.html")


# -----------------------------
# Loan Form
# -----------------------------
@app.route("/predict")
def predict():
    return render_template("predict.html")


# -----------------------------
# Form Submission
# -----------------------------
@app.route("/submit", methods=["POST"])
def submit():

    # Read form values
    name = request.form.get("name")

    gender = request.form.get("gender")
    married = request.form.get("married")
    dependents = request.form.get("dependents")

    education = request.form.get("education")
    self_employed = request.form.get("self_employed")

    applicant_income = request.form.get("applicant_income")
    coapplicant_income = request.form.get("coapplicant_income")

    loan_amount = request.form.get("loan_amount")
    loan_term = request.form.get("loan_term")

    credit_history = request.form.get("credit_history")

    property_area = request.form.get("property_area")

    # -----------------------------
    # Print values (Testing)
    # -----------------------------

    print("\n========== Loan Application ==========")

    print("Name:", name)
    print("Gender:", gender)
    print("Married:", married)
    print("Dependents:", dependents)
    print("Education:", education)
    print("Self Employed:", self_employed)
    print("Applicant Income:", applicant_income)
    print("Co-applicant Income:", coapplicant_income)
    print("Loan Amount:", loan_amount)
    print("Loan Term:", loan_term)
    print("Credit History:", credit_history)
    print("Property Area:", property_area)

    print("======================================\n")

    # ----------------------------------------------------
    # Dummy Prediction
    # Replace this after receiving the trained ML model
    # ----------------------------------------------------

    prediction = "Loan Approved"

    # ----------------------------------------------------
    # Future ML Integration
    #
    # from utils.predictor import predict_loan
    #
    # features = [...]
    #
    # prediction = predict_loan(features)
    # ----------------------------------------------------

    return render_template(
        "submit.html",
        prediction=prediction
    )


# -----------------------------
# Run Flask
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)