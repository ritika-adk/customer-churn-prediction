
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ChurnIQ | Customer Analytics",
    page_icon="📊",
    layout="wide"
)

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(135deg, #0b1120, #111c32, #0b1628);
    color: #e5edf8;
    font-family: 'Inter', sans-serif;
}
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
h1, h2, h3 {
    color: #f1f5f9 !important;
}
p, label {
    color: #cbd5e1;
}
.hero {
    background: linear-gradient(120deg, #172554, #12304a, #134e4a);
    border: 1px solid #294664;
    border-radius: 22px;
    padding: 32px;
    margin-bottom: 24px;
}
.eyebrow {
    color: #5eead4;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 2px;
}
.hero-title {
    color: white;
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 800;
    margin: 12px 0;
}
.hero-description {
    color: #cbd5e1;
    line-height: 1.7;
}
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background-color: #111c30;
    border-color: #354760;
    border-radius: 9px;
}
div[data-baseweb="select"] *,
div[data-baseweb="input"] input {
    color: #f1f5f9 !important;
}
.stFormSubmitButton > button {
    background: linear-gradient(90deg, #2563eb, #0891b2);
    color: white;
    border: none;
    border-radius: 10px;
    min-height: 48px;
    font-weight: 700;
    width: 100%;
}
.stFormSubmitButton > button:hover {
    border: 1px solid #67e8f9;
    color: white;
}
.result-card {
    background: linear-gradient(135deg, #14263e, #102d3a);
    border: 1px solid #2c596b;
    border-radius: 20px;
    padding: 25px;
    margin-top: 12px;
}
.result-label {
    color: #94a3b8;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 1px;
}
.result-value {
    color: #5eead4;
    font-size: 2.5rem;
    font-weight: 800;
    margin: 10px 0;
}
[data-testid="stMetric"] {
    background: #14233a;
    border: 1px solid #293b55;
    border-radius: 14px;
    padding: 16px;
}
[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
}
[data-testid="stMetricValue"] {
    color: #5eead4 !important;
}
.footer {
    border-top: 1px solid #293b55;
    margin-top: 40px;
    padding-top: 20px;
    text-align: center;
    color: #94a3b8;
    font-size: 0.82rem;
}
#MainMenu, footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <div class="eyebrow">AI · CUSTOMER ANALYTICS</div>
    <div class="hero-title">Customer Churn Prediction</div>
    <div class="hero-description">
        Explore customer retention with a machine-learning model.
        Enter customer details to estimate the likelihood of churn.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return joblib.load("churn_pipeline.joblib")

try:
    model = load_model()
    st.success("Prediction engine is ready.")
except Exception as error:
    st.error("Could not load the model. Check the model file and package versions.")
    st.exception(error)
    st.stop()

st.caption("Predictions are estimates, not guarantees.")

# ---------------- INPUT FORM ----------------
st.header("Customer Profile")
st.write("Provide the customer's information below.")

with st.form("customer_form"):

    st.subheader("01 · Customer Information")
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
            "Gender", ["Female", "Male", "Other"]
        )
        senior_citizen = st.selectbox(
            "Senior Citizen", [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes"
        )
        partner = st.selectbox("Has Partner?", ["Yes", "No"])

    with col2:
        dependents = st.selectbox(
            "Has Dependents?", ["Yes", "No"]
        )
        tenure = st.number_input(
            "Tenure (months)", min_value=0,
            max_value=72, value=12
        )

    st.divider()
    st.subheader("02 · Phone and Internet Services")

    col1, col2 = st.columns(2)

    with col1:
        phone_service = st.selectbox(
            "Phone Service", ["Yes", "No"]
        )

        if phone_service == "No":
            multiple_lines = "No phone service"
            st.info("Multiple Lines: No phone service")
        else:
            multiple_lines = st.selectbox(
                "Multiple Lines", ["No", "Yes"]
            )

        internet_service = st.selectbox(
            "Internet Service", ["DSL", "Fiber optic", "No"]
        )

    with col2:
        if internet_service == "No":
            online_security = "No internet service"
            online_backup = "No internet service"
            device_protection = "No internet service"
            tech_support = "No internet service"
            streaming_tv = "No internet service"
            streaming_movies = "No internet service"
            st.info("Internet add-on services are set to No internet service.")
        else:
            online_security = st.selectbox(
                "Online Security", ["Yes", "No"]
            )
            online_backup = st.selectbox(
                "Online Backup", ["Yes", "No"]
            )
            device_protection = st.selectbox(
                "Device Protection", ["Yes", "No"]
            )
            tech_support = st.selectbox(
                "Tech Support", ["Yes", "No"]
            )
            streaming_tv = st.selectbox(
                "Streaming TV", ["Yes", "No"]
            )
            streaming_movies = st.selectbox(
                "Streaming Movies", ["Yes", "No"]
            )

    st.divider()
    st.subheader("03 · Contract and Billing")

    col1, col2 = st.columns(2)

    with col1:
        contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"]
        )
        paperless_billing = st.selectbox(
            "Paperless Billing", ["Yes", "No"]
        )

    with col2:
        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    col1, col2 = st.columns(2)

    with col1:
        monthly_charges = st.number_input(
            "Monthly Charges ($)",
            min_value=0.0, value=70.0, step=1.0
        )

    with col2:
        total_charges = st.number_input(
            "Total Charges ($)",
            min_value=0.0, value=840.0, step=1.0
        )

    st.caption("Use realistic customer details for meaningful results.")
    submitted = st.form_submit_button("Generate Churn Prediction")

# ---------------- PREDICTION ----------------
if submitted:
    customer = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])

    try:
        prediction = model.predict(customer)[0]
        probabilities = model.predict_proba(customer)[0]
        churn_probability = probabilities[
            list(model.classes_).index("Yes")
        ]

        st.divider()
        st.header("Prediction Results")

        result_col, probability_col = st.columns([1.2, 1])

        with result_col:
            if prediction == "Yes":
                heading = "May Churn"
                description = (
                    "The model predicts this customer may leave the service."
                )
                st.warning("Higher predicted churn risk")
            else:
                heading = "May Stay"
                description = (
                    "The model predicts this customer may remain with the service."
                )
                st.success("Lower predicted churn risk")

            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">MODEL PREDICTION</div>
                <div class="result-value">{heading}</div>
                <div>{description}</div>
            </div>
            """, unsafe_allow_html=True)

        with probability_col:
            st.metric(
                "Estimated Churn Probability",
                f"{churn_probability:.1%}"
            )
            st.progress(float(churn_probability))
            st.write(
                f"Estimated probability of staying: "
                f"{1 - churn_probability:.1%}"
            )

        with st.expander("View submitted customer information"):
            st.dataframe(customer, use_container_width=True)

    except Exception as error:
        st.error("Prediction failed. Please check the inputs and model.")
        st.exception(error)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    ChurnIQ · Customer Churn Prediction<br>
    Built with Python, Pandas, Scikit-learn and Streamlit<br>
    Educational demonstration — predictions may be inaccurate.
</div>
""", unsafe_allow_html=True)
