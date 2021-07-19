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
          '|         0        ',
          '|        /|＼      ',
          '|        / ＼      ',
          '| GAME        OVER!']

# Setting the stage number to be used as limit for incorrect attempts
stage_num = len(stages)


def greeting():
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
    time.sleep(0.3)


def category_select():
    """
    Prompt user to select a category for the game and vaidate the input
    """
    print("~~~~~~  Please choose from one of following category: ~~~~~~")
    print("~~~~~~ 1. Animals, 2. Sea creatures, 3. Fruits 4. All the category mixed  ~~~~~~")
    category_num = 0
    while not 1 <= category_num <= 4:
        try:
            category_num = int(input("Please enter 1, 2, 3 or 4  >>>  ")) 
            if 1 <= category_num <= 4:
                return category_num
            else:
                pass
        except ValueError as e:
            print("Only number 1, 2 or 3 accepted")

def select_question():
    """
    random word selection from the list and display _ for each letter
    """
    time.sleep(0.3)
    category_chosen = category_select()
    list_num  = category_chosen - 1
    print(f"Category {category_chosen}  was chosen")
    if category_chosen == 4:
        word = category[random.randint(0, 3)][random.randint(0, 5)]
        return(word)
    else:
        word = category[list_num][random.randint(0, 5)]
        return(word)
       

def hangman():
    """
    Main game function to display questions, check the answer and
    count attempts.
    Returns to the begining process if game completion condition is not met.
    Either word completion or reaching full stages will end the game.
    """
    incorrect = 0    # Setting the starting point of incorrect attempts
    correct_guess = set([])   # Creating a empty list to store correct answers
    word = select_question()    # Random word chosen by the function
    check_answer = word.replace(" ","")   # Removing the space for checking answer
    answers = [i for i in check_answer]    # Create list from the word without space
    print(f"Answer is set as {answers}")    # ******  For testing purpose ********
    while incorrect < stage_num:
        print("\n")
        print("Can you guess the word?")
        print("Enter one letter to see if you are right!")
        """
        Print out _ for the remaining letters to guess
        """
        for i in word:
            if i == " ":
                print(i, end=" ")
            elif i in correct_guess:
                print(i.upper(), end=" ")
            else:
                print("_  ", end=" ")
        print('\n')
        guessed = input("Enter one letter please! \n").lower()
        if guessed in answers:  # Checking the answer and determine the action
            if guessed in correct_guess:
                print("Ahhh surely you know you already pressded this letter,"
                      " it's already displayed!")
                time.sleep(0.1)           
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
                time.sleep(0.1)
        else:
            if len(guessed) > 1:
                print("***** Please input one letter at a time *****") 
            else:
                print(f"\" {guessed.upper()} \" is not in included in correct answer!")
                
            incorrect += 1    # Increment incorrect attempt
            print("\n".join(stages[:incorrect]))  # Display hangman image
            print("\n")
            time.sleep(0.1)
    if incorrect == stage_num:
        game_over()

    time.sleep(0.2)
    replay()


def game_over():
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
    play_again = input("Please press y to play, any other key to exit the game \n")
    if play_again.lower() == "y":
        hangman()
    else:
        print("Thank you for playing the game")

greeting()  # greeting function
hangman()

# ===== Still to fix ====
# sapce included in correct_guess list that needs to be removes
# brief instructions on how to play the game
# include the 4th option that selects a word from all the list
# when category chosen, feed back on the cagtegory name 

