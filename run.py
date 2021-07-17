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

stage_num = len(stages)   # Setting the stage number so that it can be used as limit for incorrect attempt


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
    list_range = range(1,4)
    while int(category_num) != 1-3 :
        category_num = input("Enter 1,2 or 3 >>>>> \n")     
        try:
            if int(category_num) >= 0 and int(category_num) <=3:
                print(f"try succeeded,list_range is {list_range}")
                print(f"You chose {category_num}")
                # print(f"Guess all the letters included in the words in the category {category_num}")
        except Exception as e:     #NOR WORKING!!============= NEED TO FIX
            print('Please enter 1, 2 or 3')
        else:
            return category_num
    
    time.sleep(0.1)

def select_question():
    """
    random word selection from the list and display _ for each letter
    """
    category_chosen = category_select()
    print(f"Category {category_chosen} was chosen")
    word = animals[random.randint(0,5)]
    return(word)

def hangman():
    """
    Main game function to display questions, check the answer and count attempts.
    Returns to the begining process if game completion cndition is not met.
    Either word completion or reaching full stages will end the game.
    """
    incorrect = 0    # Setting the starting point of incorrect tries 
    # question = []    
    correct_guess = set([])   # Creating a empty list to store correct answers
    word = select_question()    # Random word chosen by the function
    answers = [i for i in word]    #Creating list of letters from the word
    print(f"Answer is set as {answers}")    # For testing purpose, NEED TO BE DELETED ON COMPLETION
    while incorrect < stage_num: 
        print("\n")             
        print("Can you guess the word? Enter one letter to see if you are right!")
        """
        Print out _ for the remaining letters to guess
        """
        for i  in word:
            if i ==  " ":
                print(i, end=" ")
            elif i in correct_guess:
                print(i.upper(), end=" ")
            else:
                print("_  ", end=" ")               
        print('\n')
        guessed = input("Enter one letter please! \n").lower()    #Prompting user input
        if guessed in answers:    # Checking the answer and run corresponding response 
            if guessed in correct_guess:
                print("Ahhh surely you know you already pressded this letter, it's already displayed!")
                time.sleep(0.1)
            else:
                print(f"{guessed.upper()} is the right answer!")
                correct_guess.add(guessed)   # Add correct letter to the list
                print(f"corect_guess is {correct_guess} and answer is {set(word)}")
                if  correct_guess == set(word) :
                    print(f"CONGRATULATIONS! You completed the word {word.upper()}. YOU WIN!")
                    break
                time.sleep(0.1)
        else:
            print(f"Letter {guessed.upper()} is not in the word!")
            incorrect += 1    # Increment incorrect attempt
            print("\n".join(stages[:incorrect]))     # Display hangman image stage
            print("\n")
            time.sleep(0.1)
    print("GAME COMPELETED")


def main():
    # greeting() # greeting function
    category_select() # choose category function NEED TO FIX VALIDATION
    hangman() 
        # Checking if the word is filled.
    # game over 

main()
