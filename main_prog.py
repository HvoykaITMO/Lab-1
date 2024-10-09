#Артём Галстян (3 вариант)
#Артём Галстян (3 вариант)
#Артём Галстян (3 вариант)
#Артём Галстян (3 вариант)
#Артём Галстян (3 вариант)
#Артём Галстян (3 вариант)
#Артём Галстян (3 вариант)


# CONSTANTS
FLAG_LENGTH = 35
FLAG_WIDTH = 2
COLOR_ID = {'red': '\u001b[48;5;124m', 'white': '\u001b[48;5;231m', 'blue': '\u001b[48;5;19m', 'default': '\u001b[0m'}
COLOR_ORDER = ('red',
               'white',
               'blue')


def draw_netherlands_flag():
    for i in range(len(COLOR_ORDER)):
        for j in range(FLAG_WIDTH):
            print(COLOR_ID[COLOR_ORDER[i]] + ' ' * FLAG_LENGTH + COLOR_ID['default'])


COEFF = 3
H = 10
K = H * COEFF
STEP = COEFF
SYMBOL = '\u001b[40m \u001b[0m' * 2


def dram_symbol_c():
    global K
    k = K
    step = COEFF
    j = 0
    t = 0
    for i in range(H + 1):
        print(' ' * j + SYMBOL + ' ' * abs(k) + SYMBOL + ' ' * t + SYMBOL + ' ' * abs(k) + SYMBOL)
        k -= step * 2
        if i < H // 2:
            j += step
            t += step * 2
        else:
            j -= step
            t -= step * 2


def main():
    draw_netherlands_flag()
    dram_symbol_c()


if __name__ == '__main__':
    main()
