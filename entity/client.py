class Client:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def details(self):
        return f"Name: {self.name}, Age: {self.age}, Phone: {self.phone}"
