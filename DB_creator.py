import psycopg2

from utils import set_vacancies_list


class DBcreator:
    def __init__(self, password, database, vacancies_table, employers_table):
        self.connection = psycopg2.connect(host='localhost', database=database, user='postgres', password=password)
        self.vacancies_table = vacancies_table
        self.employers_table = employers_table

    def create_vacancies_table(self):
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    cursor.execute(f"""CREATE TABLE {self.vacancies_table} (
                                                                            vacancy_id serial PRIMARY KEY,
	                                                                        hh_vacancy_id int NOT NULL,
                                                                            title varchar NOT NULL,
	                                                                        area varchar NOT NULL,
	                                                                        employer_id int NOT NULL,
	                                                                        url varchar NOT NULL,
	                                                                        salary_min int,
	                                                                        salary_max int,
	                                                                        currency varchar,
	                                                                        salary_avr_rub int,
	                                                                        description varchar,
	                                                                        requirements varchar
                                                                            );"""
                                   )
        finally:
            pass
        #     self.connection.close()

    def create_employers_table(self):
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    cursor.execute(f"""CREATE TABLE {self.employers_table} (
                                                                            employer_id serial PRIMARY KEY,
                                                                            title varchar NOT NULL,
	                                                                        url varchar NOT NULL,
	                                                                        vacancies_url varchar NOT NULL,
	                                                                        trusted int NOT NULL,
	                                                                        CONSTRAINT chk_trusted CHECK (trusted IN (1, 0))
                                                                            );"""
                                   )
        finally:
            pass
        #     self.connection.close()

    def fill_in_vacancies(self, employers):
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    cursor.executemany(f"""INSERT into {self.vacancies_table} (
                                                                               hh_vacancy_id, 
                                                                               title, 
                                                                               area, 
                                                                               employer_id, 
                                                                               url, 
                                                                               salary_min, 
                                                                               salary_max, 
                                                                               currency, 
                                                                               salary_avr_rub, 
                                                                               description, 
                                                                               requirements
                                                                               ) 
                                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                                       set_vacancies_list(employers)
                                       )
                    cursor.execute(f'SELECT * from {self.vacancies_table}')
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)
        finally:
            self.connection.close()
