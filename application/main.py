from entity import Client
from entity import Account

c1 = Client(name="Raul", age=16, phone="(81)99754-8023")

print(c1.details())

account = Account(account_id=10, balance=1000.10)

print(account.details())