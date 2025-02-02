#Exercise 1 : Use the terminal

# #PS B:\Learning\DI_Bootcamp\Week1\Day1\ExcerciseXP> $ python
# $ : The term '$' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path 
# was included, verify that the path is correct and try again.
# At line:1 char:1
# + $ python
# + ~
#     + CategoryInfo          : ObjectNotFound: ($:String) [], CommandNotFoundException
#     + FullyQualifiedErrorId : CommandNotFoundException


# PS B:\Learning\DI_Bootcamp\Week1\Day1\ExcerciseXP> python
# Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> ^Z


#Exercise 2 : Alias

# After a bit of reaserch I reinstalled python specifically 3.12.8 and now python runs when I use the py command 


# Exercise 3 : Outputs

#<= 3 < 9                           True 
# 3 == 3 == 3                       True   
#bool(0)                            False
#bool(5 == "5")                     False      
#bool(4 == 4) == bool("4" == "4")   True
#bool(bool(None))                   False


# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10

# print("x is", x)
# print("y is", y)
# print("a:", a)
# print("b:", b)                    
#                                   x is True
#                                   y is False
#                                   a: 5
#                                   b: 10


#Exercise 4 : How many characters in a sentence ?

#not sure why but I had to paste each individual line of the text body. STraight copy paste did not work and gives manye errors not sure if there is another way to paste see below and uncoment to view errors or lower for the way I found works

# #my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
#            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#            Ut enim ad minim veniam, quis nostrud exercitation ullamco 
#            laboris nisi ut aliquip ex ea commodo consequat. 
#            Duis aute irure dolor in reprehenderit in voluptate velit 
#            esse cillum dolore eu fugiat nulla pariatur. 
#            Excepteur sint occaecat cupidatat non proident, 
#            sunt in culpa qui officia deserunt mollit anim id est laborum.

my_text = '"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

print (len(my_text))


# Exercise 5: Longest word without a specific character

longest_sentence = ""

while True:
    user_input = input("Enter the longest sentence you can without using 'A':\n")

    if "A" in user_input.upper():  
        print("Oops! I see an 'A'. Try again.")
        continue  

    if len(user_input) > len(longest_sentence):
        longest_sentence = user_input
        print("Congratulations! New Record!")

    print(f"Current longest sentence: {longest_sentence}\n")
