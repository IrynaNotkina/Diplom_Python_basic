import datetime

class Person2:
    def __init__(self, first_name, birth_date, gender, last_name='', middle_name='', death_date=None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = birth_date
        self.death_date = death_date
        self.gender = gender

    def validate_date(self, date_str):
        formats = ['%d.%m.%Y', '%d-%m-%Y', '%d %m %Y', '%d,%m,%Y']
        for fmt in formats:
            try:
                datetime.datetime.strptime(date_str, fmt)
                return True
            except ValueError:
                pass
        return False

    def calculate_age(self):
        if self.birth_date:
            if self.death_date:
                death_date = datetime.datetime.strptime(self.death_date, '%d.%m.%Y')
            else:
                death_date = datetime.datetime.now()
            birth_date = datetime.datetime.strptime(self.birth_date, '%d.%m.%Y')
            age = death_date.year - birth_date.year - ((death_date.month, death_date.day) < (birth_date.month, birth_date.day))
            return age
        else:
            return None

    def __str__(self):
        output = f"{self.first_name}"
        if self.last_name:
            output += f" {self.last_name}"
        if self.middle_name:
            output += f" {self.middle_name}"
        if self.birth_date:
            output += f", {self.calculate_age()} років, {self.gender}. Народився {self.birth_date}."
            if self.death_date:
                output += f" Помер: {self.death_date}."
        return output

p1 = Person('Tom', '10.04/1981', 'male', 'Junior', "SmidtJohn", '01/01,2030')
p2 = Person('MaryJohn', '10/04.1981', 'female')

print(p1)
