import time
import random
from tav import Tav
from draw import draw_d6

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def generate_monster() -> int:
    r = random.randint(1, 6)
    draw_d6(r)
    if r == 1 or r == 2 or r == 3:
        skeleton = '\U0001F480'
        print(skeleton + ' skeleton crawls out of the floor')
        print('roll required 3')
        return 3 
    if r == 4 or r == 5:
        robot = '\U0001F916'
        print(robot + 'robot falls from out of the sky')
        print('roll requierd 9')       
        return 9
    if r == 6:
        ghost = '\U0001F47B'
        print(ghost + ' ghost appearing from the trees')
        print('roll required 17')
        return 17

if __name__ == '__main__':

    # collecting user input
    name = input('Name: ')
    role = input('Role: ')

    player = Tav(name, role)

    print('Bludgeons & Flagons')

    player.print_character_sheet()

    print_dramatic_text('Our advanture begins in a dark forest ...')
    requirement = generate_monster()


