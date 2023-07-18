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
        print('1.Добавить.')
    if m == 2:
        print('2.Найти.')
    if m == 3:
        print('3.Редактировать.')
    if m == 4:
        print('4.Удалить.')
    if m == 5:
        print('5.Выход.')
        return modul_exit.m_exit()