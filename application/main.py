from entity import Client
from entity import Account

class Main:
    @staticmethod
    def main():
        name = input("Enter your name: ")
        phone = input("Enter your phone (10 digits): ")
        age = int(input("Enter your age: "))

        client = Client(name=name, age=age, phone=phone)
        print(client.details())

        account_id = int(input("Enter your account ID: "))
        balance = float(input("Enter your initial balance: "))

        account = Account(account_id=account_id, balance=balance, holder=client)
        print(account.details_to_string())


if __name__ == "__main__":
    Main.main()
