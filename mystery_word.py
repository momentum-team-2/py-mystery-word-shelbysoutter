import random
import string

file = open("words.txt")
text = file.read().split()
file.close()

easy_list = [
    word.upper()
    for word in text
    if 4 <= len(word) <= 6
]

normal_list = [
    word.upper()
    for word in text
    if 6 <= len(word) <= 8
]

hard_list = [
    word.upper()
    for word in text 
    if 8 <= len(word)
]

guess_list = []

def get_word_difficulty():
    difficulty = input('Please select difficult (e - Easy, n - Normal, h - Hard): ')
    # print(difficulty)
    # choose one word at random to be The Word that should be guessed based on difficulty
    if difficulty == 'e':
        word = random.choice(easy_list)
    elif difficulty == 'n':
        word = random.choice(normal_list)
    elif difficulty == 'h':
        word = random.choice(hard_list)
    else:
        return get_word_difficulty()
    print(f'The mystery word is {len(word)} characters long.')
    return word

    
def get_guess_list(guess_list):
    guess = input('Guess a letter: ').upper()
    #prevent user from guessing more than 1 letter at a time
    if len(guess) != 1:
        print('Please guess a single letter.')
        #add something so original prompt is returned
    else: 
        guess_list.append(guess)
    return guess_list

def display_word(word, guess_list):
    return (letter if letter in guess_list else '_' for letter in word)

def wrong_letters(word, guess_list):
    return sorted(set(
        letter
        for letter in guess_list
        if not letter in word
    ))

def play_game(word):
    guess_list = []
    while True:
        guesses_remaining = 8 - len(wrong_letters(word, guess_list))
        print(f'Incorrect letters: {" ".join(wrong_letters(word, guess_list))}.')
        print(f'Mystery Word: {" ".join(display_word(word, guess_list))}')
        print(f'You have {guesses_remaining} guesses remaining.')
        if '_' not in display_word(word, guess_list):
            print(f'You win, the Mystery Word was {word}')
            play_again()
            return
        if guesses_remaining == 0:
            print(f'GAME OVER, the Mystery Word was {word}.')
            play_again()
            return
        guess_list = get_guess_list(guess_list)

def play_again():
    if input('Would you like to play again? (y/n): ') == 'y':
        new_word = get_word_difficulty()
        play_game(new_word)
    return

if __name__ == '__main__':
    word = (get_word_difficulty())
    play_game(word)


