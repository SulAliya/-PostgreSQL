import json

import requests


def load_vacancies():
    companies = [
        "АО Уфанет",
        "Яндекс",
        "Тинькофф",
        "Тензор",
        "Контур",
        "ASTON",
        "Сбер"
        "Альфа-Банк"
        "VK",
        "ТрансТехСервис"
    ]
    vacancies = []

    for company in companies:
        url = "https://api.hh.ru/vacancies"
        params = {'text': company, 'per_page': 10}
        data = requests.get(url, params=params)

        if data.status_code == 200:
            json_data = data.json()
            for item in json_data['items']:
                job_title = item['name']
                link_to_vacancy = item['alternate_url']
                salary = item['salary']
                if salary:
                    salary_from = salary.get('from', 'Зарплата не указана')
                    salary_to = salary.get('to', 'не указано')
                    currency = salary.get('currency')
                else:
                    salary_from = 'Зарплата не указана'
                    salary_to = ''
                    currency = ''
                description = item['snippet']['responsibility']
                requirement = item['snippet']['requirement']

                vacancies.append({
                    "company": company,
                    "job_title": job_title,
                    "link_to_vacancy": link_to_vacancy,
                    "salary": [f'От {salary_from}, до {salary_to} {currency}'],
                    "description": description,
                    "requirement": requirement
                })
        else:
            print(f"Ошибка {data.status_code}")
    return vacancies


if __name__ == "__main__":
    vacancies = load_vacancies()
    for vacancy in vacancies:
        print(vacancy)
        filename = 'vacancy_json.json'
        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(vacancies, outfile, ensure_ascii=False, indent=4)



