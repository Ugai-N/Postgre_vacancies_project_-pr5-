from DB_creator import DBcreator


class DBManager(DBcreator):
    """Класс для работы с БД: сортировки, фильтрации и тд. Дочерний от DBcreator"""

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        with self.connection.cursor() as cursor:
            cursor.execute(
                           f"""SELECT {self.employers_table}.title, COUNT (*)
                           FROM {self.vacancies_table}
                           JOIN {self.employers_table} USING (employer_id)
                           GROUP BY {self.employers_table}.title;"""
                           )
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании,
        названия вакансии, зарплаты, региона и ссылки на вакансию"""
        with self.connection.cursor() as cursor:
            cursor.execute(
                           f"""SELECT {self.employers_table}.title as company_title, {self.vacancies_table}.title, 
                           {self.vacancies_table}.salary_avr_rub, {self.vacancies_table}.area, 
                           {self.vacancies_table}.url
                           FROM {self.vacancies_table}
                           JOIN {self.employers_table} USING (employer_id)
                           ORDER BY {self.vacancies_table}.salary_avr_rub DESC;"""
                           )
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        with self.connection.cursor() as cursor:
            cursor.execute(
                           f"""SELECT AVG(salary_avr_rub)
                           FROM {self.vacancies_table};"""
                           )
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        with self.connection.cursor() as cursor:
            cursor.execute(
                           f"""SELECT {self.employers_table}.title as company_title, {self.vacancies_table}.* 
                           FROM {self.vacancies_table}
                           JOIN {self.employers_table} USING (employer_id) 
                           WHERE salary_avr_rub > (SELECT AVG(salary_avr_rub) FROM {self.vacancies_table})
                           ORDER BY salary_avr_rub DESC;"""
                           )
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    def get_vacancies_with_keyword(self, key):
        """получает список всех вакансий, в названии которых содержатся переданные
        в метод слова, например “python” без учета регистра"""
        with self.connection.cursor() as cursor:
            cursor.execute(
                           f"""SELECT {self.employers_table}.title as company_title, {self.vacancies_table}.* 
                           FROM {self.vacancies_table}
                           JOIN {self.employers_table} USING (employer_id) 
                           WHERE lower({self.vacancies_table}.title) LIKE '%{key.lower()}%'
                           ORDER BY salary_avr_rub DESC;"""
                           )
            rows = cursor.fetchall()
            for row in rows:
                print(row)
