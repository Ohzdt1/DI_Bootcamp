#🌟 Exercise 1 : What are you learning ?

def display_message():
    print('Generative AI and Machine Learning')

display_message()


#🌟 Exercise 2: What’s your favorite book ?

def favorite_book(title ):
    print("One of my Favorite Books is: " + title)


favorite_book('The Name of the Wind')

#🌟 Exercise 3 : Some Geography

def describe_city(city, country ='Israel'):
    if city == 'Jerusalem':
        print(f'{city} is in {country}')


describe_city('Jerusalem')
describe_city('Caracas')


#Exercise 4 : Random
import random

def random_num(user_num):
    if 1 <= user_num <= 100:
        random_num = random.randint(1, 100)
        if user_num == random_num:
            print("Phychic Guess")
        else:
            print(f'{user_num} is a wrong guess the random number is: {random_num}')
    else:
        print("only enter a number between 1 - 100")

random_num(37)


#🌟 Exercise 5 : Let’s create some personalized shirts !

def make_shirt(size="Large", message="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{message}'.")

make_shirt()
make_shirt('Medium')
make_shirt('Small', "Code is Life")

make_shirt(size="XL", message="Keep Calm and Code On")
make_shirt(message="Debugging is my cardio", size="M")

#🌟 Exercise 6 : Magicians …

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"

make_great(magician_names)

show_magicians(magician_names)

#🌟 Exercise 7 : Temperature Advice


import random

def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10, 16), 1)
    elif season == "spring":
        return round(random.uniform(5, 25), 1)
    elif season == "summer":
        return round(random.uniform(20, 40), 1)
    elif season == "autumn" or season == "fall":
        return round(random.uniform(10, 25), 1)
    else:
        return round(random.uniform(-10, 40), 1)

def get_season_from_month(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        return None  
    
def main():
    try:
        month = int(input("Enter the number of the month (1-12): "))
        season = get_season_from_month(month)
        if season is None:
            print("Invalid month. Please enter a number between 1 and 12.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    temperature = get_random_temp(season)
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today. ")
    elif 0 <= temperature <= 16:
        print("Quite chilly! Don’t forget your coat. ")
    elif 16 < temperature <= 23:
        print("It's a pleasant temperature. A light jacket should be enough. ")
    elif 24 <= temperature <= 32:
        print("It's warm outside! Stay hydrated. ")
    else:
        print("It's really hot! Make sure to stay cool and drink plenty of water.")

main()


#🌟 Exercise 8 : Star Wars Quiz

# Star Wars Quiz
data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def star_wars_quiz():
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []  

    for item in data:
        user_answer = input(f"{item['question']} ").strip()
        
        if user_answer.lower() == item['answer'].lower():
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer was: {item['answer']}\n")
            incorrect_answers += 1
            wrong_answers.append({"question": item['question'], "your_answer": user_answer, "correct_answer": item['answer']})

    print("\n--- Quiz Results ---")
    print(f"Correct Answers: {correct_answers}")
    print(f"Incorrect Answers: {incorrect_answers}")

    if wrong_answers:
        print("\nQuestions you got wrong:")
        for item in wrong_answers:
            print(f"{item['question']}")
            print(f"Your Answer: {item['your_answer']}")
            print(f"Correct Answer: {item['correct_answer']}\n")

    if incorrect_answers > 3:
        print("You got more than 3 wrong. Try again!\n")
        retry = input("Do you want to play again? (yes/no): ").strip().lower()
        if retry == "yes":
            star_wars_quiz()
        else:
            print("Thanks for playing!")

star_wars_quiz()
