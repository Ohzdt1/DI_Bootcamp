from game import Game

def get_user_menu_choice():
    """Display the menu and get user choice."""
    print("\nMenu:")
    print("(g) Play a new game")
    print("(x) Show scores and exit")
    return input("Choose an option: ").lower()

def print_results(results):
    """Display final results."""
    print("\nGame Results:")
    print(f"You won {results['win']} times")
    print(f"You lost {results['loss']} times")
    print(f"You drew {results['draw']} times")
    print("\nThank you for playing!")

def main():
    """Main function that runs the game loop."""
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "g":
            game = Game()
            result = game.play()
            results[result] += 1  
            
        elif choice == "x":
            print_results(results)
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
