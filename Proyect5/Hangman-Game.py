from random import choice

words = ['baker', 'dinosaur', 'helipad', 'shark']
correct_letters = []
incorrect_letters = []
attempts = 6
hits = 0
game_over = False


def choose_word(word_list):
    chosen_word = choice(word_list)
    unique_letters = len(set(chosen_word))

    return chosen_word, unique_letters


def request_letter():
    chosen_letter = ''
    is_valid = False
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while not is_valid:
        chosen_letter = input("Choose a letter: ")
        if chosen_letter in alphabet and len(chosen_letter) == 1:
            is_valid = True
        else:
            print("You didn't choose a valid letter.")

    return chosen_letter


def display_new_board(chosen_word):
    hidden_list = []

    for l in chosen_word:
        if l in correct_letters:
            hidden_list.append(l)
        else:
            hidden_list.append('-')

    print(' '.join(hidden_list))


def check_letter(chosen_letter, hidden_word, lives, matches):
    end = False

    if chosen_letter in hidden_word:
        correct_letters.append(chosen_letter)
        matches += 1
    else:
        incorrect_letters.append(chosen_letter)
        lives -= 1

    if lives == 0:
        end = lose()
    elif matches == unique_letters:
        end = win(hidden_word)

    return lives, end, matches


def lose():
    print("You ran out of lives.")
    print("The hidden word was " + word)

    return True


def win(discovered_word):
    display_new_board(discovered_word)
    print("Congratulations, you found the word!!!")

    return True


word, unique_letters = choose_word(words)

while not game_over:
    print('\n' + '*' * 20 + '\n')
    display_new_board(word)
   
