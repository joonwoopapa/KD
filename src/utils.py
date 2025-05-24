from typing import Set
import streamlit as st
from .types import Features, InputData

def validate_input_data(
    input_data: InputData,
    features: Features
) -> Set[str]:
    """
    Validate input data and return set of invalid field keys.
    
    Args:
        input_data: Dictionary of input values
        features: Feature configuration
        
    Returns:
        Set of field keys that are invalid (zero values)
    """
    invalid_fields = set()
    
    for section_key, section in features.items():
        for field_key in section['fields'].keys():
            if input_data[field_key] == 0:
                invalid_fields.add(field_key)
                
    return invalid_fields

def load_css():
    """Load custom CSS styles."""
    st.markdown("""
        <style>
            /* Override dark mode */
            .stApp {
                background-color: white;
            }

            .stMarkdown {
                color: #2c3e50;
            }

            /* Tab styling */
            .stTabs [data-baseweb="tab-list"] {
                gap: 2rem;
            }

            .stTabs [data-baseweb="tab"] {
                height: 50px;
                white-space: pre-wrap;
                color: black !important;
                font-weight: 500;
            }

            .stTabs [data-baseweb="tab-list"] button {
                font-size: 1rem;
            }

            .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
                color: black !important;
                font-weight: 600;
            }

            /* Input field styles */
            div[data-testid="stNumberInput"] input {
                color: white !important;
                background-color: black !important;
            }

            /* Required field indicator */
            .required-indicator {
                color: #e53e3e;
                margin-left: 4px;
            }

            /* Input label */
            .input-label {
                color: #4a5568;
                font-size: 0.95rem;
                margin-bottom: 4px;
            }

            /* Invalid input styles */
            .invalid-label {
                color: #e53e3e !important;
            }

            .validation-message {
                color: #e53e3e;
                font-size: 0.8rem;
                margin-top: 4px;
            }

            /* Section title */
            .section-title {
                color: #2c3e50;
                font-size: 1.1rem;
                font-weight: 600;
                margin-bottom: 15px;
                padding-bottom: 8px;
                border-bottom: 1px solid #e0e0e0;
            }
        </style>
    """, unsafe_allow_html=True) 