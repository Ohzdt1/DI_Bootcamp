#For Loop

# for <variable (i)> in ,iterable/sequence>
    # indented block of code

#looping on a sequence (list)
# fruits = 'apple', 'banana', 'kiwi','pear'

# for each_fruit in fruits:
#     print(each_fruit)

#looping on a range of numbers 

#range (start, stop, step)
# for i in range(5):
#     print(i)
# for i in range(1,6):
#     print(i)
# for i in range(2,10,2):
#     print(i)

#enumerate

# fruits = 'apple', 'banana', 'kiwi','pear'

# for i, each_fruit in enumerate(fruits):
#     if each_fruit == fruits[3]:
#         print('this is the last one')
#     print (i, each_fruit)

# for i, each_fruit in enumerate(fruits):
#     if each_fruit == 'kiwi':
#         fruits[i] = 'lime'
#     else:
#         print(each_fruit)
# print(fruits)

# number = int(input('add your number to veiw its multiplication table\n'))

# for i in range(1,11):
#     print(number * i)

#While loop

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# fruits = ['apple', 'banana', 'kiwi','pear']

# i = 0
# while i <len(fruits):
#     print(fruits[i])
#     i += 1

# pizzas_order = []
# max_pizza = 5

# while len(pizzas_order) < max_pizza:
#     flavor = input('whichflavor?(if you finish type "done")\n')

#     if flavor == 'done':
#         print('Your Pizza is getting ready')
#         break

#     pizzas_order.append(flavor)

    # while True: always use break
pizzas_order = []

while True:
    flavor = input('which flavor would you like?(if you finish type "done")\n')
    
    if flavor == 'done':
        print(pizzas_order)
        print('Your Pizza is getting ready')
        break

    pizzas_order.append(flavor)