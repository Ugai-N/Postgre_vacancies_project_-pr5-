from DB_creator import DBcreator


class DBManager(DBcreator):

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        # SELECT employer_id, COUNT (*)
        # from vacancies_nov
        # GROUP BY employer_id
        pass

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""
        # SELECT employer_id, title, salary_avr_rub, url
        # FROM vacancies_nov
        # ORDER BY salary_avr_rub DESC
        pass

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        # SELECT AVG(salary_avr_rub)
        # FROM vacancies_nov
        pass

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        # SELECT * FROM vacancies_nov
        # WHERE salary_avr_rub > (SELECT AVG(salary_avr_rub) FROM vacancies_nov)
        # ORDER BY salary_avr_rub DESC
        pass

    def get_vacancies_with_keyword(self, query):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”"""
        # SELECT * FROM vacancies_nov
        # WHERE title LIKE '%Python%'
        # ORDER BY salary_avr_rub DESC
        # РЕГИСТР!!
        pass
