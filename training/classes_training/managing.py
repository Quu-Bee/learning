from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

    @abstractmethod
    def update_status(self, new_status):
        pass


class RegularUser(User):
    def update_status(self, new_status):
        self.status = new_status


class AdminUser(User):
    def update_status(self, new_status):
        self.status = new_status

    def update_user_status(self, user, new_status):
        user.update_status(new_status)


admin1 = AdminUser("NotSanya", 48, "Active")
user2 = RegularUser("Oler", 52, "Active")
admin1.update_user_status(user2, "Inactive")
print(user2.status)
