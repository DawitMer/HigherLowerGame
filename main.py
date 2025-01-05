#import art
#import random for the array
#import the game_data for the celebrities information

import art
import random
import game_data



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

def format_data(celebrity):
    account_name = celebrity["name"]
    account_descr = celebrity["description"]
    account_country = celebrity["country"]

    return f"{account_name}, a {account_descr}, from {account_country}."


def game():
    """Take two celebrity as an input to compare and play the game"""
    print(art.logo)
    score = 0
    keep_playing = True
    celebrityA = Celebrity_pick()


    while keep_playing:
        if score != 0:
            print(f"You're right! Current score: {score}.")

        # print the first celebrity information from array, has to be random
        print(f"Compare A: {format_data(celebrityA)}")

        # print vs logo
        print(art.vs)

        # print the second celebrity information from array, has to be random
        # what if the Celebrity_pick same person twice so we can do if else
        celebrityB = Celebrity_pick()
        while celebrityA == celebrityB:
            celebrityB = Celebrity_pick()
        print(f"Compare B: {format_data(celebrityB)}")

        # take input from the user A or B
        result = compare(celebrityA["follower_count"], celebrityB["follower_count"])
        guess = input("who has more followers? Type 'A' or 'B': ").lower()

        print("\n" * 20)
        print(art.logo)
        if guess == result:
            # compare if higher or lower if correct keep B and pick random from the array again
            # increase the score for the player
            celebrityA = celebrityB
            score += 1
        else:
            keep_playing = False
            print(f"Sorry, that's wrong. Final score: {score}")




game()





