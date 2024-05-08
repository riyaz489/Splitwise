import os

from expense import *
from helpers.constants import MainMenu
from helpers.menu import Menu

if __name__ == '__main__':
    u_handler = UserHandler()
    g_handler = GroupHandler()
    e_handler = ExpenseHandler()

    while True:
        m = Menu()
        menu_items = [x.value for x in MainMenu]
        menu_items.append('Exit')
        m.draw_menu(menu_items)
        input()

        if MainMenu.AddExpense.value == menu_items[m.index]:
            amt = input('enter total amount: ')
            name = input('enter expense description: ')
            os.system('cls')
            print('select group\n')
            gpr_menu = [x for x in g_handler.groups.keys()]
            m = Menu()
            m.draw_menu(gpr_menu)
            group = g_handler.groups[gpr_menu[m.index]]
            input()
            os.system('cls')
            print('enter split Amount for group users\n')
            u_map = []
            t_amount = 0
            for u in group.users:
                a = input(f'enter amount for {u}: ')
                u_map.append((u,float(a)*-1))
                t_amount+= float(a)

            if abs(t_amount-float(amt))>1:
                # taking 1 margin for float errors
                print('total amount and divide amount does not match, try again... ')
                input()
                os.system('cls')
                continue
            os.system('cls')
            print('enter Amount paid by group users\n')
            t_amount = 0
            for u in group.users:
                a = input(f'enter amount for {u}: ')
                u_map.append((u, float(a)))
                t_amount += float(a)
            os.system('cls')

            if abs(t_amount-float(amt))>1:
                # taking 1 margin for float errors
                print('total amount and paid amount does not match, try again... ')
                input()
                os.system('cls')
                continue

            e_handler.add_expense(amt, u_map, group, name)
            input('expense added successfully, press any key to continue...')
            os.system('cls')

        elif MainMenu.AddUser.value == menu_items[m.index]:
            u_name = input('enter user name: ')
            u_handler.add_user(u_name)
            os.system('cls')

        elif MainMenu.AddGrpMember.value == menu_items[m.index]:
            print('select group\n')
            gpr_menu = [x for x in g_handler.groups.keys()]
            m = Menu()
            m.draw_menu(gpr_menu)
            group = gpr_menu[m.index]
            input()

            cgu = set(x for x in g_handler.groups[group].users)
            usr_menu = [x for x in u_handler.users.keys() if x not in cgu]
            print('select user \n')
            m = Menu()
            m.draw_menu(usr_menu)
            input()
            user = usr_menu[m.index]
            g_handler.add_memeber(group, user)


        elif MainMenu.AddGroup.value == menu_items[m.index]:
            g_name = input('enter group name: ')
            g_handler.add_group(g_name)
            os.system('cls')

        elif MainMenu.SimplifyGroupExpense.value == menu_items[m.index]:
            print('select group\n')
            gpr_menu = [x for x in g_handler.groups.keys()]
            m = Menu()
            m.draw_menu(gpr_menu)
            group = gpr_menu[m.index]
            input()
            os.system('cls')
        else:
            break



