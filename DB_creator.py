import sqlite3

import psycopg2

from utils import set_vacancies_list


class DBcreator:
    """Класс для работы с БД: создание таблиц и заполнение их данными"""

    def __init__(self, password, database, vacancies_table, employers_table, employers):
        self.connection = psycopg2.connect(host='localhost', database=database, user='postgres', password=password)
        self.vacancies_table = vacancies_table
        self.employers_table = employers_table
        self.vacancies, self.employers = set_vacancies_list(employers)

    def create_vacancies_table(self) -> None:
        """Создает таблицу для работы с вакансиями"""
        with self.connection.cursor() as cursor:
            try:
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
                print(f'Таблица {self.vacancies_table} создана')
            except sqlite3.DatabaseError as error:
                print("Error: ", error)

    def create_employers_table(self) -> None:
        """Создает таблицу для работы с компаниями-работодателями"""
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(f"""CREATE TABLE {self.employers_table} (
                                                                        employer_id serial PRIMARY KEY,
                                                                        title varchar NOT NULL,
                                                                        url varchar NOT NULL,
                                                                        vacancies_url varchar NOT NULL,
                                                                        trusted int NOT NULL,
                                                                        CONSTRAINT chk_trusted CHECK (trusted IN (1, 0))
                                                                        );"""
                               )
                print(f'Таблица {self.employers_table} создана')
            except sqlite3.DatabaseError as error:
                print("Error: ", error)

    def fill_in_vacancies(self) -> None:
        """заполняет таблицу данными о вакансиях"""
        with self.connection.cursor() as cursor:
            try:
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
                                   self.vacancies
                                   )
                print(f'Таблица {self.vacancies_table} заполнена данными')
            except sqlite3.DatabaseError as error:
                print("Error: ", error)

    def fill_in_employers(self) -> None:
        """заполняет таблицу данными о компаниях-работодателях"""
        with self.connection.cursor() as cursor:
            try:
                cursor.executemany(f"""INSERT into {self.employers_table} (
                                                                           employer_id, 
                                                                           title, 
                                                                           url, 
                                                                           vacancies_url, 
                                                                           trusted
                                                                           ) 
                                   VALUES (%s, %s, %s, %s, %s)""",
                                   self.employers
                                   )
                print(f'Таблица {self.employers_table} заполнена данными')
            except sqlite3.DatabaseError as error:
                print("Error: ", error)
