from account_book import Transaction
from account_book import AccountBook


class APP:

    def __init__(self):
        self.book = AccountBook()

    def run(self):
        print('Welcome to AccountBook APP:')
        while True:
            user_input = input(
                "-------------------------\n"
                "1. Display all the book\n"
                "2. Income amount\n"
                "3. Expense amount\n"
                "4. Display the Balance\n"
                "5. Quit\n"
                "-------------------------\n"
            )

            try:
                user_input = int(user_input)
            except ValueError:
                print("Please input a valid number")

            if user_input not in range(1, 6):
                print("Please input the number 1~5")
                continue

            if user_input == 1:
                self.book.display_book()

            elif user_input == 2:
                trans = Transaction(
                    'income',
                    amount=input("amount: "),
                    category=input("category: "),
                    description=input("description: ")
                )
                self.book.add_transactions(trans)

            elif user_input == 3:
                trans = Transaction(
                    'expense',
                    amount=input("amount: "),
                    category=input("category: "),
                    description=input("description: ")
                )
                self.book.add_transactions(trans)

            elif user_input == 4:
                self.book.display_balance()

            elif user_input == 5:
                break
        self.book.save_json()
        print('Have a nice day!')
