# Feature definitions
FEATURES = {
    'blood_test': {
        'title': 'Blood Test',
        'fields': {
            'Lympho_before': 'Lymphocyte (%)',
            'PLT_before': 'Platelet count(10^3/ml)',
            'Chol_before': 'Cholesterol(mg/dL)',
            'CRP_before': 'CRP(mg/dL)',
            'Seg_before': 'Neutrophil (%)',
            'TB_before': 'Total bilirubin(mg/dL)',
            'P_before': 'Phosphorus(mg/dL)',
            'ANC_before': 'Absolute Neutrophil count(10^9/L)'
        }
    },
    'echo': {
        'title': 'Echocardiography',
        'fields': {
            'initial_echo_RCA_Z': 'RCA z score',
            'initial_echo_LMCA_Z': 'LMCA z score',
            'initial_echo_LAD_Z': 'LAD z score'
        }
    },
    'clinical': {
        'title': 'Clinical Symptom',
        'fields': {
            'fever_duration': 'Fever duration (days)'
        }
    }
}

# Model file paths
MODEL_PATH = "models/multi_model.pkl"
EXPLAINER_IVIG_PATH = "models/explainer_ivig.pkl"
EXPLAINER_ANEURYSM_PATH = "models/explainer_aneurysm.pkl"

# Plot configurations
WATERFALL_PLOT_SIZE_SINGLE = (12, 8)
WATERFALL_PLOT_SIZE_COMBINED = (8, 6)
PLOT_PADDING = 20 