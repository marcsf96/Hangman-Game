#import relevant libraries
import random

#words to be used in the game
choices = ['3dhubs', 'marvin', 'print', 'filament', 'order', 'layer']

#choose a random word every new game from the list
rand_int = random.randint(0, len(choices)-1)
word = choices[rand_int]

#here characters are stored depending if they are coincident with the random word or not
previous = []
wrong = []

#counters for the game
num_goes = 5
stage_int = 5

#list that stores the current state of the man
stages = [
        "__________        ",
        "|        |      ",
        "|        0      ",
        "|       /|\     ",
        "|       / \     "
              ]


while num_goes > 0:

    product = ""
    '''
    This first loop allows the '_' to be placed in the right place. When the game is started at 
    first, all positions of the word are going to be underscores. As the user guesses, the loop
    substitutes the underscore for the character in case its coincident.
    '''
    for character in word:
        if character not in previous:
            product +=  " _ "

        else:
            product += character

    #self explanatory loop, if the product is equal to word, it means that the user won
    if product == word:
        print('Congratulations! You guessed correctly', word)
        break #if the condition is true, the game must stop, hence break the loop

    #shows what characters have been correctly guessed, otherwise underscore
    print("Guess the character:", product) 
    print(num_goes, "chances to get hanged!")

    #asks the user for an input
    user_input = input("guess a character: ")

    '''
    The next loop, appends character guesses in two lists. If the character exists in the word,
    it is appended in previous. Otherwise in wrong. 
    Then the first if statement checks if the new guess given by the user exists in either list,
    if it exists, return a warning message that that word is already guessed before
    '''
    if user_input in previous or user_input in wrong:
        print("Fish memory! You guessed this one already", user_input)

    elif user_input in word:
        previous.append(user_input)

    else:
        print()
        print("Wrong, try again")
        num_goes -= 1
        wrong.append(user_input)
        print()
        #printing is iterated over the range of the substraction stated so its printed vertically
        for i in range(stage_int - num_goes):
            print(stages[i])

    print()

if num_goes == 0:
    print("You didn't get", word)