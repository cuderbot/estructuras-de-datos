# -*- coding: utf-8 -*-
from . import sep, option_not_valid, get_option
from .stack import menu_stack
from .queue import menu_queue


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
    }

    sub_menu = options.get(choice, option_not_valid)
    sub_menu()

