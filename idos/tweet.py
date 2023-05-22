import uuid

from pydantic import BaseModel, Field


class TweetIDO(BaseModel):
    """
    Tweet Intermediate Data Object
    """
    id: str = Field(default_factory=lambda: uuid.uuid4().hex)
    text: str  # the content of the tweet
