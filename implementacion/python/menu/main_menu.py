# -*- coding: utf-8 -*-
from . import sep, option_not_valid, get_option
from .stack import menu_stack
from .queue import menu_queue
from .linked_list import menu_linked_list


def create_menu():
  choice = 1
  while choice != 0:
    print('')
    print(sep)
    print('Escoge un tipo de estructura de dato:')
    print(sep)
    print('')
    print('1.- Stack / Pila')
    print('2.- Queue / Cola')
    print('3.- Linked List / Listas Enlazadas')
    print('0.- Salir')
    print('')

    choice = get_option()

    print(sep)
    print('')
    
    options = {
      1: menu_stack,
      2: menu_queue,
      3: menu_linked_list
    }

    sub_menu = options.get(choice, option_not_valid)
    sub_menu()

