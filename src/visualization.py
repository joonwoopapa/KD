import streamlit as st
import matplotlib.pyplot as plt
import shap
from .config import WATERFALL_PLOT_SIZE_SINGLE, WATERFALL_PLOT_SIZE_COMBINED, PLOT_PADDING

def display_prediction_cards(probabilities: dict):
    """Display prediction results in card layout."""
    st.markdown(f"""
        <div style='
            display: flex;
            justify-content: space-around;
            margin: 2rem 0;
            gap: 2rem;
        '>
            <div style='
                flex: 1;
                background: #f0f9ff;
                padding: 1.5rem;
                border-radius: 8px;
                text-align: center;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            '>
                <h3 style='color: #2563eb; margin-bottom: 0.5rem;'>IVIG Resistance</h3>
                <p style='font-size: 1.5rem; font-weight: 600;'>{probabilities['ivig']:.1%}</p>
            </div>
            <div style='
                flex: 1;
                background: #f0f9ff;
                padding: 1.5rem;
                border-radius: 8px;
                text-align: center;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            '>
                <h3 style='color: #2563eb; margin-bottom: 0.5rem;'>Coronary Aneurysm</h3>
                <p style='font-size: 1.5rem; font-weight: 600;'>{probabilities['aneurysm']:.1%}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

def plot_shap_waterfall(shap_values, title, size):
    """Create and display a SHAP waterfall plot."""
    plt.figure(figsize=size)
    shap.plots.waterfall(shap_values, show=False)
    fig = plt.gcf()
    plt.title(title, pad=PLOT_PADDING)
    st.pyplot(fig)
    plt.close()

def display_combined_shap_analysis(shap_values: dict):
    """Display combined SHAP analysis for both predictions."""
    st.markdown("#### Combined Feature Importance Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### IVIG Resistance Prediction")
        plot_shap_waterfall(
            shap_values['ivig'],
            "IVIG Resistance Impact",
            WATERFALL_PLOT_SIZE_COMBINED
        )

    with col2:
        st.markdown("##### Coronary Aneurysm Prediction")
        plot_shap_waterfall(
            shap_values['aneurysm'],
            "Coronary Aneurysm Impact",
            WATERFALL_PLOT_SIZE_COMBINED
        )

    st.markdown("""
    #### Understanding the Waterfall Plots
    
    These plots show how different features affect both predictions simultaneously:
    
    * 🔴 **Positive Values (Red)**: Increase the likelihood of the condition
    * 🔵 **Negative Values (Blue)**: Decrease the likelihood of the condition
    * 📏 **Bar Length**: Shows the strength of each feature's influence
    * 🔄 **Comparison**: You can compare how the same feature might have different impacts on each condition
    
    Features are ordered by their absolute impact in each plot, with the most influential features at the top.
    """)

def display_detailed_shap_analysis(shap_values: dict, prediction_type: str):
    """Display detailed SHAP analysis for a specific prediction type."""
    if prediction_type == 'ivig':
        title = "IVIG Resistance Prediction"
        values = shap_values['ivig']
    else:
        title = "Coronary Aneurysm Prediction"
        values = shap_values['aneurysm']
    
    st.markdown(f"##### Detailed Analysis for {title}")
    plot_shap_waterfall(
        values,
        f"Feature Impact on {title}",
        WATERFALL_PLOT_SIZE_SINGLE
    )
    
    _display_waterfall_explanation(title)

def _display_waterfall_explanation(condition: str):
    """Display explanation text for waterfall plots."""
    st.markdown(f"""
    #### Understanding the Waterfall Plot
    
    This plot shows how each feature affects the model's prediction:
    
    * 🔴 **Positive Impact (Red)**: Features that increase the likelihood of {condition}
    * 🔵 **Negative Impact (Blue)**: Features that decrease the likelihood of {condition}
    * 📏 **Bar Length**: Represents the strength of each feature's influence
    * 📊 **Base Value**: The starting point represents the model's average prediction
    * 🎯 **Final Prediction**: The end point shows the prediction for this specific case
    
    The features are ordered by their absolute impact, with the most influential features at the top.
    """) 