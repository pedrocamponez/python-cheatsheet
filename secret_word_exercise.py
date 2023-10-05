"""
Create a game where the user has to guest the secret word
- I will create a secret word, and the user will type only one letter
- Check if the typed letter is in the word
  - if it is there, show the correct letter inside the word, that will be made of ******
  - if it is NOT there, show the current word
i.e: word is CARROT. If user typed B, show ******. If user typed A, show *A****
- Count user attempts.
"""

import os

secret_word = 'peitinho'
right_letters = ''
user_attempts = 0

while True:
    typed_letter = input('Type a letter: ')
    user_attempts += 1

    if len(typed_letter) > 1:
        print('Type just one letter.')
        continue

    if typed_letter in secret_word:
        right_letters += typed_letter

    right_letters_in_attempt = ''
    for secret_letter in secret_word:
        if secret_letter in right_letters:
            right_letters_in_attempt += secret_letter
        else:
            right_letters_in_attempt += '*'
    
    print('The word until now is:', right_letters_in_attempt)

    if right_letters_in_attempt == secret_word:
        os.system('cls')
        print('CONGRATULATIONS!! YOU WON!! :D')
        print('The word was', secret_word)
        print('Attempts: ', user_attempts)
        right_letters = ''
        user_attempts = 0