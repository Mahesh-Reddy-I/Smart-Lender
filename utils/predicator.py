import os
import joblib
import numpy as np

# Base directory of project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "best_loan_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")

# Load once when application starts
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


def predict_loan(features):
    """
    Parameters
    ----------
    features : list
        List of 11 features in the exact order used during training.

    Returns
    -------
    int
        0 -> Loan Rejected
        1 -> Loan Approved
    """

    data = np.array(features).reshape(1, -1)

    # Scale features
    data = scaler.transform(data)

    prediction = model.predict(data)

    return int(prediction[0])