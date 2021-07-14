import random

# list for question word

animals = ["kangaroo", "chimpanzee", "tasmanian devil", "elephant", "giraffe", "wombat",]
sea_creatures = ["jellyfish", "sea monkey", "monkfish", "seahorse", "dolphin", "octopus"]
fruits = ["papaya", "dragon fruit", "kiwi fruit", "water melon", "lychee", "pineapple"]

# stages for wrong answer   
stages = ['',
              '___________________',
              '|         |        ',
              '|         |        ',
              '|         0        ',
              '|        /|＼      ',
              '|        / ＼      ',
              '|                  ']

def greeting():
    """
    Prompt user to input name and display greetings
    """
    user_name = input("Enter your name:")
    print(f"~~~~~~  Welcome to hangman game, {user_name} ~~~~~~")

def category_select():
    """
    Prompt user to select a category for the game and vaidate the input
    """
    print("~~~~~~  Please choose from one of following category: ~~~~~~")
    print("~~~~~~ 1. Animals, 2. Sea creatures, 3. Fruits ~~~~~~")
    category_num = input("Enter 1,2 or 3 >>>>> ")
    if int(category_num) >= 0 and int(category_num) <=3:
        try:
            print(f"You chose {category_num}")
        except ValueError:     #NOR WORKING!!============= NEED TO FIX
            print('Please enter 1, 2 or 3')

    # print(f"You chose {category_num}")

def display_question():
    """
    random word selection from the list and display _ for each letter
    """
    word = animals[random.randint(0,5)]
    print(word)
    word_len = len(word)
    print(word_len)
    qusestion = "_ " * len(word)
    print(qusestion)
 

def main():
    greeting() # greeting function
    category_select() # choose category function NEED TO FIX VALIDATION
    display_question()  # display question function
        #request user input
    # checking input function(While game_on = True)
        # Check data type -convert to lower case > (try: except errortype:)
        # check if answer is correct
            # if correct
                # replace __ to the letter 
                # check if the word is completed
                    # true complete the game(game_on = False) and return go to game over
                    # False back to the top of the while loop (input)
            # if the answer is wrong 
                # increment hangman stage by 1
                # check hangman stage is complete
                    # if complete (game_on = False) and user lose message and go to game over
                    # else go back to the top of the while loop (input)
    # game over 

main()
