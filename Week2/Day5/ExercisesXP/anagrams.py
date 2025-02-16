from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker()

    while True:
        print("\nAnagram Checker")
        print("1. Enter a word")
        print("2. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "2":
            print("Goodbye!")
            break

        elif choice == "1":
            word = input("\nEnter a word: ").strip()

            if not word.isalpha():
                print("Error: Only alphabetic characters are allowed.")
                continue
            if " " in word:
                print("Error: Please enter only one word.")
                continue

            is_valid = checker.is_valid_word(word)
            anagrams = checker.get_anagrams(word)

            print(f"\nYOUR WORD: \"{word.upper()}\"")
            print("This is a valid English word." if is_valid else "This is not a valid English word.")
            print("Anagrams:", ", ".join(anagrams) if anagrams else "None found.")

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
