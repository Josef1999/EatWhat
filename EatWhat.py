from random import randint
import json


def load_menu(menu_name="menu.json"):
    with open(menu_name, encoding='utf-8') as f:
        menu = json.load(fp=f)
    return menu


def make_decision(main_menu):
    cur_option = main_menu
    while type(cur_option) is not str:
        option_name=None
        if type(cur_option) is list:
            index = randint(0, len(cur_option)-1)
            cur_option = cur_option[index]
        elif type(cur_option) is dict:
            index = randint(0, len(cur_option.keys()) - 1)
            option_name = list(cur_option.keys())[index]
            cur_option = cur_option[option_name]
        else:
            raise NotImplementedError()
        if option_name is not None:
            print(option_name)
    print(cur_option)

if __name__ == '__main__':
    menu = load_menu()
    make_decision(menu)
