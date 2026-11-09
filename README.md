# Flood Risk Prediction Using Rainfall and Environmental Data

**Student:** SATISH SHASHIKUMAR CHIMANAPPAGOL  
**Register No.:** 8080134  
**Course:** Diploma in Artificial Intelligence and Machine Learning

## Project summary
This educational prototype uses a Random Forest classifier to estimate a flood-risk category (Low, Medium, High) from rainfall and environmental features. It displays class scores and the input factors used.

ಕನ್ನಡದಲ್ಲಿ: ಈ ಪ್ರಾಜೆಕ್ಟ್ ಮಳೆಯ ಪ್ರಮಾಣ ಮತ್ತು ಪರಿಸರದ ಅಂಶಗಳನ್ನು ಆಧರಿಸಿ Low, Medium ಅಥವಾ High flood-risk category ಅನ್ನು Machine Learning ಮೂಲಕ ಅಂದಾಜು ಮಾಡುತ್ತದೆ.

## Important dataset disclaimer
The included `flood_dataset.csv` is **synthetic demonstration data generated for software testing**. It is not verified historical flood data and must not be described as real observations. Model scores/accuracy on this data do not demonstrate real-world forecasting performance. For a serious research evaluation, replace it with verified local/historical observations and documented flood labels.

## Features
- `rainfall_mm`: rainfall amount in millimetres
- `elevation_m`: elevation in metres
- `drainage_capacity`: illustrative drainage score from 0 (poor) to 100 (good)
- `soil_moisture_pct`: soil moisture percentage
- `river_distance_km`: distance from river in kilometres
- `slope_degree`: land slope in degrees
- `urban_surface_pct`: built-up/impervious surface percentage
- `flood_risk`: target label (Low / Medium / High)

These features are demonstration inputs. Confirm units, measurement methods, and availability before using any real dataset.

## Requirements
- Python 3.10 or newer recommended
- VS Code or another Python editor
- Internet only for installing packages (after installation, the app can run locally)

## Run in VS Code (Windows PowerShell)
1. Extract the ZIP folder.
2. Open the extracted folder in VS Code.
3. Open Terminal > New Terminal.
4. Create a virtual environment:
   `py -m venv .venv`
5. Activate it:
   `.venv\Scripts\Activate.ps1`
   If PowerShell blocks activation, use Command Prompt terminal and run:
   `.venv\Scripts\activate.bat`
   Or run commands using `.venv\Scripts\python.exe` without activation.
6. Install libraries:
   `python -m pip install -r requirements.txt`
7. Train the model:
   `python train_model.py`
8. Start the website:
   `python -m streamlit run app.py`
9. Open the local URL shown in the terminal, normally `http://localhost:8501`.

## Kannada steps
1. ZIP file extract ಮಾಡಿ.
2. VS Code ನಲ್ಲಿ folder open ಮಾಡಿ.
3. Terminal open ಮಾಡಿ.
4. `py -m venv .venv` ಮೂಲಕ virtual environment ರಚಿಸಿ.
5. `python -m pip install -r requirements.txt` ಮೂಲಕ libraries install ಮಾಡಿ.
6. `python train_model.py` ಮೂಲಕ model train ಮಾಡಿ.
7. `python -m streamlit run app.py` ಮೂಲಕ website start ಮಾಡಿ.
8. Browser ನಲ್ಲಿ terminal ತೋರಿಸುವ local URL open ಮಾಡಿ.

## Main files
- `app.py`: Streamlit website and prediction interface
- `train_model.py`: preprocessing, model training, evaluation, model saving
- `flood_dataset.csv`: synthetic demonstration dataset
- `requirements.txt`: required Python packages
- `models/`: trained model and evaluation metrics are saved here after training

## Viva explanation
**What is the project?**  
This project estimates flood-risk categories using rainfall and environmental data with a Random Forest machine-learning classifier. It displays a category and model class scores in a Streamlit dashboard.

**ಕನ್ನಡ:** ಮಳೆ ಮತ್ತು ಪರಿಸರದ ಮಾಹಿತಿಯನ್ನು ಬಳಸಿ Random Forest algorithm ಮೂಲಕ ಪ್ರವಾಹದ ಅಪಾಯವನ್ನು Low, Medium ಅಥವಾ High ಎಂದು ಅಂದಾಜು ಮಾಡುವ project ಇದು.

**Which algorithm is used?** Random Forest Classifier.

**What is the output?** Predicted risk category and model class probability scores.

**Is it an official warning system?** No. It is an educational prototype only.

## Limitations and future enhancement
- Replace synthetic data with verified historical/local data.
- Add location, date/time, upstream river level, and time-window rainfall when reliable data is available.
- Validate on separate locations and time periods to avoid data leakage.
- Consult domain experts and official disaster-management agencies before any operational use.
