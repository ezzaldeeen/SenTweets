from pydantic import BaseModel


class AnalyticRequest(BaseModel):
    """
    Analytic Intermediate Data Object
    """
    text: str  # the content of the tweet
