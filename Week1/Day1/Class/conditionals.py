# # my_city = 'Beit Shemesh'

# # if my_city == 'Beit Shemesh' :
    
# #     print(f'I like {my_city}')

# # print('Finish')

# # my_city = 'Tel Aviv'

# # if my_city == 'Beit Shemesh' :
    
# #     print(f'I like {my_city}')
    

# # print('Finish')

# # #Syntax of if statement 
# # #if (keyword) + (condition) + :
# #         #indentation  + block of code 

# #exercise 
# #take the name of the user using an imput ()
# #check the name is the same as yours 
# #if so, print "we have teh same name"


# user_name = input ('whats your name?')

# if user_name == "Pinjas":
#     print("We have the same name")
# elif user_name == "Daniel" :
#     print('You have a beautiful name')
# else: 
#     print("we have different names")

guess_number = int(input('Guess a number from 1 to 100:\n')) 

if guess_number % 3 == 0 and guess_number % 5 ==0 :
    print("FizzBuzz") 
elif guess_number % 3 == 0 :
    print("Fizz")
elif guess_number % 5 == 0 :
    print("Buzz")
 


