import random


def play():
    user = input("Choose:\n\t 'r' for rock, 'p' for paper, 's' for scissors. ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'You won!!!'

    return "You lost :("


def is_win(player, opponent):  # player pov
    return ((player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (
                player == 's' and opponent == 'p'))



if __name__ == '__main__':
    print(play())




