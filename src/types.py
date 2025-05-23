from typing import TypedDict, Dict, List, Union

class FeatureField(TypedDict):
    """Type definition for a feature field."""
    title: str
    fields: Dict[str, str]

class PredictionResults(TypedDict):
    """Type definition for prediction results."""
    probabilities: Dict[str, float]
    shap_values: Dict[str, List[float]]

# Type aliases
Features = Dict[str, FeatureField]
InputData = Dict[str, float] 