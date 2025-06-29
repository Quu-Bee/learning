list_1 = [1, 2, 3, 0]
list_2 = [4, 5, 7, 9]

summed = list(map(lambda x, y: x + y, list_1, list_2))
print(summed)

first_name = ["Sanya", "Daniil", "Bim_Bim"]
second_name = ["Juravl", "Bolotov", "Bom_Bom"]
full_name = list(map(lambda x, y: x + " " + y, first_name, second_name))
print(full_name)
