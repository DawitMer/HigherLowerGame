#import art
#import random for the array
#import the game_data for the celebrities information

import art
import random
import game_data

#logo for intro
print(art.logo)

def Celebrity_pick():
    """pick two random celebrity from the game_data array"""
    return random.choice(game_data.data)

#compare function
def compare(num1, num2):
    """compare two numbers and return a if number 1 is greater or will return b or else """
    if num1 > num2:
        return "a"
    else:
        return "b"



def game(celeb_a, celeb_b, score):
    """Take two celebrity as an input to compare and play the game"""
    # print the first celebrity information from array, has to be random
    if score != 0:
        print(f"You're right! Current score: {score}.")

    celebrityA = celeb_a
    print(f"Compare A: {celebrityA["name"]}, a {celebrityA["description"]}, from {celebrityA["country"]}.")
    # print vs logo
    print(art.vs)

    # print the second celebrity information from array, has to be random
    # what if the Celebrity_pick same person twice so we can do if else
    celebrityB = celeb_b
    while celebrityA == celebrityB:
        celebrityB = Celebrity_pick()
    print(f"Compare B: {celebrityB["name"]}, a {celebrityB["description"]}, from {celebrityB["country"]}.")

    # take input from the user A or B
    result = compare(celebrityA["follower_count"], celebrityB["follower_count"])
    A_or_B = input("who has more followers? Type 'A' or 'B': ").lower()


    if A_or_B == result:
        # compare if higher or lower if correct keep B and pick random from the array again
        # increase the score for the player
        game(celebrityB, Celebrity_pick(), score + 1)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")




game(Celebrity_pick(), Celebrity_pick(), 0)





