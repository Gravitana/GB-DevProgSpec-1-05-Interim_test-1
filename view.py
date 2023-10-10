from config import DATA_SEPARATOR


def input_num():
    return int(input())


def input_data(message):
    return input(message)


def show_banner():
    print("╔═════════════════════════════════════╗")
    print("║            З А М Е Т К И            ║")
    print("╚═════════════════════════════════════╝")


def show_main_menu(instruction):
    print("╔═════════════════════════════════════╗")
    print("║      Г Л А В Н О Е   М Е Н Ю        ║")
    print("╟─────────────────────────────────────╢")
    for key, value in instruction.items():
        print("║" + str(key).rjust(3) + " : " + value.ljust(30) + " ║")
    print("╚═════════════════════════════════════╝")


def show_alert(message):
    print("╔═════════════════════════════════════╗")
    print("║ " + message.ljust(35) + " ║")
    print("╚═════════════════════════════════════╝")


def show_error(message):
    print("╔════════╤════════════════════════════╗")
    print("║ ОШИБКА │ " + message.ljust(26) + " ║")
    print("╚════════╧════════════════════════════╝")


def show_note(row):
    print('║ {:3d} : {} – {}'.format(int(row[0]), row[1], row[2], ), end='')


def show_all(lst):
    if lst:
        print("╔═════════════════════════════════════╗")
        print("║            З А М Е Т К И            ║")
        print("╟─────────────────────────────────────╜")
        for row in lst:
            show_note(row.split(DATA_SEPARATOR))
        print("╙─\n")
    else:
        show_error("Ничего не найдено")
