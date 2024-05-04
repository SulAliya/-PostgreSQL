import csv
import psycopg2


with psycopg2.connect(
    host='Localhost',
    database='HH_Vacancies',
    user='postgres',
    password='Qwerty098'
) as conn:
    with conn.cursor() as cur:
        with open('vacancy_json.json', encoding="utf8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cur.execute('INSERT INTO vacancy_table VALUES (%s,%s,%s,%s,%s,%s)', (row.get('company'),
                                                                                  row.get('job_title'),
                                                                                  row.get('link_to_vacancy'),
                                                                                  row.get('salary'),
                                                                                  row.get('description'),
                                                                                  row.get('requirement')))
            cur.execute("SELECT * FROM vacancy_table")
            rows = cur.fetchall()
            for row in rows:
                print(row)