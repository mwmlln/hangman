import random
import time

# list for question word
animals = ["kangaroo", "chimpanzee", "tasmanian devil",
           "elephant", "giraffe", "wombat"]
sea_creatures = ["jellyfish", "sea monkey", "monkfish",
                 "seahorse", "dolphin", "octopus"]
fruits = ["papaya", "dragon fruit", "kiwi fruit", "water melon",
          "lychee", "pineapple"]

category = [animals, sea_creatures, fruits]

# stages for wrong answer
stages = ['___________________',
          '|         |        ',
          '|         |        ',
          '|         |        ',
          '|         0        ',
          '|        /|＼      ',
          '|        / ＼      ',
          '| GAME        OVER!']

# Setting the stage number to be used as limit for incorrect attempts
stage_num = len(stages)


def display_greeting():
    """
    Prompt user to input name and display greetings
    """
    print("WELCOME TO")
    # Title ASCII ART
    print(" ██░ ██  ▄▄▄       ███▄    █  "
          " ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ ")
    print("▓██░ ██▒▒████▄     ██ ▀█   █  "
          "██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ ")
    print("▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒"
          "██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒")
    print("░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░"
          "▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒")
    print("░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░"
          "▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░")
    print(" ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  "
          "░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ")
    print(" ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░"
          "  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░")
    print(" ░  ░░ ░  ░   ▒      ░   ░ ░ "
          "░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ ")
    print(" ░  ░  ░      ░  ░         ░  "
          "     ░        ░         ░  ░         ░ ")

    user_name = input("Please enter your name: \n")
    print(f"~~~~~~  Welcome to hangman game, {user_name} ~~~~~~")
    pause()


def display_instructions():
    """
    Ask user if instruction is need and displays instruction as requested
    """
    print("Would you like a brief instruction on how to play?")
    instruction_on = input("Press y if yes, any other key to play game : \n")
    if instruction_on.lower() == "y":
        instructions_text()
        print("Are you ready to play?")
        game_start = input("Press Any key to start a game >> \n")
    else:
        pass


def instructions_text():
    """
    Display instructions
    """
    print("Here is instruction on how to play \n"
          "1. Choose a category\n"
          "2. The same number of Underscores '_' will be displayed \n"
          "   as letters in the word.\n"
          "3. Guess the word\n"
          "   Only one alphabet key should be entered at each time.\n"
          "   Space between the words is considered incorrect.\n"
          "4. If your answer is correct, the letter will be displayed\n"
          "   instead of the underscore'_'.\n"
          "5. If you guess all the letters and complete the word,\n"
          "   you win the game\n"
          "7. If the incorrect answer is entered, hangman image will progress.\n"
          "8. If the number of incorrect attempts reaches the limit \n"
          "   and hangman image completes, game over!")


def category_select():
    """
    Prompt user to select a category for the game and validate the input
    """
    print("~~~~~~  Please choose one of following category: ~~~~~~\n")
    print("~~ 1. Animals, 2. Sea creatures, 3. Fruits "
          "4. All the category mixed  ~~\n")
    category_num = 0
    while not 1 <= category_num <= 4:
        try:
            category_num = int(input("Please enter 1, 2, 3 or 4  >>>  \n"))
            if 1 <= category_num <= 4:
                return category_num
            else:
                pass
        except ValueError as e:
            print("Only number 1, 2, 3 or 4 accepted")


def select_question():
    """
    Random word selection from the list and display _ for each letter
    """
    pause()
    category_chosen = category_select()
    list_num = category_chosen - 1
    print(f"Category {category_chosen}  was chosen")
    if category_chosen == 4:
        category_item = random.choice(category)
        word = random.choice(category_item)
        return(word)
    else:
        category_item = category[list_num]
        word = random.choice(category_item)
        return(word)


def start_game():
    """
    Main game function to display questions, check the answer and
    count attempts.
    Repeats process if game completion condition is not met.
    Either word completion or reaching full stages will end the game.
    """
    incorrect = 0    # Setting the starting point of incorrect attempts
    correct_guess = set([])   # Creating a empty list to store correct answers
    word = select_question()    # Random word chosen by the function
    check_answer = word.replace(" ", "")   # Removing space from answer
    answers = [i for i in check_answer]    # Create list from the word
    wrong_guess = []   # Incorrect letters goes in here
    while incorrect < stage_num:
        display_guess_message()
        """
        Print out _ for the remaining letters to guess
        """
        for i in word:
            if i == " ":
                print(i, end="  ")
            elif i in correct_guess:
                print(i.upper(), end=" ")
            else:
                print("_  ", end=" ")
        print('\n')
        guessed = input("Enter one letter please! \n").lower()
        if guessed in answers:  # Checking the answer and determine the action
            if guessed in correct_guess:
                display_alredy_used()
                pause()
            else:
                print(f"{guessed.upper()} is the right answer!")
                correct_guess.add(guessed)   # Add correct letter to the list
                word_letters = word.replace(" ", "")
                if correct_guess == set(word_letters):
                    print(word.upper())
                    print(f"CONGRATULATIONS! "
                          f"You completed the word {word.upper()}. YOU WIN!")
                    you_win()
                    break
                pause()
        else:
            if len(guessed) > 1:
                print("***** Please input one letter at a time *****")
            else:
                print(f"' {guessed.upper()}' is not in correct answer!")

            incorrect += 1    # Increment incorrect attempt
            print("\n".join(stages[:incorrect]))  # Display hangman image
            print("\n")
            wrong_guess.append(guessed.upper())
            print(f"Your incorrect guesses: {wrong_guess} ")
            pause()
    if incorrect == stage_num:
        print(f"Answer is {word.upper()}")
        game_over()

    pause()
    replay()


def display_guess_message():
    print("\n")
    print("Can you guess the word?")
    print("Enter one letter to see if you are right!")


def display_alredy_used():
    print("Ahhh surely you know you already pressed this letter,"
          " it's already displayed!")


def game_over():
    """
    GAME OVER ascii art
    """
    print(" ██████╗  █████╗ ███╗   ███╗███████╗"
          "     ██████╗ ██╗   ██╗███████╗██████╗")
    print("██╔════╝ ██╔══██╗████╗ ████║██╔════╝"
          "    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
    print("██║  ███╗███████║██╔████╔██║█████╗   "
          "   ██║   ██║██║   ██║█████╗  ██████╔╝")
    print("██║   ██║██╔══██║██║╚██╔╝██║██╔══╝     "
          " ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
    print("╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗  "
          "  ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
    print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝  "
          "   ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")


def you_win():
    print(" _______ _______ _______     _______ _______ _______ _______ ")
    print("|\     /|\     /|\     /|   |\     /|\     /|\     /|\     /|")
    print("| +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ | +---+ |")
    print("| |   | | |   | | |   | |   | |   | | |   | | |   | | |   | |")
    print("| |Y  | | |O  | | |U  | |   | |W  | | |I  | | |N  | | |!  | |")
    print("| +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ | +---+ |")
    print("|/_____\|/_____\|/_____\|   |/_____\|/_____\|/_____\|/_____\|\n")


def replay():
    print("Would you like to play again?")
    print("Enter y or press RUN PROGRAM button above to play again."
          "or press any other key to exit the game.")
    play_again = input(
        "Please press y to play, any other key to exit the game \n")
    if play_again.lower() == "y":
        start_game()
    else:
        print("Thank you for playing the game")


def pause():
    time.sleep(0.2)


def main():
    display_greeting()  # greeting function
    display_instructions()  # display instruction if user chooses
    start_game()


main()
