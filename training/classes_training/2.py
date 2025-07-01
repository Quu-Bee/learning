import time


def count_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"функция {func.__name__}, была выполнена за {end_time - start_time}")

    return inner


@count_time
def sum1(x, y):
    time.sleep(3)
    return x + y


@count_time
def sum2(x, y, z):
    time.sleep(5)
    return x + y + z


sum1(5, 10)
sum2(10, 15, 20)
