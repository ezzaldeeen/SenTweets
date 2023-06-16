from pydantic import BaseModel
from enum import Enum


class SentimentEnum(str, Enum):
    POSITIVE = "POSITIVE"
    NEUTRAL = "NEUTRAL"
    NEGATIVE = "NEGATIVE"


class AnalyticResponse(BaseModel):
    """
    Analytic Intermediate Data Object
    """
    text: str  # the content of the tweet
    sentiment: str
    confidence: float
