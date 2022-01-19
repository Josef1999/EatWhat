from random import randint
import json


def load_menu(menu_name="menu.json"):
    with open(menu_name, encoding='utf-8') as f:
        menu = json.load(fp=f)
    return menu


def make_decision(main_menu: list or dict, level=1):
    print('='*level, end='')
    if type(main_menu) is dict:
        index = randint(0, len(main_menu.keys()) - 1)
        sub_menu_name = list(main_menu.keys())[index]
        print(sub_menu_name)
        make_decision(main_menu[sub_menu_name], level+1)
    else:
        main_menu = list(main_menu)
        print(main_menu[randint(0, len(main_menu) - 1)])


if __name__ == '__main__':
    menu = load_menu()
    make_decision(menu)
