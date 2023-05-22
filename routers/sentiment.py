from fastapi import APIRouter, status, Response, Depends
from pydantic import BaseModel

router = APIRouter(prefix="/v1/predictions", tags=["Predictions"])


class TweetRequest(BaseModel):
    """
    Tweet Data Transfer Object
    """
    text: str


@router.post("", status_code=status.HTTP_201_CREATED)
def predict_tweet_sentiment(tweet: TweetRequest,
                            response: Response):
    """
    Analyze the sentiment of the passed tweets
    :param tweet: Request Model
    :param response: Pydantic Res Model
    """
    pass
