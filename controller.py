"""
Напишите проект, содержащий функционал работы с заметками.
Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.
"""
from config import *
from model import *
from view import *


def main():
    show_banner()
    while True:
        show_main_menu(MAIN_MENU)
        num = input_num()
        if num == 0:
            break
        elif num == 1:
            show_all(get_all())
        elif num == 2:
            row = (str(get_new_id()) + DATA_SEPARATOR
                   + input_data("Введите заголовок: ") + DATA_SEPARATOR
                   + input_data("Введите текст: "))
            add_note(row)
            show_alert("Запись сохранена")
        elif num == 3:
            data = get_all()
            show_all(data)
            note_id = int(input_data("Введите id записи для редактирования или 0 для отмены: "))
            if note_id == 0:
                continue
            row = find_note(note_id, data)
            if row is None:
                show_error("Запись не найдена")
                continue
            show_note(row.split(DATA_SEPARATOR))
            row = (str(note_id) + DATA_SEPARATOR
                   + input_data("Введите заголовок: ") + DATA_SEPARATOR
                   + input_data("Введите текст: "))
            if edit_note(row):
                show_alert("Запись отредактирована")
            else:
                show_error("Запись не найдена")
        elif num == 4:
            show_all(get_all())
            note_id = int(input_data("Введите id записи для удаления или 0 для отмены: "))
            if note_id == 0:
                continue
            if delete_note(note_id):
                show_alert("Запись удалена")
            else:
                show_error("Запись не найдена")
        else:
            show_error("Команда не существует")
    show_alert("Программа завершена")


init_db()
main()
