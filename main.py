import requests
import os
from dotenv import load_dotenv


MONTHS = [
    'января',
    'февраля',
    'марта',
    'апреля',
    'мая',
    'июня',
    'июля',
    'августа',
    'сентября',
    'октября',
    'ноября',
    'декабря',
]

def main():
    load_dotenv()
    api_key = os.getenv('API_KEY') 

    url = 'https://calendarific.com/api/v2/holidays'
    params = {
    'api_key': api_key,
    'country':'RU', 
    'year': 2025,}
    response = requests.get(url, params=params)
    response.raise_for_status()
    holidays = response.json()['response']['holidays']

    for holiday in holidays:
        month = holiday['date']['datetime']['month']
        print(f'''Дата: {holiday['date']['datetime']['day']} {MONTHS[month-1]}
Название праздника: {holiday['name']}
Описание: {holiday['description']}
''')


if __name__ == '__main__':
    main()