"""Train and evaluate the Flood Risk Prediction model.

IMPORTANT:
The included CSV is synthetic demonstration data. Replace it with verified,
properly labelled historical/local data before making real-world claims.
"""
from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "flood_dataset.csv"
MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)
MODEL_PATH = MODEL_DIR / "flood_model.joblib"
METRICS_PATH = MODEL_DIR / "evaluation_metrics.json"

FEATURES = [
    "rainfall_mm", "elevation_m", "drainage_capacity",
    "soil_moisture_pct", "river_distance_km",
    "slope_degree", "urban_surface_pct"
]
TARGET = "flood_risk"

def main():
    data = pd.read_csv(DATA_PATH)
    required = FEATURES + [TARGET]
    missing = [c for c in required if c not in data.columns]
    if missing:
        raise ValueError(f"Dataset is missing columns: {missing}")

    X = data[FEATURES]
    y = data[TARGET].astype(str)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    model = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("classifier", RandomForestClassifier(
            n_estimators=250, max_depth=12,
            min_samples_split=4, random_state=42,
            class_weight="balanced"
        ))
    ])
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, output_dict=True, zero_division=0)
    matrix = confusion_matrix(y_test, predictions, labels=["Low", "Medium", "High"])

    joblib.dump({"model": model, "features": FEATURES}, MODEL_PATH)
    metrics = {
        "accuracy": round(float(accuracy), 4),
        "classification_report": report,
        "confusion_matrix": matrix.tolist(),
        "class_order": ["Low", "Medium", "High"],
        "test_records": int(len(y_test)),
        "dataset_note": "Synthetic demonstration dataset; metrics are not evidence of real-world flood forecasting performance."
    }
    METRICS_PATH.write_text(json.dumps(metrics, indent=2))
    print(f"Training completed. Test accuracy: {accuracy:.3f}")
    print(classification_report(y_test, predictions, zero_division=0))
    print(f"Saved model: {MODEL_PATH}")
    print(f"Saved metrics: {METRICS_PATH}")

if __name__ == "__main__":
    main()
