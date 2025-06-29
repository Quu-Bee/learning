
def add_new_transaction():   
    transaction = {}
    date = str(input("Enter the transaction date \n"))
    transaction.update({"date": date})
    value = int(input("Enter the transaction value \n"))
    transaction.update({"value": value})
    category = str(input("Enter the transaction category \n"))
    transaction.update({"category": category})
    return transaction

