from entity import Client

class Account:

    def __init__(self, balance: float, account_id: int, holder: Client):
        self.__balance = balance
        self.__account_id = account_id
        self.__holder = holder

    @property
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, holder: Client):
        self.__holder = holder

    @property
    def account_id(self):
        return self.__account_id

    def deposit(self, amount: float):
        self.__balance += amount

    def withdrawal(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
            print("Successful withdrawal!")
        else:
            raise ValueError("Invalid operation, insufficient balance!")

    def details_to_string(self):
        return f"Balance: {self.__balance}, Account ID: {self.__account_id}, Holder: {self.__holder}"

    def __str__(self):
        return self.details_to_string()
