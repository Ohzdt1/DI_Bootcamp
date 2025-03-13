import random
import csv

def get_words_from_file(filename):
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                words.extend(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Make sure it is in the correct directory.")
        exit()
    return words

def get_random_sentence(length, words):
    return " ".join(random.choices(words, k=length)).lower()

def main():
    print("Welcome to the Random word Generator!")
    print("This program generates random words in a sentence with the length of your choice.")
    
    filename = r"B:\Learning\DI_Bootcamp\Week2\Day4\ExercisesXP\word_list.csv"
    words = get_words_from_file(filename)
    
    while True:
        try:
            length = int(input("Enter how long you would like the sentence to be (between 2 and 1000): "))
            if 2 <= length <=1000:
                break
            else:
                print("Error: Please enter a number between 2 and 1000.")
            raise ValueError("Invalid number of words. Please enter a number between 2 and 1000.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")

    
    sentence = get_random_sentence(length, words)
    print("\nGenerated Sentence:")
    print(sentence)
if __name__ == "__main__":
    main()  


#🌟 Exercise 2: Working with JSON

import json

# Given JSON string
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

salary = data["company"]["employee"]["payable"]["salary"]
print(f"Salary: {salary}")

data["company"]["employee"]["birth_date"] = "21-01-1988"

with open("updated_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Updated JSON saved to 'updated_data.json'.")
