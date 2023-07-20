import json
import view
import controller
import datetime

def add_new_note_book():
    y_or_n = input('\nВы действительно хотите создать новую книгу заметок? '
                   '\nЭто удалит старую книгу. '
                   '\n(Y/N)?: ')
    if y_or_n == 'y' or y_or_n == 'Y':
        data = [
            [
                {'ID': 0},
                {'Heading': 'Заголовок'},
                {'Body': 'Тело'},
                {'Date/Time': f'{datetime.datetime.now().date()}/{datetime.datetime.now().time().hour}'
                              f':{datetime.datetime.now().time().minute}'
                              f':{datetime.datetime.now().time().second}'}
            ]
        ]
        with open("note_books.json", "w", encoding='utf-8') as write_file:
            write_file.write(json.dumps(data, ensure_ascii=False))
    elif y_or_n == 'n' or y_or_n == 'N':
        controller.button_click()
    else:
        print("\033[31m {}" .format("\nНе верный ввод, повторите попытку!"))
        print("\033[0m {}".format(" "))
        add_new_note_book()

def add_note():
    view.heading()