import curses
import random
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from curses import wrapper
import time #time.sleep(0.2) KELL A MOZGÁS VÉGÉRE

def main(stdscr):
    stdscr.clear()


screen = curses.initscr() #képernyő
curses.noecho()
asd = screen.getmaxyx()  #asd = max y és max x
curses.curs_set(0)
screen.keypad(1)

x = asd[1]//2
y = asd[0]//2
a = random.randint(1, asd[0])
b = random.randint(1, asd[1])
over = False
direction = 0
screen.nodelay(1)


while not over:
    screen.clear()
    screen.addch(a, b, '&') # random helyen megjeleníti a kaját ('&' jelet)
    screen.addch(y,x, '#')
    screen.refresh() #megjelníti az új képernyőt

    action = screen.getch()


    if action == curses.KEY_UP and direction != 1:
        direction = 3
    elif action == curses.KEY_DOWN and direction != 3:
        direction = 1
    elif action == curses.KEY_RIGHT and direction != 2:
        direction = 0
    elif action == curses.KEY_LEFT and direction != 0:
        direction = 2

    if direction == 0:
        x += 1
    elif direction == 2:
        x -= 1
    elif direction == 1:
        y += 1
    elif direction == 3:
        y -= 1

    if (a == y) and (b == x):
        a = random.randint(1, asd[0])
        b = random.randint(1, asd[1])
        screen.delch(a, b)
        screen.addch(a, b, '&')
        screen.refresh()
    time.sleep(0.1)

    if y == asd[0] and x == asd[1]:
        over = True
screen.getch()



curses.endwin() #kilép, visszatér a képernyő
wrapper(main)
