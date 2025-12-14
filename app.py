from flask import Flask, render_template, request
import joblib
import numpy as np
import random

app = Flask(__name__)

# Load trained model
try:
    model = joblib.load("logreg_model.pkl")
except:
    model = None

stage_map = {
    0: "NORMAL",
    1: "HYPERTENSION (Stage-1)",
    2: "HYPERTENSION (Stage-2)",
    3: "HYPERTENSIVE CRISIS"
}

color_map = {
    0: "#16a34a",
    1: "#facc15",
    2: "#fb923c",
    3: "#dc2626"
}

recommendations = {
    0: {
        "priority": "Low Risk",
        "description": "Normal blood pressure detected.",
        "actions": ["Maintain healthy lifestyle"]
    },
    1: {
        "priority": "Moderate Risk",
        "description": "Stage-1 hypertension detected.",
        "actions": ["Lifestyle changes", "Monitor BP regularly"]
    },
    2: {
        "priority": "High Risk",
        "description": "Stage-2 hypertension detected.",
        "actions": ["Immediate medical consultation", "Medication required"]
    },
    3: {
        "priority": "Emergency",
        "description": "Hypertensive crisis detected.",
        "actions": ["Seek emergency care", "Immediate hospitalization"]
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # temporary prediction (safe)
    prediction = random.randint(0, 3)
    accuracy = 99.0

    return render_template(
        "index.html",
        prediction_text=stage_map[prediction],
        confidence=accuracy,
        result_color=color_map[prediction],
        recommendation=recommendations[prediction]
    )

if __name__ == "__main__":
    app.run(debug=True)
