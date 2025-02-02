#Exercise 1 : Hello World

print("Hello World \n" * 4)

#Exercise 2 : Some Math

print(99**3*8)

#Exercise 3 : What is the output ?

# 5 < 3 # False 
# 3 == 3 # True  
# 3 == "3" # False 
# "3" > 3 #TypeError or False 
# "Hello" == "hello" #False  

#Exercise 4 : Your computer brand

computer_brand = ('Custom Built')
print(('I have a ') + (computer_brand) + (' computer'))

# Exercise 5 : Your information

name = ('Pinjas')
age = ('37')
shoe_size = ('45')
info = f"My name is {name} with a spanish pronunciation \n, I am {age} years old and I have worked in 10 vastly different jobs since the age of 14 \n, and my shoe size is {shoe_size}."

# Exercise 6 : A & B

a = ('25')
b = ('10')

if a > b :
 print('Hello World')

#  Exercise 7 : Odd or Even

user_num_input = int(input("Chose a number any number: \n"))

if user_num_input % 2 == 0 :
    print(f"{user_num_input} is even")
else:
   print(f"{user_num_input} is odd")

#Exercise 8 : What’s your name ?

while True:

    user_name = input("what is your name? \n")

    if user_name == ('Pinjas'):
        input('yes thats my name but what is your name? \n')
    else:
        print('This is not for you') 
        break

#Exercise 9 : Tall enough to ride a roller coaster

user_height = int(input('How many centimeters tall are you? \n'))

if user_height >= 145 :
   print('You are tall enough to ride')

else :
   print('You must be 145cm to be able to ride')