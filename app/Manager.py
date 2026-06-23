from Employee import Employee


class Manager(Employee):
    def __init__(self, branch_name: str):
        self.branch_name = branch_name

    def create_employee(self):
        pass

    def remove_employee(self):
        pass
