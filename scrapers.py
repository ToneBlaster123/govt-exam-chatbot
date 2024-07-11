import requests
from bs4 import BeautifulSoup

def get_exam_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    exam_name = soup.find('h1', class_='exam-title').text
    exam_date = soup.find('span', class_='exam-date').text

    return {'exam_name': exam_name, 'exam_date': exam_date}
