import string

from faker import Faker
import random

faker = Faker()

class DataForRegistrationUser:
    def __init__(self):
        self._email = self.set_email()
        self._password = self.set_password()
        self._name = self.set_name()

    @property
    def email(self):
        return self._email


    def set_email(self):
        identifier = '_'
        identifier+=faker.first_name()
        identifier+='_'
        identifier+=faker.last_name()
        domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'icloud.com', 'ymail.com'])


        return identifier + '@' + domain

    @property
    def password(self):
        return self._password



    def set_password(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(10))


    @property
    def name(self):
        return self._name


    def set_name(self):
        return faker.first_name()








