import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib
import os

MODEL_PATH = "ai_engine/credit_model.pkl"


def train_model():
    # Dummy training dataset
    X = np.array(
        [
            [750, 50000, 100000, 5, 10000],
            [600, 30000, 150000, 2, 40000],
            [580, 25000, 2000000, 1, 60000],
            [800, 90000, 250000, 8, 20000],
            [600, 30000, 1500000, 3, 8000],
            [580, 25000, 2000000, 2.5, 10000],
        ]
    )

    # 0 = No Default, 1 = Default
    y = np.array([0, 1, 1, 0, 0, 0])

    model = LogisticRegression()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    print("Model Trained and Saved!")


def load_model():
    if not os.path.exists(MODEL_PATH):
        train_model()
    return joblib.load(MODEL_PATH)


def predict_risk(data):
    model = load_model()
    prediction = model.predict_proba([data])[0][1]
    return prediction
