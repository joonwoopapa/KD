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

def load_css() -> None:
    """Load custom CSS styles."""
    with open('styles/main.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 