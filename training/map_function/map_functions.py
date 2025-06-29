no_title_list = ["ya", "sanya", "juravl", "bomba"]
title_list = list(map(str.title, no_title_list))
print(title_list)

numbers = [1, 2, 3, 4, 5, 6, 7]
squared = list(map(lambda x: x ** 2, numbers)) #
print(squared)

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
multiplied = list(map(lambda a, b: a * b, list_1, list_2))
print(multiplied)


str_numbers = ["10", "20", "30"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)

def celsius_to_fahrenheit(c):
    return(c * 9/5) + 32
temperatures = [32, 11, 17, 25]
fahrenheit_temperatures = list(map(celsius_to_fahrenheit, temperatures))

print(fahrenheit_temperatures)

