class Account:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def get_info(self):
        return f"ID: {self.id}\nName: {self.name}\nBalance {self.__balance}"

    def deposit(self, amount_of_money):
        self.__balance += amount_of_money

    def withdraw_money(self, amount_of_money):
        if amount_of_money > self.__balance:
            raise ValueError(
                f"Недостаточно средств на счете!\n Сумма снятия: {amount_of_money}\n Баланс: {self.__balance} "
            )
        self.__balance -= amount_of_money


class AccountBase:
    def __init__(self):
        self.account_list = []

    def __str__(self):
        return f"AccountBase: {len(self.account_list)} пользователей"

    def add_user(self, user):
        if isinstance(user, Account) and user not in self.account_list:
            self.account_list.append(user)

    def delete_user(self, user):
        if isinstance(user, Account) and user in self.account_list:
            self.account_list.remove(user)

    def show_user_list(self):
        return "\n".join(user.get_info() for user in self.account_list)

    def find_user_with_id(self, id):
        for user in self.account_list:
            if user.id == id:
                return user.get_info()
        raise AttributeError("ID не найден")


if __name__ == "__main__":
    user1 = Account(1, "Sergey", 1000)
    user2 = Account(2, "Aglaea", 5)
    user3 = Account(112, "Sanya", 0)
    acc_base = AccountBase()
    acc_base.add_user(user1)
    acc_base.add_user(user2)
    acc_base.add_user(user3)
    print(acc_base)
    print(acc_base.show_user_list())
    acc_base.delete_user(user1)
    acc_base.show_user_list()
    print(acc_base.find_user_with_id(112))
