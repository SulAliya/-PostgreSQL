import psycopg2


class DBManager:
    def __init__(self, dbname, user, password, host):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """
        получает список всех компаний и количество вакансий у каждой компании.
        :return:
        """
        query = """
                SELECT company, COUNT(*)
                FROM vacancy_table 
                GROUP BY company
                """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_all_vacancies(self):
        """
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        """
        query = """
                SELECT company, job_title, salary_from, link_to_vacancy
                FROM vacancy_table
                """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_avg_salary(self):
        """
        получает среднюю зарплату по вакансиям.
        :return:
        """
        query = """
                SELECT AVG(salary_from)
                FROM vacancy_table
                """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_vacancies_with_higher_salary(self):
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        :return:
        """
        query = """
                SELECT job_title, salary_from
                FROM vacancy_table
                WHERE salary_from > (SELECT AVG(salary_from) FROM vacancy_table)
                """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """
        получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        :return:
        """
        query = """
                SELECT * FROM vacancy_table
                WHERE LOWER(job_title) LIKE %s
                """
        self.cur.execute(query, ('%' + keyword.lower() + '%',))
        return self.cur.fetchall()

    def close_connection(self):
        self.cur.close()
        self.conn.close()