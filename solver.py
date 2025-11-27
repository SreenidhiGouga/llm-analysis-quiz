from bs4 import BeautifulSoup


def extract_question(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator="\n")

    return text
