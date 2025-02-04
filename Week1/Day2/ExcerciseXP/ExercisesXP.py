# #🌟 Exercise 1 : Favorite Numbers

# my_fav_numbers = {27,18,10,28,3}
# print(my_fav_numbers)

# my_fav_numbers.add(2)
# my_fav_numbers.add(11)
# print(my_fav_numbers)

# my_fav_numbers.pop()
# print(my_fav_numbers)

# friend_fav_numbers = {25,88,46,5,69}

# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# print(our_fav_numbers)


# #🌟 Exercise 2: Tuple

# #Because a Tuble is immutable you cannot add but we could Concatenate

# #🌟 Exercise 3: List

# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# print(basket)

# basket.remove('Banana')
# print(basket)

# basket.remove('Blueberries')
# print(basket)

# basket.append('Kiwi')
# print(basket)

# basket.insert(0, "Apples")
# print(basket)

# apple_count = basket.count("Apples")
# print(basket)

# basket.clear()

# print("Final basket:", basket)


# #🌟 Exercise 4: Floats

# #The difference between an integer and a float also explains what a float is.
# #the difference betrween these two data types is that am integer will only have whole numbers and a float will also include decimal numbers.

# mixed_list = []
# for i in range(1, 10):
#     mixed_list.append(i * 0.5)  
#     mixed_list.append(i)        

# print(mixed_list) 

# intigers = (list[1,2,3,4,5])
# floats = (list[1.2,2.3,3.4,4.5,5.6])



# float_list = [x * 0.5 for x in range(3, 11)]
# print(float_list)


# #🌟 Exercise 5: For Loop

# for number in range(1, 21):
#     print(number)

# for number in range(1, 21, 2):
#     print(number)


# #🌟 Exercise 6 : While Loop


# while True:
#     user_name =input('whats your name?\n')
#     if user_name == 'Pinjas':
#           print('Access Granted')
#           break
#     else:
#        print('You Shall Not Pass!')


#🌟 Exercise 7: Favorite fruits

favorite_fruits = input("Enter your favorite fruits (separate them with spaces): ")

chosen_fruit = input("Enter the name of a fruit: ")

if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy!")


# #Exercise 8: Who ordered a pizza ?

# toppings = []

# while True:
#     topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    
#     if topping.lower() == 'quit':
#         break
    
#     toppings.append(topping)
#     print(f"Adding {topping} to your pizza!")

# total_price = 10 + (2.5 * len(toppings))

# print("\nYour pizza includes the following toppings:")
# for topping in toppings:
#     print(f"- {topping}")

# print(f"Total price: ${total_price:.2f}")


# #Exercise 9: Cinemax
# #part1 
# total_cost = 0

# num_people = int(input("How many tickets will it be? "))

# for i in range(num_people):
#     age = int(input(f"Enter the age of person {i + 1}: "))
    
#     if age < 3:
#         price = 0  # Free ticket
#     elif 3 <= age <= 12:
#         price = 10
#     else:
#         price = 15

#     total_cost += price  # Add to total cost

# print(f"\nTotal cost for the family: ${total_cost}")

# #part 2

# teenagers = ["Harry", "Bilbo", "Eragon", "Kvoth", "Durzo"]

# allowed_viewers = []

# for name in teenagers:
#     age = int(input(f"Enter {name}'s age: "))
    
#     if 16 <= age <= 21:
#         print(f"Sorry, {name}, you are not allowed to watch this movie.")
#     else:
#         allowed_viewers.append(name) 


# print("\nFinal list of viewers:")
# print(allowed_viewers)

# #Exercise 10 : Sandwich Orders

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# while "Pastrami sandwich" in sandwich_orders:
#     sandwich_orders.remove("Pastrami sandwich")

# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop(0)
#     print(f"I made your {current_sandwich.lower()}")
#     finished_sandwiches.append(current_sandwich)

