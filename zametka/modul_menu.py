import modul_add
import modul_search
import modul_del
import modul_exit

number_menu = 0

def menu_init(m):
    global number_menu
    number_menu = m

def menu_operation(m):
    if m == 1:
        print('1.Создать новую книгу заметок.')
        modul_add.add_new_note_book()
    if m == 2:
        print('2.Создать заметку.')
        modul_add.add_note()
    if m == 3:
        print('3.Найти заметку.')
    if m == 4:
        print('4.Редактировать заметку.')
    if m == 5:
        print('5.Удалить заметку.')
    if m == 6:
        print('6.Выход.')
        return modul_exit.m_exit()
