# ChurnIQ — Customer Churn Prediction

A machine-learning web application that estimates customer churn probability using customer demographics, service subscriptions, contract details, and billing information.

**Live Demo:** https://ritika-adk-customer-churn-prediction-app-hdvxee.streamlit.app/  
**GitHub Repository:** https://github.com/ritika-adk/customer-churn-prediction

## Project Overview

Customer churn occurs when a customer stops using a company's service. Identifying customers who may be likely to leave can help businesses investigate retention opportunities.

ChurnIQ uses a Logistic Regression classification pipeline to estimate the probability that a telecommunications customer will churn.

## Features

- Interactive customer information form
- Churn prediction: May Stay or May Churn
- Estimated churn probability
- Preprocessing of numerical and categorical features
- Responsive web interface built with Streamlit

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

## Model and Dataset

The model was trained using the Telco Customer Churn dataset, containing 7,032 customer records after data cleaning and 19 input features.

The machine-learning pipeline includes:
- StandardScaler for numerical features
- OneHotEncoder for categorical features
- LogisticRegression for classification

The data was split into training and test sets using an 80/20 split, with stratification and `random_state=42`.

## Test Set Performance

Evaluation was performed on 1,407 held-out customer records.

| Metric | Result |
|---|---:|
| Accuracy | 80.4% |
| Precision (Churn = Yes) | 64.8% |
| Recall (Churn = Yes) | 57.2% |
| F1-score (Churn = Yes) | 60.8% |
| ROC-AUC | 0.836 |

The model identifies some customers who churn, but it misses a meaningful portion of actual churners at the current classification threshold. These results are a baseline and could be improved through model comparison, threshold tuning, and further evaluation.

## Run Locally

1. Clone this repository:

   git clone https://github.com/ritika-adk/customer-churn-prediction.git
   cd customer-churn-prediction
   

2. Create and activate a virtual environment if desired.

3. Install the dependencies:

   
   pip install -r requirements.txt
   

4. Run the application:

   
   python -m streamlit run app.py
   

5. Open the local URL shown in the terminal.

Ensure "churn_pipeline.joblib" is in the project directory alongside "app.py".

## Limitations

- Predictions are estimates, not guarantees of actual customer behavior.
- Model performance depends on the training dataset and may not generalize to other companies or customer populations.
- The model's current recall indicates that some customers who churn will not be identified.
- This project is an educational portfolio demonstration, not a production decision system.

## Future Improvements

- Compare Logistic Regression with tree-based models
- Evaluate class imbalance and decision thresholds
- Improve recall while monitoring precision
- Add visual summaries of model performance
- Expand documentation and automated testing

## Author

Developed as an AI/ML portfolio project using Python and Streamlit.