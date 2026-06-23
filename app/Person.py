class Person:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone

    def display_profile(self):
        return f"""
        name: {self.name}
        email: {self.email}
        phone no: {self.phone}
    """
