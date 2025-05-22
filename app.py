
import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("IVIG Resistance & Coronary Aneurysm Risk Prediction")

model = joblib.load("multi_model.pkl")
explainer_ivig = joblib.load("explainer_ivig.pkl")
explainer_aneurysm = joblib.load("explainer_aneurysm.pkl")

features = [
    'Lympho_before', 'PLT_before', 'Chol_before', 'CRP_before',
    'Seg_before', 'TB_before', 'P_before', 'ANC_before',
    'initial_echo_RCA_Z', 'initial_echo_LMCA_Z', 'initial_echo_LAD_Z', 'fever_duration'
]

input_data = {feat: st.number_input(feat, value=0.0) for feat in features}
X_input = pd.DataFrame([input_data])

if st.button("Predict"):
    y_pred_proba = model.predict_proba(X_input)
    st.subheader("Prediction Results")
    st.markdown(f"**IVIG Resistance Probability:** {y_pred_proba[0][0][1]:.2%}")
    st.markdown(f"**Coronary Aneurysm Probability:** {y_pred_proba[1][0][1]:.2%}")

    st.subheader("SHAP Explanation: IVIG Resistance")
    shap_values_ivig = explainer_ivig(X_input)
    fig1 = shap.plots.waterfall(shap_values_ivig[0], show=False)
    st.pyplot(fig1)
    force_html_ivig = shap.plots.force(shap_values_ivig[0], matplotlib=False).html()
    st.components.v1.html(shap.getjs(), height=0)
    st.components.v1.html(force_html_ivig, height=300)

    st.subheader("SHAP Explanation: Coronary Aneurysm")
    shap_values_aneurysm = explainer_aneurysm(X_input)
    fig2 = shap.plots.waterfall(shap_values_aneurysm[0], show=False)
    st.pyplot(fig2)
    force_html_aneurysm = shap.plots.force(shap_values_aneurysm[0], matplotlib=False).html()
    st.components.v1.html(force_html_aneurysm, height=300)
