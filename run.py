import random
import time

# list for question word
animals = ["kangaroo", "chimpanzee", "tasmanian devil",
           "elephant", "giraffe", "wombat"]
sea_creatures = ["jellyfish", "sea monkey", "monkfish",
                 "seahorse", "dolphin", "octopus"]
fruits = ["papaya", "dragon fruit", "kiwi fruit", "water melon",
          "lychee", "pineapple"]

category = [animals, sea_creatures, fruits
]

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
    user_name = input("Please enter your name: \n")
    print(f"~~~~~~  Welcome to hangman game, {user_name} ~~~~~~")
    time.sleep(1)


def category_select():
    """
    Prompt user to select a category for the game and vaidate the input
    """
    print("~~~~~~  Please choose from one of following category: ~~~~~~")
    print("~~~~~~ 1. Animals, 2. Sea creatures, 3. Fruits ~~~~~~")
    category_num = 0
    while category_num != 1 and category_num != 2 and category_num != 3:
        category = input("Enter 1,2 or 3 >>>>> \n")
        try: 
            category_num = int(category)
        except Exception as e:
            print("Plesae enter 1, 2, or 3")

    if category_num == 1 or category_num == 2 or category_num == 3:
        return category_num
        print(f"category_num {category_num} of type {type(category_num)}is returned")
        
        print(type(category_num))

    print(f"You chose {category_num}")
    return category_num
    time.sleep(0.1)


def select_question():
    """
    random word selection from the list and display _ for each letter
    """
    category_chosen = category_select()
    print(f"Category {category_chosen} was chosen")
    word = animals[random.randint(0, 5)]
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
    answers = [i for i in word]    # Create list from the word
    print(f"Answer is set as {answers}")    # For testing purpose
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
                    break
                time.sleep(0.1)
        else:
            print(f"Letter {guessed.upper()} is not in the word!")
            incorrect += 1    # Increment incorrect attempt
            print("\n".join(stages[:incorrect]))  # Display hangman image
            print("\n")
            time.sleep(0.1)
    print("GAME COMPELETED")
    time.sleep(0.2)
    replay()


def main():
    category_select()   # choose category function NEED TO FIX VALIDATION
    hangman()


def replay():
    print("Would you like to play again?")
    print("Enter y or press RUN PROGRAM button above to play again."
          "or press any other key to exit the game.")
    play_again = input("Please press y to play, any other key to exit the game \n")
    if play_again.lower() == "y":
        main()
    else:
        print("Thank you for playing the game")

greeting()  # greeting function
main()
