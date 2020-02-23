def asw(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mError! Please enter a valid input.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUser prefer not to input an option!\033[m')
        else:
            return n


def line(size=120):
    return '-' * size


def title(text):
    print(line())
    print(text.center(120))
    print(line())


def menu(list):
    title('MAIN MENU')
    counter = 1
    for item in list:
        print(f'\033[33m{counter}\033[m - \033[34m{item}\033[m')
        counter += 1
    print(line())
    option = asw('\033[32mEnter one option:\033[m ')
    return option
