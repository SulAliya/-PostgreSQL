# создание таблицы в БД PostgreSQL

CREATE TABLE vacancy_table
(
    company_id int PRIMARY KEY,
    vacancy_id int NOT NULL,
    job_title varchar(100),
    link_to_vacancy text,
    salary text,
    description text,
    requirement text
)