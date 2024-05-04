import json
import psycopg2

with psycopg2.connect(
        host='localhost',
        database='HH_Vacancies',
        user='postgres',
        password='Qwerty098'
) as conn:
    with conn.cursor() as cur:
        with open('vacancy_json.json', 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
            for vacancy in vacancies:
                cur.execute(
                    'INSERT INTO vacancy_table (company, job_title, link_to_vacancy, salary, description, '
                    'requirement) VALUES (%s, %s, %s, %s, %s, %s)',
                    (vacancy.get('company'), vacancy.get('job_title'), vacancy.get('link_to_vacancy'),
                     vacancy.get('salary'), vacancy.get('description'), vacancy.get('requirement')))

        cur.execute("SELECT * FROM vacancy_table")
        rows = cur.fetchall()
        for row in rows:
            print(row)
