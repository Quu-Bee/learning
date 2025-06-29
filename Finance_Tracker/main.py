from new_transaction import add_new_transaction
from interface import create_interface
from summary import transaction_sum
from amount_per_day import create_amount_per_day
from amount_per_a_certain_category import create_amount_per_category

all_transactions = []
value_list = []
value_sum = 0
options = {
    1: lambda: all_transactions.append(add_new_transaction()),
    2: lambda: print(all_transactions),
    3: lambda: print(transaction_sum(all_transactions)),
    4: lambda: print(create_amount_per_day(all_transactions)),
    5: lambda: print(create_amount_per_category(all_transactions)),
}

create_interface()
while (x := int(input())) != 6:
    if option := options.get(x):
        option()
    else:
        print("Введено некорректное значение, пожалуйста повторите")
    create_interface()

    # if x == 1:
    # all_transactions.append(add_new_transaction())
    #     pass
    # elif x == 2:#
    #     print(all_transactions)
    # elif x == 3:
    #     print(transaction_sum(all_transactions))
    # elif x == 4:
    #     print(create_amount_per_day(all_transactions))
    # elif x == 5:
    #     print(create_amount_per_category(all_transactions))
    # elif x == 6:
    #     exit()
    # else:
