import requests
from secret import EMAIL, SECRET


def submit_answer(submit_url, quiz_url, answer):
    payload = {
        "email": EMAIL,
        "secret": SECRET,
        "url": quiz_url,
        "answer": answer
    }

    res = requests.post(submit_url, json=payload)

    return res.json()
