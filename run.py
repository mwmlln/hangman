# python code goes here
# list for question word

animals = ["kangaroo", "chimpanzee", "tasmanian devil", "elephant", "giraffe", "wombat",]
sea_creatures = ["jellyfish", "sea monkey", "monkfish", "seahorse", "dolphin", "octopus"]
fruits = ["papaya", "dragon fruit", "kiwi fruit", "water melon", "lychee", "pineapple"]


def greeting():
    """
    prompt user name input and display greetings
    """
    user_name = input("Enter your name:")
    
    print(f"Welcome to hangman game, {user_name}")


def main():
    greeting() # greeting function
    # choose category function
    # display question function
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
