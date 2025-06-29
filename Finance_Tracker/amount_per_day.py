

def create_amount_per_day(all_transactions):
    date = str(input("Введите дату в следующем формате '01.01.2001'\n"))
    transaction_list = []
    sum_value = 0
    for entry in all_transactions:
        if entry.get("date") == date:
            transaction_list.append(entry.get("value"))
    for item in transaction_list:
        sum_value = sum_value + item
    return sum_value

