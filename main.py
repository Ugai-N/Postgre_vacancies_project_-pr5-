import os

from DB_creator import DBcreator

employers = [
             1212374, 847383, 1740, 2661787, 9804951, 598471, 8966021, 851604, 78638, 1818108,
             4574784, 9056925, 56119, 2498826, 4080, 5269493, 5473303, 113953
            ]
sql_database = '555'
sql_password = os.getenv('POSTGRES_PASSWORD')
sql_vacancies_table = 'vacancies_NOV'
sql_employers_table = 'employers_NOV'

# создали таблицы
HH_database = DBcreator(sql_password, sql_database, sql_vacancies_table, sql_employers_table)
HH_database.create_vacancies_table()
HH_database.create_employers_table()

#заполнили таблицу с вакансиями
HH_database.fill_in_vacancies(employers)
