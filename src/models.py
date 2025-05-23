import joblib
import pandas as pd
from .config import MODEL_PATH, EXPLAINER_IVIG_PATH, EXPLAINER_ANEURYSM_PATH

class KDPredictor:
    def __init__(self):
        self.model = None
        self.explainer_ivig = None
        self.explainer_aneurysm = None
        self._load_models()

    def _load_models(self):
        """Load all required models and explainers."""
        try:
            self.model = joblib.load(MODEL_PATH)
            self.explainer_ivig = joblib.load(EXPLAINER_IVIG_PATH)
            self.explainer_aneurysm = joblib.load(EXPLAINER_ANEURYSM_PATH)
        except Exception as e:
            raise Exception(f"Error loading models: {str(e)}")

    def predict(self, input_data: dict) -> tuple:
        """
        Make predictions for IVIG resistance and Coronary Aneurysm.
        
        Args:
            input_data (dict): Dictionary containing input features
            
        Returns:
            tuple: (predictions, shap_values_ivig, shap_values_aneurysm)
        """
        try:
            # Create DataFrame from input
            X_input = pd.DataFrame([input_data])
            
            # Get predictions
            y_pred_proba = self.model.predict_proba(X_input)
            
            # Calculate SHAP values
            shap_values_ivig = self.explainer_ivig(X_input)
            shap_values_aneurysm = self.explainer_aneurysm(X_input)
            
            # Extract probabilities for positive class
            ivig_prob = y_pred_proba[0][0][1]
            aneurysm_prob = y_pred_proba[1][0][1]
            
            # Get SHAP values for positive class
            shap_values_ivig_class1 = shap_values_ivig[:, :, 1][0]
            shap_values_aneurysm_class1 = shap_values_aneurysm[:, :, 1][0]
            
            return {
                'probabilities': {
                    'ivig': ivig_prob,
                    'aneurysm': aneurysm_prob
                },
                'shap_values': {
                    'ivig': shap_values_ivig_class1,
                    'aneurysm': shap_values_aneurysm_class1
                }
            }
        except Exception as e:
            raise Exception(f"Error making predictions: {str(e)}") 