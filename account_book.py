import datetime
import json
import pathlib


class Transaction:

    def __init__(self, op, amount, category, description, time=None):

        if op not in ['income', 'expense']:
            raise ValueError(f'Invalid transaction op: {op}')

        self.op = op    # 'income' or 'expense'
        self.amount = amount
        self.category = category
        self.description = description
        if not time:
            self.time = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
        else:
            self.time = time

    def __str__(self):
        return (
            f"{self.op.capitalize()} - ￥{self.amount} - {self.category} - "
            f"{self.description} on {self.time}"
        )

    def to_dict(self):
        return {
            'op': self.op,
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'time': self.time
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            op=data['op'],
            amount=data['amount'],
            category=data['category'],
            description=data['description'],
            time=data['time']
        )


class AccountBook:

    def __init__(self):
        self.balance = 0
        self.transactions = []
        self.save_file = pathlib.Path(__file__).resolve().parent / 'data.json'

    def display_balance(self):
        print(f"Balance: {self.balance}")

    def calculate_balance(self):
        balance = 0
        for transaction in self.transactions:
            if transaction.op == 'income':
                balance += float(transaction.amount)
            elif transaction.op == 'expense':
                balance -= float(transaction.amount)
            else:
                raise ValueError(f'Invalid transaction op: {transaction.op}')
        self.balance = balance
        print(f"Balance calculate success! Balance: {self.balance}")

    def update_balance(self, transaction):
        if transaction.op == 'income':
            self.balance += float(transaction.amount)
        elif transaction.op == 'expense':
            self.balance -= float(transaction.amount)
        else:
            raise ValueError(f'Invalid transaction op: {transaction.op}')
        # print(f'Balance update success! Balance: {self.balance}')

    def add_transactions(self, transaction):
        self.transactions.append(transaction)
        self.update_balance(transaction)
        print(f"Transaction add success! Balance: {self.balance}")

    def display_book(self):
        if len(self.transactions) == 0:
            print("No transactions found!")
        else:
            print(f'Balance: ￥{self.balance}')
            for index, transaction in enumerate(self.transactions, start=1):
                print(f'{index}. {str(transaction)}')
        print('Display finish!')

    def save_json(self):
        with self.save_file.open(mode='w') as f:
            data = [transaction.to_dict() for transaction in self.transactions]
            json.dump(data, f, indent=4)
