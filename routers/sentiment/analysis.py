from fastapi import APIRouter, status, Response

from routers.sentiment.request import AnalyticRequest
from routers.sentiment.response import AnalyticResponse
from libs.predictions import predict

router = APIRouter(prefix="/v1/analytics", tags=["Analytics"])


@router.post("",
             status_code=status.HTTP_201_CREATED)
def predict_tweet_sentiment(payloads: list[AnalyticRequest],
                            response: Response) -> list[AnalyticResponse]:
    """
    Analyze the sentiment of the passed tweets
    :param payloads: Request Model
    :param response: Pydantic Res Model
    """
    inputs = [payload.text for payload in payloads]
    outputs = predict(inputs)
    resp = [AnalyticResponse(**output) for output in outputs]
    return resp
