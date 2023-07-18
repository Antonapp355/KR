import view
import modul_menu

def button_click():
    value_m = view.menu()
    modul_menu.menu_operation(value_m)
    if value_m == 9:
        return exit
    if value_m != 9:
        button_click()