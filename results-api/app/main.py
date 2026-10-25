
import os
from typing import Literal

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, text

app = FastAPI(title="QuickBallot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://localhost:8080",
        "http://127.0.0.1:8080",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is required")

engine = create_engine(DATABASE_URL)


class VoteRequest(BaseModel):
    option: Literal["AWS", "Docker", "Kubernetes"]


@app.get("/")
def root():
    return {"message": "QuickBallot Results API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/vote", status_code=201)
def cast_vote(vote: VoteRequest):
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO votes (option) VALUES (:option)"),
            {"option": vote.option},
        )

    return {
        "message": "Vote recorded successfully",
        "option": vote.option,
    }


@app.get("/results")
def results():
    with engine.connect() as conn:
        rows = conn.execute(
            text("""
                SELECT option, COUNT(*) AS votes
                FROM votes
                GROUP BY option
                ORDER BY option
            """)
        )
        return {row.option: row.votes for row in rows}
