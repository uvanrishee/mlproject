# End-to-End Machine Learning Project

A production-style machine learning project built using Python, Flask, and Scikit-learn.

This project covers the complete ML lifecycle:

- Data ingestion
- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Prediction pipeline
- Web deployment using Flask

---

## Project Overview

This project predicts student performance based on demographic and academic features.

The application allows users to input student details through a web interface and get predicted scores using a trained machine learning model.

---

## Features

✅ Modular project structure  
✅ Custom exception handling  
✅ Logging implementation  
✅ Data transformation pipeline  
✅ Model training pipeline  
✅ Prediction pipeline  
✅ Flask web application  
✅ CatBoost + Ensemble model support  

---

## Project Structure

```bash
mlproject/
│
├── artifact/                 # Saved models and preprocessors
├── catboost_info/            # CatBoost training logs
├── notebook/                 # Jupyter notebooks and experiments
├── src/                      # Source code
│   ├── components/           # Data ingestion, transformation, training
│   ├── pipeline/             # Prediction and training pipelines
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│
├── templates/                # HTML templates
├── application.py            # Flask application
├── setup.py
├── requirments.txt
├── README.md
```

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- CatBoost
- XGBoost
- Flask
- HTML/CSS

---

## Installation

### 1. Clone repository

```bash
git clone https://github.com/uvanrishee/mlproject.git
cd mlproject
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirments.txt
```

---

## Run Application

```bash
python application.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

## Input Features

The model takes:

- Gender
- Race/Ethnicity
- Parental education
- Lunch type
- Test preparation course
- Reading score
- Writing score

---

## ML Pipeline

### Data Ingestion

Loads dataset and splits into train/test sets.

### Data Transformation

- Missing value handling
- Encoding categorical features
- Feature scaling

### Model Training

Models evaluated:

- Linear Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- CatBoost
- AdaBoost

Best model is saved automatically.

### Prediction Pipeline

Loads trained model and preprocessor to generate predictions.

---

## Screenshots

Add screenshots of:

- Home page
- Prediction form
- Output page

---

## Future Improvements

- Docker deployment
- CI/CD pipeline
- Cloud deployment
- Experiment tracking with MLflow
- API endpoints

---

## Author

👨‍💻 Uvan Rishee

Engineering Student | Machine Learning Enthusiast

GitHub: https://github.com/uvanrishee

---

## License

This project is for educational and portfolio purposes.
