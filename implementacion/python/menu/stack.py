# -*- coding: utf-8 -*-
from . import sep, option_not_valid, get_option
from data_structures.stack.array_stack import ArrayStack
from data_structures.stack.linkedlist_stack import LinkedListStack


def menu_stack():
  choice = 1
  while choice != 0:
    print('')
    print(sep)
    print('Escoge un tipo de estructura de datos:')
    print(sep)
    print('')
    print('1.- Static Stack / Pila estatica (pila implementada con un arreglo)')
    print('2.- Dynamic Stack / Pila dinamica (pila implementada con una lista enlazada)')
    print('0.- Salir')
    print('')

    choice = get_option()

    print(sep)
    print('')
    
    options = {
      1: sub_menu_stack_static,
      2: sub_menu_stack_dynamic,
    }
    
    sub_menu = options.get(choice, option_not_valid)
    sub_menu()


def create_menu_stack(s):
  choice = 1
  while choice != 0:
    print('')
    print(sep)
    print('Selecciona una accion:')
    print(sep)
    print('')
    print('1.- apilar un dato')
    print('2.- desapilar un dato')
    print('3.- ver último de la pila')
    print('4.- tamaño de la pila')
    print('0.- salir')
    print(sep)
    print('')

    try:
      choice = int(input())
    except Exception:
      choice = 0
    
    print('')
    print(sep)
    if choice == 1:
      print('push / apilar')
      print('')
      d = input('Ingresa un numero a almacenar:\t')
      s.push(d)
    elif choice == 2:
      print('pop / desapilar')
      try:
        s.pop()
      except IndexError as e:
        print(e)
    elif choice == 3:
      print('peek / leer último')
      print('')
      try:
        print(f'El ultimo dato ingresado es: {s.peek()}')
      except IndexError as e:
        print(e)
    elif choice == 4:
      print('size / tamaño')
      print('')
      print(f'El tamaño de la pila es: {s.size()}')
    else:
      break
    print(sep)


def sub_menu_stack_static():
  print('')
  print(sep)
  size = None
  try:
    size = int(input('Ingresa el tamaño de la cola:\t'))
  except Exception:
    size = 10
  print(sep)
  print('')

  s = ArrayStack()
  create_menu_stack(s)


def sub_menu_stack_dynamic():
  s = LinkedListStack()
  create_menu_stack(s)

