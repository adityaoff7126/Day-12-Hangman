README - Hangman Game (Python)

Description:
This is a simple Hangman-style word guessing game written in Python. The program randomly selects a word from a predefined list, and the player must guess the word one letter at a time. The player is given limited attempts to complete the word.

How the Program Works:
1. The program imports the random module to select a random word.
2. A list of words is defined.
3. One word is randomly selected from the list.
4. The selected word is hidden using underscores.
5. The player is given attempts equal to the word length plus two extra chances.
6. The player guesses letters.
7. If the guessed letter is correct, it replaces the corresponding underscore.
8. If the guessed letter is incorrect, one attempt is reduced.
9. The game continues until:
   - The player guesses the full word (Win), or
   - The player runs out of attempts (Lose).

Requirements:
- Python 3 installed on your system.

How to Run:
1. Save the program in a file named hangman.py.
2. Open terminal or command prompt.
3. Navigate to the folder containing the file.
4. Run the command:
   python hangman.py

Game Rules:
- Only one letter should be guessed at a time.
- Attempts decrease only when the guessed letter is not in the word.
- The game ends automatically when the word is guessed or attempts reach zero.

Possible Improvements:
- Add more words to the list.
- Prevent repeated guesses.
- Show used letters.
- Add graphical hangman stages.
- Add difficulty levels.
