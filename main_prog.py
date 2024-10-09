# Артём Галстян (3 вариант)
import os
from time import sleep


# CONSTANTS

# FOR FLAG
FLAG_LENGTH = 35
FLAG_WIDTH = 2
COLOR_ID = {'red': '\u001b[48;5;124m', 'white': '\u001b[48;5;231m', 'blue': '\u001b[48;5;19m', 'default': '\u001b[0m'}
COLOR_ORDER = ('red',
               'white',
               'blue')

# FOR PATTERN
COEFF = 3
HEIGHT_PAT = 10
K = HEIGHT_PAT * COEFF
SYMBOL_PAT = '\u001b[40m \u001b[0m' * 2

# FOR GRAPH Y=2X
SYMBOL_GRAPH = '\u001b[48;5;231m \u001b[0m' * 2
HEIGHT_GRAPH = 9

# FOR CHART
SYMBOL_CHART1 = '\u001b[48;5;19m|\u001b[0m'
SYMBOL_CHART2 = '\u001b[48;5;124m|\u001b[0m'
SCALE = 100
FILENAME = 'sequence.txt'


def draw_netherlands_flag():
    for i in range(len(COLOR_ORDER)):
        for j in range(FLAG_WIDTH):
            print(COLOR_ID[COLOR_ORDER[i]] + ' ' * FLAG_LENGTH + COLOR_ID['default'])


def draw_pattern_c():
    k, step = K, COEFF
    t = j = 0
    for i in range(HEIGHT_PAT + 1):
        print(' ' * j + SYMBOL_PAT + ' ' * abs(k) + SYMBOL_PAT + ' ' * t + SYMBOL_PAT + ' ' * abs(k) + SYMBOL_PAT)
        k -= step * 2
        if i < HEIGHT_PAT // 2:
            j += step
            t += step * 2
        else:
            j -= step
            t -= step * 2


def draw_graph_2x():
    for i in range(HEIGHT_GRAPH, -1, -1):
        print(' ' * i + SYMBOL_GRAPH)


def draw_chart():
    even = 0
    odd = 0
    with open(FILENAME) as f:
        check = True
        for num in [abs(float(el.rstrip())) for el in f.readlines()]:
            if check:
                odd += num
            else:
                even += num
            check = not check
        percent_even_cages = round(SCALE * (even / (odd + even)))
        percent_odd_cages = round(SCALE * (odd / (odd + even)))
        fill_chart(title='EVENS', percent_cages=percent_even_cages, abs_sum=round(even, 2), symbol_type=SYMBOL_CHART1)
        fill_chart(title='ODS', percent_cages=percent_odd_cages, abs_sum=round(odd, 2), symbol_type=SYMBOL_CHART2)
        print(f'\nTotal: {round(odd + even, 2)}')


def fill_chart(title, percent_cages, abs_sum, symbol_type):
    print(title)
    for i in range(SCALE):
        if percent_cages != 0:
            percent_cages -= 1
            print(symbol_type, end='')
        else:
            print('|', end='')
    print(f'\tABS SUM: {abs_sum}')


def main():
    funcs = [draw_netherlands_flag, draw_pattern_c, draw_graph_2x, draw_chart]
    i = 0
    while True:
        funcs[i]()
        i = (i + 1) % len(funcs)
        sleep(1)
        os.system("cls")


if __name__ == '__main__':
    main()
