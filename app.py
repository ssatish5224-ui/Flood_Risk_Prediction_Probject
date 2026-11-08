from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "flood_model.joblib"

st.set_page_config(page_title="Flood Risk Prediction", page_icon="🌧️", layout="wide")

@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        return None
    return joblib.load(MODEL_PATH)

st.title("🌧️ Flood Risk Prediction System")
st.subheader("Using Rainfall and Environmental Data")
st.write("Enter environmental values to view a dataset-based flood-risk category.")

st.info(
    "Prototype disclaimer: This student project is an educational demonstration, "
    "not an official flood-warning system. The included dataset is synthetic demo data. "
    "Do not use predictions for emergency or evacuation decisions."
)

bundle = load_model()
if bundle is None:
    st.error("Model file not found. First run: python train_model.py")
    st.stop()

model = bundle["model"]
features = bundle["features"]

st.sidebar.header("Environmental Inputs")
rainfall = st.sidebar.number_input("Rainfall (mm)", min_value=0.0, max_value=1000.0, value=180.0, step=5.0)
elevation = st.sidebar.number_input("Elevation (metres)", min_value=0.0, max_value=5000.0, value=100.0, step=5.0)
drainage = st.sidebar.slider("Drainage capacity (0 = poor, 100 = good)", 0.0, 100.0, 40.0)
soil = st.sidebar.slider("Soil moisture (%)", 0.0, 100.0, 65.0)
river = st.sidebar.number_input("Distance from river (km)", min_value=0.0, max_value=200.0, value=2.0, step=0.5)
slope = st.sidebar.slider("Land slope (degrees)", 0.0, 60.0, 5.0)
urban = st.sidebar.slider("Urban / built-up surface (%)", 0.0, 100.0, 50.0)

input_data = pd.DataFrame([{
    "rainfall_mm": rainfall,
    "elevation_m": elevation,
    "drainage_capacity": drainage,
    "soil_moisture_pct": soil,
    "river_distance_km": river,
    "slope_degree": slope,
    "urban_surface_pct": urban
}], columns=features)

left, right = st.columns([1, 1])
with left:
    st.markdown("### Input summary")
    st.dataframe(input_data.T.rename(columns={0: "Entered value"}), use_container_width=True)

if st.button("Predict Flood Risk", type="primary", use_container_width=True):
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    classes = list(model.classes_)
    confidence = float(max(probabilities)) * 100

    with right:
        st.markdown("### Prediction result")
        if prediction == "High":
            st.error(f"Predicted category: {prediction} Risk")
        elif prediction == "Medium":
            st.warning(f"Predicted category: {prediction} Risk")
        else:
            st.success(f"Predicted category: {prediction} Risk")
        st.metric("Model confidence score", f"{confidence:.1f}%")
        st.caption("This is the model's highest class probability, not a verified probability of an actual flood.")

    st.markdown("### Class probability scores")
    probability_frame = pd.DataFrame({
        "Risk category": classes,
        "Model score (%)": [round(float(p) * 100, 2) for p in probabilities]
    })
    st.bar_chart(probability_frame.set_index("Risk category"))
    st.markdown("### Factors considered")
    st.write(", ".join(features))
    st.caption("Prediction depends on the training dataset and its quality. It is not an official warning.")

st.divider()
st.caption("Student Project | SATISH SHASHIKUMAR CHIMANAPPAGOL | Register No. 8080134")
