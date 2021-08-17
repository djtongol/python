from words import words
import random
import string

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word= random.choice(words)
    
    return word.upper()

def hangman():
    word= get_valid_word(words)
    word_letters = set(word) 
    alphabet=set(string.ascii_uppercase)
    used_letters= set()

    lives=6


    #getting user input
    while len(word_letters)>0 and lives > 0:
        #letter used
        print('You have ', lives,' You have used these letters:',' '.join(used_letters))
        #what the current word is
        word_list= [letter if letter  in used_letters else '-' for letter in word]
        print('Current word:',' '.join(word_list))
        

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives=lives-1
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already guessed that letter, please try again')
        else:
            print("Invalid Character, Try again")
    
    if lives==0:
        print('You died, sorry. The word was ', word)
    else:
        print('You guessed the word', word, '!!')

hangman()