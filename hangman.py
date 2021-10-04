import random

hanging = [r"""
                +-------+
                |       |
                        |
                        |
                        |
                        |
            =============
           """,
           r"""
                +-------+
                |       |
                O       |
                        |
                        |
                        |
            =============
           """,
           r"""
                +-------+
                |       |
                O       |
                |       |
                        |
                        |
            =============
           """,
           r"""
                +-------+
                |       |
                O       |
               /|       |
                        |
                        |
            =============
           """,
           r"""
                +-------+
                |       |
                O       |
               /|\      |
                        |
                        |
            =============
           """,
           r"""
                +-------+
                |       |
                O       |
               /|\      |
               /        |
                        |
            =============
           """,
           r"""
                +-------+
                |       |
                O       |
               /|\      |
               / \      |
                        |
            =============
           """
           ]
 
word = random.choice(["Refresh", "Otter", "Sparkle", "Penguin", "Binge", "Whale", "Rainbow",
                      "Passport", "Pretzel", "Computer", "Steam", "Backpack", "Bubble", "Active",
                      "Excellent", "Simple", "Cartoon", "Onion", "Hamburger", "Example", "Trinket",
                      "Button", "Reverse", "Driven", "Kindle", "Light", "Freight", "Transport"])
secretWord = ['_'] * len(word)
wrongGuess = []

print("Welcome to Hangman!")

while True:
     print(hanging[len(wrongGuess)])
     print()
     print(' '.join(secretWord))
     print()     
     print("Wrong Letter(s): ", ' '.join(wrongGuess))
     print()
     
     guess = input("> ").lower()
     while True:          
          if len(guess) != 1 or not guess.isalpha():
               print("Please enter a SINGLE letter.")
          elif guess in wrongGuess:
               print("You've already guessed this letter.")
          else:
               break
          guess = input("> ").lower()
 
     for letter in range(len(word)):
          if guess in word[letter].lower():
               secretWord[letter] = word[letter]

     if '_' not in secretWord:
          print("You've Won!!!\nThe word was: ", ''.join(secretWord))
          break
     elif guess not in word.lower():
          wrongGuess.append(guess)
          if len(wrongGuess) == len(hanging) - 1:
               print(hanging[len(wrongGuess)])
               print("You've run out of guesses!\nThe secret word was:", word)
               break
