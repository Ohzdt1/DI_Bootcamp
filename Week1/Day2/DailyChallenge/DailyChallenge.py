#Challenge 1

# def multiples_list():
#     number = int(input("Enter a number: "))
#     length = int(input("Enter the length of the list: "))

#     multiples = [number * i for i in range(1, length + 1)]
    
#     print("List of multiples:", multiples)

# multiples_list()


number = int(input('Choose a number any number \n'))
length = int(input('Choose a length any Length \n'))

multiples = [number * i for i in range(1, length + 1)]
    
print("List of multiples:", multiples)



# Challenge 2

def remove_consecutive_duplicates(s):
    result = []
    prev_char = None 

    for char in s:
        if char != prev_char:  
            result.append(char)  
        prev_char = char  
    
    return "".join(result)  

word = input("Enter a word: ")
new_string = remove_consecutive_duplicates(word)
print("Word without consecutive duplicates:", new_string)
