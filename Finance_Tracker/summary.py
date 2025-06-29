def transaction_sum(all_transactions):
    value_sum = 0
    value_list = []
    for item in all_transactions:
        value_list.append(item["value"])
    for items in value_list:
        value_sum = value_sum + items
    return value_sum
