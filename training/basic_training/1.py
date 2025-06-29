x = list(map(int, (input("Введите числа, разделённые пробелом ").split())))
num_max = max(x)
num_min = min(x)
num_sr = sum(x) / len(x)
print(
    f"максимальное значение списка: {num_max}, минимальное значение списка: {num_min}, среднее арифметическое всех чисел: {num_sr}"
)
sorted_list = sorted(x)
print(sorted_list)

