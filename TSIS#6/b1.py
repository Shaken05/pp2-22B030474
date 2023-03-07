import math

input_string = input()
my_list = [int(x) for x in input_string.split()]
result = math.prod(my_list)
print(result)
