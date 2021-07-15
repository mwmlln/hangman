import random, time

# list for question word

animals = ["kangaroo", "chimpanzee", "tasmanian devil", "elephant", "giraffe", "wombat",]
sea_creatures = ["jellyfish", "sea monkey", "monkfish", "seahorse", "dolphin", "octopus"]
fruits = ["papaya", "dragon fruit", "kiwi fruit", "water melon", "lychee", "pineapple"]

# stages for wrong answer   
stages = [    '___________________',
              '|         |        ',
              '|         |        ',
              '|         0        ',
              '|        /|＼      ',
              '|        / ＼      ',
              '| GAME        OVER!' ]

stage_num = len(stages)   # getting the stage number so that it can be used as limit for incorrect attempt



def greeting():
    """
    Prompt user to input name and display greetings
    """
    user_name = input("Enter your name: \n")
    print(f"~~~~~~  Welcome to hangman game, {user_name} ~~~~~~")
    time.sleep(1)

def category_select():
    """
    Prompt user to select a category for the game and vaidate the input
    """
    print("~~~~~~  Please choose from one of following category: ~~~~~~")
    print("~~~~~~ 1. Animals, 2. Sea creatures, 3. Fruits ~~~~~~")
    category_num = input("Enter 1,2 or 3 >>>>> \n")
    if int(category_num) >= 0 and int(category_num) <=3:
        try:
            print(f"You chose {category_num}")
            print(f"Guess all the letters included in the words in the category {category_num}")
        except ValueError:     #NOR WORKING!!============= NEED TO FIX
            print('Please enter 1, 2 or 3')
    time.sleep(1)

def select_question():
    """
    random word selection from the list and display _ for each letter
    """
    word = animals[random.randint(0,5)]
    return(word)

def hangman():
    """
    display questions and checks the answer and count attempts
    """
    incorrect = 0
    question = []
    correct_guess = []
    word = select_question()
    answers = [i for i in word]
    print(f"Answer is set as {answers}")
    # word_len = len(word)   
    while incorrect < stage_num:              
        print("Can you guess the word? Enter one letter to see if you are right!")
        for i  in word:
            if i != " ":
                print("_  ", end="")
            elif i in correct_guess:
                print(i, end="")
            else:
                print(i, end="")
        print('\n')
        guessed = input("Enter one letter please! \n").lower()
        print(f"You entered {guessed}")
        if guessed in answers:
            print(f"{guessed} is the right answer")
            correct_guess.append(guessed)
            print(correct_guess)
            time.sleep(1)
        else:
            print(f"Letter {guessed.lower()} is not in the word!")
            incorrect += 1
            print("\n".join(stages[:incorrect])) 
            print("\n")
            time.sleep(1)

def main():
    # greeting() # greeting function
    # category_select() # choose category function NEED TO FIX VALIDATION
    hangman() 
        # Check data type -convert to lower case > (try: except errortype:)
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
