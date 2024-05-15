from datetime import datetime


class Person:
    PEOPLE_BASE = []
    PEOPLE_AMOUNT = 0

    def __init__(self, first_name, birth_date, gender, last_name='', middle_name='', death_date=None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = birth_date
        self.death_date = death_date
        self.gender = gender

    def __str__(self):
        error = '*** available genders: m/male or f/female only ***'
        he_she = "he" if self.gender in ['m', 'male'] else "she" if self.gender in ['f', 'female'] else ''
        men_women = "men" if self.gender in ['m', 'male'] else "women" if self.gender in ['f', 'female'] else error
        age = self.calc_age()
        age_rate = 'year' if int(age) < 2 else 'years'
        output = f"{self.first_name}"
        birth_date_formatted = self.date_format(self.check_date_format(self.birth_date))
        death_date_formatted = self.date_format(self.check_date_format(self.death_date)) if self.death_date else None
        if self.last_name:
            output += f" {self.last_name}"
        if self.middle_name:
            output += f" {self.middle_name}"
        if self.birth_date:
            output += f' {self.calc_age()} {age_rate} old, {men_women}, {he_she} was born in {birth_date_formatted}'
            if self.death_date:
                output += f',  {he_she} died in {death_date_formatted}'
        return output

    @staticmethod
    def check_date_format(date_format):
        delimiters = ['.', '/', ' ', ',']
        for delimiter in delimiters:
            date_format = date_format.replace(delimiter, '.')
        return date_format

    @staticmethod
    def date_format(date_format):
        try:
            day, month, year = map(int, date_format.split('.'))
            return datetime(year, month, day).date()
        except Exception as e:
            return f"Error: {e}"

    def calc_age(self):
        birth_date = self.check_date_format(self.birth_date)
        death_date = self.check_date_format(self.death_date) if self.death_date else None
        birth_date = self.date_format(birth_date)
        death_date = self.date_format(death_date) if death_date else None
        if death_date:
            if (death_date.month, death_date.day) < (birth_date.month, birth_date.day):
                return death_date.year - birth_date.year - 1
            else:
                return death_date.year - birth_date.year
        else:
            today = datetime.now().date()
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                return today.year - birth_date.year - 1
            else:
                return today.year - birth_date.year

    @classmethod
    def create_person(cls):
        first_name = input("Введіть ім'я: ")
        last_name = input("Введіть прізвище (або натисніть Enter, якщо прізвище відсутнє): ")
        middle_name = input("Введіть по-батькові (або натисніть Enter, якщо по-батькові відсутнє): ")
        birth_date = input("Введіть дату народження (у форматі дд.мм.рррр): ")
        while not cls.date_format(cls.check_date_format(birth_date)):
            print("Некоректна дата. Будь ласка, введіть дату у коректному форматі.")
            birth_date = input("Введіть дату народження (у форматі дд.мм.рррр): ")
        death_date = input("Введіть дату смерті (або натисніть Enter, якщо дата смерті відсутня): ")
        while death_date and not cls.date_format(cls.check_date_format(death_date)):
            print("Некоректна дата. Будь ласка, введіть дату у коректному форматі або натисніть Enter.")
            death_date = input("Введіть дату смерті (або натисніть Enter, якщо дата смерті відсутня): ")
        gender = input("Введіть стать (m/f): ").lower()
        while gender not in ['m', 'f']:
            print("Некоректна стать. Будь ласка, введіть 'm' або 'f'.")
            gender = input("Введіть стать (m/f): ").lower()

        return cls(first_name, last_name, middle_name, birth_date, death_date, gender)


p1 = Person('Tom', '10.04/1981', 'x', 'Junior', "SmidtJohn", '01/01,2030')
p2 = Person('MaryJohn', '10/04.1981', 'female')

print(p1)
print(p2)

