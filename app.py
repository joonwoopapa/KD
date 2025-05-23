import streamlit as st
import sys
import os
import traceback

from src.config import FEATURES
from src.models import KDPredictor
from src.utils import load_css, validate_input_data
from src.components import (
    render_page_header,
    render_required_notice,
    render_debug_info,
    render_input_sections,
    render_predict_button
)
from src.visualization import (
    display_prediction_cards,
    display_combined_shap_analysis,
    display_detailed_shap_analysis
)

# Must be the first Streamlit command
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Load CSS
load_css()

# Add logo and title in the same row
col1, col2 = st.columns([3, 7])
with col1:
    st.markdown('<div style="padding-top: 30px;">', unsafe_allow_html=True)
    st.image('snuh_nukki.png', width=400)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<h1 style="margin-top: 50px; text-align: left; margin-left: -8rem;">IVIG Resistance & Coronary Aneurysm Risk Prediction</h1>', unsafe_allow_html=True)

# Add sidebar maintainer info
with st.sidebar:
    st.markdown('<h3 style="color: white;">Maintainer</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color: white;">Wooyoung, Park</p>', unsafe_allow_html=True)

# Initialize session state for field validation
if 'invalid_fields' not in st.session_state:
    st.session_state.invalid_fields = set()

# Initialize predictor
predictor = KDPredictor()

# Render page layout
render_page_header()
render_required_notice()
render_debug_info()

# Render input sections and collect data
input_data = render_input_sections(FEATURES, st.session_state.invalid_fields)

# Render predict button
if render_predict_button():
    # Clear previous invalid fields
    st.session_state.invalid_fields.clear()
    
    # Validate input data
    invalid_fields = validate_input_data(input_data, FEATURES)
    
    if invalid_fields:
        st.session_state.invalid_fields = invalid_fields
        st.error("❌ Required fields are missing. Please check the fields highlighted in red.")
        st.rerun()
    else:
        try:
            with st.spinner('Calculating predictions...'):
                # Get predictions and SHAP values
                results = predictor.predict(input_data)
                
                # Display prediction results
                display_prediction_cards(results['probabilities'])

                # SHAP Explanations
                st.markdown("### Model Explanations")
                tabs = st.tabs(["Overall View", "IVIG Resistance", "Coronary Aneurysm"])
                
                with tabs[0]:
                    display_combined_shap_analysis(results['shap_values'])
                
                with tabs[1:]:
                    display_detailed_shap_analysis(results['shap_values'])

        except Exception as e:
            with st.sidebar:
                with st.expander("🔧 Debug Information", expanded=True):
                    st.error(f"Prediction Error: {str(e)}")
                    st.error("Full error details:")
                    st.code(traceback.format_exc())
