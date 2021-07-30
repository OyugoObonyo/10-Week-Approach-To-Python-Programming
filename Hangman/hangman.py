"""
A simple console hangman game
"""
from random import choice

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
