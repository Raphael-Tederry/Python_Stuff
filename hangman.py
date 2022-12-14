import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def print_lives(lives):
    stickman = ''
    if lives == 0:
        stickman = "\
     |------\n\
     |    O\n \
    | ---|---\n \
    |   / \\ \n \
    |  /   \\ \n \
    |_____"
    if lives == 1:
        stickman = "\
     |------\n\
     |    O\n \
    | ---|---\n \
    |   /  \n \
    |  /    \n \
    |_____"
    if lives == 2:
        stickman = "\
     |------\n\
     |    O\n \
    | ---|---\n \
    |      \n \
    |     \n \
    |_____"
    if lives == 3:
        stickman = "\
     |------\n\
     |    O\n \
    | ---|\n \
    |     \n \
    |      \n \
    |_____"
    if lives == 4:
        stickman = "\
     |------\n\
     |    O\n \
    |    |   \n \
    |        \n \
    |         \n \
    |_____"
    if lives == 5:
        stickman = "\
     |------\n\
     |    O\n \
    |        \n \
    |        \n \
    |         \n \
    |_____"
    if lives == 6:
        stickman = "\
     |------\n\
     |     \n \
    |        \n \
    |        \n \
    |        \n \
    |_____"
    print(stickman)


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print_lives(lives)
        print(f'You have {lives} lives left. \tAnd you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in the word. :(\n')

        elif user_letter in used_letters:
            print("You already tried that bro -_-\n")
        else:
            print('Invalid character. Please try again.\n')

    if lives == 0:
        print_lives(lives)
        print('Sorry you died, The word was ', word)
    else:
        print('You successfully guessed the word, ', word, '!!!')


if __name__ == '__main__':
    hangman()
