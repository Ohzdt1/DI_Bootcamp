#Challenge 1 : Sorting
word_list = []

def user_words():
    global word_list
    word_input = input("Provide a list of words separated by a comma:\n")
    word_list = [word.strip() for word in word_input.split(',')]
    word_list.sort()
    print(', '.join(word_list))
    print(', \n'.join(word_list))
    
user_words()

# Challenge 2 : Longest Word

def longest_word():
    sentence = input("Type your sentence:\n")
    words = sentence.split()
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word
    print(longest)

longest_word()



