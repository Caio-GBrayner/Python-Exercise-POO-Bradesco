class Client:

    def __init__(self, name: str, age: int, phone: str):
        self.__name = name
        self.__age = age
        self.phone = phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("The age cannot be less than 0")
        else:
            self.__age = age

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not phone.isdigit():
            raise ValueError("The telephone number must contain only digits")
        if len(phone) != 11:
            raise ValueError("The telephone number must contain only ten digits")
        else:
            self.__phone = self.format_phone(phone)

    @staticmethod
    def format_phone(phone: str) -> str:
        return f"({phone[:2]}){phone[2:6]}-{phone[6:]}"

    def details(self):
        return f"Name: {self.__name}, Age: {self.__age}, Phone: {self.__phone}"

    def __str__(self):
        return self.details()
