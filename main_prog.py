# Артём Галстян (3 вариант)
import os
from time import sleep


# CONSTANTS

# TIME
SWAP_SLIDE_TIME = 7

# FOR FLAG
FLAG_LENGTH = 35
FLAG_WIDTH = 2
COLOR_ID = {'red': '\u001b[48;5;124m', 'white': '\u001b[48;5;231m', 'blue': '\u001b[48;5;19m', 'default': '\u001b[0m'}
COLOR_ORDER = ('red',
               'white',
               'blue')

# FOR PATTERN
SYMBOL_PAT = '\u001b[40m   \u001b[0m'
PATTERN_REPEAT_AMOUNT = 4

# FOR GRAPH Y=2X
SYMBOL_GRAPH = '\u001b[48;5;231m   \u001b[0m'
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


def draw_pattern_c(amount=PATTERN_REPEAT_AMOUNT):
    step = SYMBOL_PAT.count(' ')
    total_gaps = step * 7

    k = total_gaps
    j = 0
    i = 1
    step = SYMBOL_PAT.count(' ')
    while abs(k) < total_gaps + 1:
        if k < 0 < i:
            line = (' ' * j + SYMBOL_PAT).ljust(total_gaps + len(SYMBOL_PAT) + step, ' ')
            print(line * amount)
            k += step * 2
            i = -1
            j += step * i
            continue
        line = (' ' * j + SYMBOL_PAT + ' ' * abs(k) + SYMBOL_PAT).ljust(total_gaps + len(SYMBOL_PAT) * 2, ' ')
        print(line * amount)
        k += step * 2 * (-i)
        j += step * i


def draw_graph_2x():
    strip_l = ''
    for i in range(HEIGHT_GRAPH * 2, -1, -1):
        line = (f'{i:>2}' + '--' * i + SYMBOL_GRAPH)
        print(line + strip_l)
        if i % 2 == 0:
            strip_l = '| ' + strip_l
        else:
            strip_l = '  ' + strip_l
    line = '   0'
    for i in range(1, HEIGHT_GRAPH + 1):
        line += f'---{i}'
    print(line)


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
        sleep(SWAP_SLIDE_TIME)
        os.system("cls")


if __name__ == '__main__':
    main()
