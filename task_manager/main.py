from classes import DailyTask
from tasks import task_list


if __name__ == "__main__":
    upgrade = DailyTask("gaining knowledge")
    upgrade.add_task(task_list[0])
    upgrade.add_task(task_list[1])

    upgrade.show()

