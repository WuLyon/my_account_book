import pathlib
import account_book
import json

file_path = pathlib.Path(__file__).resolve().parent / 'data.json'
with file_path.open(mode='r') as f:
    data = json.load(f)
    transactions = [account_book.Transaction.from_dict(item) for item in data]
    # print(data)
    print(transactions[0])
