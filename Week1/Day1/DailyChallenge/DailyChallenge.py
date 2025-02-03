
#1 Using the input function, ask the user for a string. The string must be 10 characters long.
#2 Then, print the first and last characters of the given text.


user_input = input('Please write a 10 character string :\n')
if len(user_input) < 10 :
    print ('your string is not long enough')
elif len(user_input) > 10 :
    print('Your string is too long')   
else :
    print('Perfect String')
print(user_input[0])
print(user_input[9])


#3. Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:

for i in range(len(user_input)):
        print(user_input[:i+1])


#4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

import random

char_list = list(user_input)
random.shuffle(char_list) 
shuffled_string = ''.join(char_list)
print(f"Shuffled string: {shuffled_string}")