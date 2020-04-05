import random
import os

hand = ['r', 'p', 's']
player = []
computer = []


def question():
    choice = [input('what would you show? [r]ock, [p]aper or [s]cissors: ')]
    if choice[0] == 'r':
        player.append('r')
    elif choice[0] == 'p':
        player.append('p')
    elif choice[0] == 's':
        player.append('s')
    random.shuffle(hand)
    p = hand.copy()
    computer.append(p[0])


def even():
    a = input('you\'re even! wanna try again? (y/n)')
    if a == 'y':
        player.clear()
        computer.clear()
        game()
    else:
        exit()


def computer_wins():
    b = input('I\'m sorry you lost! wanna try again? (y/n)')
    if b == 'y':
        player.clear()
        computer.clear()
        game()
    else:
        exit()


def player_wins():
    c = input('congratulations! you won! wanna try again? (y/n)')
    if c == 'y':
        player.clear()
        computer.clear()
        game()
    else:
        exit()


def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


def game():
    clear()
    question()
    if computer[0] == player[0]:
        even()
    elif computer[0] == 'r' and player[0] == 's':
        computer_wins()
        clear()
    elif computer[0] == 'r' and player[0] == 'p':
        player_wins()
        clear()
    elif computer[0] == 's' and player[0] == 'p':
        computer_wins()
        clear()
    elif computer[0] == 's' and player[0] == 'r':
        player_wins()
        clear()
    elif computer[0] == 'p' and player[0] == 'r':
        computer_wins()
        clear()
    elif computer[0] == 'p' and player[0] == 's':
        player_wins()
        clear()


if __name__ == "__main__":
    game()


