import json
import view
import controller
import datetime
import os.path
import modul_id

def add_new_note_book():
    y_or_n = view.warning_message()
    if y_or_n == 'y' or y_or_n == 'Y':
        data = [
                {'ID': 0,
                'Heading': 'Заголовок',
                'Body': 'Тело',
                'Date/Time': f'{datetime.datetime.now().date()}/{datetime.datetime.now().time().hour}'
                              f':{datetime.datetime.now().time().minute}'
                              f':{datetime.datetime.now().time().second}'}
        ]
        with open("note_books.json", "w", encoding='utf-8') as write_file:
            write_file.write(json.dumps(data, ensure_ascii=False))
    elif y_or_n == 'n' or y_or_n == 'N':
        controller.button_click()
    else:
        view.exmessage_not_char()
        add_new_note_book()

def add_note():
    file = os.path.exists('note_books.json')
    if file:
        new_data ={'ID': modul_id.next_iD(),
               'Heading': f'{view.heading()}',
               'Body': f'{view.body()}',
               'Date/Time': f'{datetime.datetime.now().date()}/{datetime.datetime.now().time().hour}'
                             f':{datetime.datetime.now().time().minute}'
                             f':{datetime.datetime.now().time().second}'}
        with open("note_books.json", "r", encoding='utf-8') as read_file:
            data = list(json.load(read_file))

        data.append(new_data)

        with open('note_books.json', 'w', encoding='utf-8') as write_book:
            write_book.write(json.dumps(data, ensure_ascii=False))
    else:
        view.exmessage_not_book()