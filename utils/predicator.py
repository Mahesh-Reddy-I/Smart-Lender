import joblib
import numpy as np

model = joblib.load("models/loan_model.pkl")

# Uncomment these only if your teammates provide them
# scaler = joblib.load("models/scaler.pkl")
# encoder = joblib.load("models/encoder.pkl")


def predict_loan(features):
    """
    features: list of numeric values in the same order
              used during model training
    """

    data = np.array(features).reshape(1, -1)

    # If a scaler is required:
    # data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        return "Loan Approved"

    return "Loan Rejected"