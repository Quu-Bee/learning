

def create_amount_per_category(all_transactions):
    category = str(input("Введите категорию:'\n"))
    transaction_list = []
    sum_value = 0
    for entry in all_transactions:
        if entry.get("category") == category:
            transaction_list.append(entry.get("value"))
    for item in transaction_list:
        sum_value = sum_value + item
    return sum_value
