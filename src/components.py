import streamlit as st
import sys
import os
from typing import Dict, Any
from .types import Features, InputData

def render_page_header() -> None:
    """Render the page title."""
    st.markdown("""
        <h1 style='
            color: #2d3748;
            font-size: 2.2rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            text-align: center;
        '>
            IVIG Resistance & Coronary Aneurysm Risk Prediction
        </h1>
    """, unsafe_allow_html=True)

def render_required_notice() -> None:
    """Render the required fields notice."""
    st.markdown("""
        <div style='
            background-color: #f8fafc;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            margin-bottom: 1.5rem;
            border-left: 3px solid #3182ce;
            max-width: 600px;
        '>
            <p style='
                margin: 0;
                color: #4a5568;
                font-size: 0.9rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            '>
                <span style='color: #3182ce;'>ℹ️</span>
                <span><strong>All fields are required.</strong> Prediction is not possible if any measurements are missing.</span>
            </p>
        </div>
    """, unsafe_allow_html=True)

def render_debug_info() -> None:
    """Render debug information in sidebar."""
    with st.sidebar:
        with st.expander("🔧 Debug Information", expanded=False):
            try:
                import numpy as np
                st.markdown("**System Information:**")
                st.code(f"""
Python version: {sys.version}
NumPy version: {np.__version__}
NumPy path: {np.__file__}
Working directory: {os.getcwd()}
                """)
                st.success("✓ All models loaded successfully")
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.error(f"Directory contents: {os.listdir('.')}")
                sys.exit(1)

def render_input_field(
    field_key: str,
    field_label: str,
    is_invalid: bool = False
) -> float:
    """Render an input field with validation."""
    label_class = "invalid-label" if is_invalid else ""
    
    # Display label with required indicator
    st.markdown(f"""
        <div class="input-label {label_class}">
            {field_label}
            <span class="required-indicator">*</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Create input field
    value = st.number_input(
        label=field_label,
        value=0.0,
        format="%.2f" if field_key != 'fever_duration' else "%.1f",
        key=field_key,
        label_visibility="collapsed"
    )
    
    # Show validation message if invalid
    if is_invalid:
        st.markdown(f"""
            <div class="validation-message">
                ⚠️ This field is required
            </div>
        """, unsafe_allow_html=True)
        
        # Apply invalid style
        st.markdown(f"""
            <style>
                div[data-testid="stNumberInput"] #{field_key} {{
                    border-color: #e53e3e !important;
                    background-color: #fff5f5 !important;
                    box-shadow: 0 0 0 1px #e53e3e !important;
                }}
            </style>
        """, unsafe_allow_html=True)
    
    return value

def render_input_sections(
    features: Features,
    invalid_fields: set
) -> InputData:
    """Render all input sections and return collected data."""
    cols = st.columns(3)
    input_data: InputData = {}
    
    for i, (section_key, section) in enumerate(features.items()):
        with cols[i]:
            st.markdown(f"<div class='section-title'>{section['title']}</div>", unsafe_allow_html=True)
            for field_key, field_label in section['fields'].items():
                input_data[field_key] = render_input_field(
                    field_key=field_key,
                    field_label=field_label,
                    is_invalid=field_key in invalid_fields
                )
    
    return input_data

def render_predict_button() -> bool:
    """Render the centered predict button."""
    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        return st.button("Predict", use_container_width=True) 