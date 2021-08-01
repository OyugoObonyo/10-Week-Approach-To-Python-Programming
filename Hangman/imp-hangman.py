"""
An improvement of the simple console hangman game
Actualized improvements can be found in the IMPROVE file 
"""
from random import choice, randint
import requests


def word_generator():
    """ 
    Generates random strings and stores the generated strings in a list
    """
    word_file = "/usr/share/dict/words"
    words = open(word_file).read().splitlines()
    words_count = len(words)
    index = randint(0, (words_count - 5))
    words_list = words[index:(index + 5)]
    return words_list

words = word_generator()
print(words)
print(type(words))
print(len(words))
"""
# Generate a random list of strings
words = ["Tree","Grass","Nature","Wildlife","Habitat"]
word = choice(words)
# maximum number of user guesses is equivalent to lives
lives = 2

print (f"Available words: {words}")
print ("INSTRUCTIONS: PICK ANY WORD FROM THE AVAILABLE WORDS. YOU HAVE ONLY 2 CHANCES TO PICK THE CORECT WORD")
print("\n")

while lives != 0:
    user_guess = input("SELECT A WORD ")
    if user_guess not in words:
        print("ERROR: You can only select words that exist in the list")
        continue
    elif user_guess == word:
        print(f"CORRECT! {user_guess} exists at index {words.index(user_guess)}")
        break
    elif user_guess != word:
        lives -= 1
        if lives == 0:
            print(f"GAME OVER! You are out of chances. Correct choice is {word}")
        else:
            print (f"INCORRECT! Guess is wrong. You have {lives} chance(s) left") 
"""
