import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number = 3728

for num, x in list_of_numbers:
    print (target_number == num + x )