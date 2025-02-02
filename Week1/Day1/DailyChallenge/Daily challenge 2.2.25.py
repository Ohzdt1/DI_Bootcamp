import random

user_input = input('Please write a 10 character string :\n')
if len(user_input) < 10 :
    print ('your string is not long enough')
elif len(user_input) > 10 :
    print('Your string is too long')   
else :
    print('Perfect String')
print(user_input[0])
print(user_input[9])


for i in range(len(user_input)):
        print(user_input[:i+1])


char_list = list(user_input)
random.shuffle(char_list) 
shuffled_string = ''.join(char_list)
print(f"Shuffled string: {shuffled_string}")