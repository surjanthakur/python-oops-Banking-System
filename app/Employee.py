from Person import Person
from uuid import uuid4


class Employee(Person):

    def __init__(self):
        self.employee_id = str(uuid4())
        self.role: str
