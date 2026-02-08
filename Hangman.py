import random

words = ["tiger", "lion"]
word = random.choice(words)
guess_word = ["_"] * len(word)
attempt = len(word) + 2
while attempt > 0 and "_" in guess_word:
    print("Hangman Word: "," ".join(guess_word))
    guess = ""
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guess = input(" Guess word: ")
                guess_word[i] = guess
                print(guess_word)
                # continue
    else:
        attempt -= 1
        print(attempt)
if "_" not in guess_word:
            print("You Win")
else:
    print("You Lose")   
