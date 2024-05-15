from datetime import datetime
from class_person_main import Person

class Person:
    @classmethod
    def create_person(cls):
        first_name = input("Enter nae: ")
        last_name = input("Enter a last name (or press Enter if there is no last name): ")
        middle_name = input("Enter middle name (or press Enter if middle name is missing): ")
        birth_date = input("Enter date of birth (in dd.mm.yyyy format): ")
        while not cls.date_format(cls.check_date_format(birth_date)):
            print("Incorrect date. Please enter the date in the correct format.")
            birth_date = input("Enter date of birth (in dd.mm.yyyy format): ")
        death_date = input("Enter the date of death (or press Enter if there is no date of death): ")
        while death_date and not cls.date_format(cls.check_date_format(death_date)):
            print("Incorrect date. Please enter the date in the correct format or click Enter.")
            death_date = input("Enter the date of death (or press Enter if there is no date of death): ")
        gender = input("Enter gender (m/f): ").lower()
        while gender not in ['m', 'f']:
            print("Incorrect gender. Please enter: 'm' or 'f'.")
            gender = input("Enter gender (m/f): ").lower()

        return cls(first_name, last_name, middle_name, birth_date, death_date, gender)

Person.create_person()

p1 = Person('Tom', '10.04/1981', 'x', 'Junior', "SmidtJohn", '01/01,2030')
p2 = Person('MaryJohn', '10/04.1981', 'female')