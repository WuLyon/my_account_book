from account_book import Transaction
from account_book import AccountBook
from app import APP


def test():
    transaction1 = Transaction('income', 100, 'salary', 'work')
    # transaction2 = Transaction('expense', 50, 'food', 'launch')
    dict1 = transaction1.to_dict()
    print(dict1)
    trans1 = Transaction.from_dict(dict1)
    print(trans1)


if __name__ == "__main__":
    app = APP()
    app.run()
