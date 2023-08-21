def menu():
    print(' \n * * * * * * * * * * * * * * * * * *'
          ' \n *                                 *'
          ' \n * 1.Создать новую книгу заметок.  *'
          ' \n * 2.Создать заметку.              *'
          ' \n * 3.Найти заметку.                *'
          ' \n * 4.Редактировать заметку.        *'
          ' \n * 5.Удалить заметку.              *'
          ' \n * 6.Показать список заметок.      *'
          ' \n * 7.Выход.                        *'
          ' \n *                                 *'
          ' \n * * * * * * * * * * * * * * * * * *\n')
    text = input('Введите номер операции: ')
    try:
        if int(text) > 0 and int(text) <= 6:
            return int(text)
        else: return exmessage_not_char()
    except:exmessage_not_char()

def search_menu():
    print(' \n * * * * * * * * * * * * * * * * * *'
          ' \n *                                 *'
          ' \n * 1.По ID.                        *'
          ' \n * 2.По названию.                  *'
          ' \n * 3.Назад.                        *'
          ' \n *                                 *'
          ' \n *                                 *'
          ' \n *                                 *'
          ' \n *                                 *'
          ' \n * * * * * * * * * * * * * * * * * *\n')
    text = input('Введите номер операции: ')
    try:
        if int(text) > 0 and int(text) <= 3:
            return int(text)
        else:
            return exmessage_not_char()
    except:
        exmessage_not_char()

def search_id():
    return input('Введите ID заметки: ')

def warning_message():
    return input('Вы действительно хотите создать новую книгу заметок?'
                 '\nЭто удалит старую книгу.'
                 '\n(Y/N)?: ')
def heading():
    return input('Введите название заметки: ')

def body():
    return input('Введите текст заметки: ')

def exmessage_not_char():
    print("\033[31m {}".format("\nНе верный ввод, повторите попытку!"),"\033[0m {}".format(" "))
    return input('Нажмите Enter для продолжения: ')

def exmessage_not_book():
    print("\033[31m {}".format('\nСоздайте книгу заметок.\n'),"\033[0m {}".format(" "))
    return input('Нажмите Enter для выхода в меню: ')

def not_func():
    print("\033[31m {}".format('\nЕще не сделано.\n'), "\033[0m {}".format(" "))
    return input('Нажмите Enter для выхода в меню: ')

def not_op():
    print('Еще не сделал.')