import math
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
roots_math = list(map(math.sqrt, numbers))
print(squared, roots_math)
