# Model Files

This directory contains the trained models and SHAP explainers required for the Kawasaki Disease prediction application.

## Files

- `multi_model.pkl`: Main prediction model for both IVIG resistance and Coronary Aneurysm
- `explainer_ivig.pkl`: SHAP explainer for IVIG resistance predictions
- `explainer_aneurysm.pkl`: SHAP explainer for Coronary Aneurysm predictions

## Version Information

Current model version: 1.0.0

### Training Details
- Training data cutoff date: [DATE]
- Model architecture: Multi-task classification
- Framework: scikit-learn

### Performance Metrics
- IVIG Resistance AUC: [SCORE]
- Coronary Aneurysm AUC: [SCORE]

## Usage

These model files are automatically loaded by the application through the `KDPredictor` class in `src/models.py`. Do not modify or delete these files as they are essential for the application to function. 