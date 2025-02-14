class Account:
    balance: float
    account_id: int

    def __init__(self, balance: float, account_id: int):
        self.balance = balance
        self.account_id = account_id

    def details(self):
        return f"Balance: {self.balance}, Account ID: {self.account_id}"
