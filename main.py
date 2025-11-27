from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

from secret import SECRET, EMAIL
from scraper import get_page_content
from solver import extract_question
from submitter import submit_answer


app = FastAPI()


class QuizRequest(BaseModel):
    email: str
    secret: str
    url: str


@app.post("/solve")
def solve_quiz(data: QuizRequest):

    # Step 1: Check secret
    if data.secret != SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    # Step 2: Get quiz page content
    html = get_page_content(data.url)

    # Step 3: Extract question text
    question = extract_question(html)

    print("\n--- QUESTION FOUND ---\n")
    print(question)

    # 🔴 TEMPORARY DUMMY ANSWER
    answer = 0

    # You can manually update logic after seeing question

    return {
        "status": "received",
        "question_sample": question[:500],
        "answer_used": answer
    }
