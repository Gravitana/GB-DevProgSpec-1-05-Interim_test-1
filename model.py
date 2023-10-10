import os

from config import DB_FILE, DATA_SEPARATOR


def init_db():
    if not os.path.isfile(DB_FILE):
        with open(DB_FILE, "w", encoding="UTF-8") as file:
            file.write('')


def get_all():
    with open(DB_FILE, "r", encoding="UTF-8") as file:
        return file.readlines()


def get_new_id():
    data = get_all()
    if data:
        row = data[-1]
        last_id = int(row.split(DATA_SEPARATOR)[0])
    else:
        last_id = 0
    return last_id + 1


def add_note(note):
    if note[-1] != "\n":
        note += "\n"
    with open(DB_FILE, "a", encoding="UTF-8") as file:
        file.write(note)


def overwrite_all(data):
    with open(DB_FILE, "w", encoding="UTF-8") as file:
        for note in data:
            if note[-1] != "\n":
                note += "\n"
            file.write(note)


def delete_note(note_id):
    data = get_all()
    was_deleted = False
    for row in data:
        row_id = int(row.split(DATA_SEPARATOR)[0])
        if note_id == row_id:
            data.remove(row)
            was_deleted = True
            break
    if was_deleted:
        overwrite_all(data)

    return was_deleted
