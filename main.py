from fastapi import FastAPI
from routers.sentiment import analysis

app = FastAPI(title="Sentiment Analyzer")

app.include_router(router=analysis.router)
