# -*- coding: utf-8 -*-
from . import option_not_valid, get_option, sep
from data_structures.queue.array_queue import ArrayQueue
from data_structures.queue.linkedlist_queue import LinkedListQueue

def menu_queue():
  choice = 1
  while choice != 0:
    print('')
    print(sep)
    print('Escoge un tipo de estructura de datos:')
    print(sep)
    print('')
    print('1.- Static Queue / Cola estatica')
    print('2.- Dynamic Queue / Cola dinamica')
    print('0.- Salir')
    print('')

    choice = get_option()

    print(sep)
    print('')
    
    options = {
      1: sub_menu_queue_static,
      2: sub_menu_queue_dynamic,
    }
    
    sub_menu = options.get(choice, option_not_valid) 
    sub_menu()


def create_sub_menu_queue(q):
  choice = 1
  while choice != 0:
    print('')
    print(sep)
    print('Selecciona una accion:')
    print(sep)
    print('')
    print('1.- encolar un dato')
    print('2.- desencolar un dato')
    print('3.- ver el primer dato de la cola')
    print('4.- tamaño de la cola')
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
      print('en queue / encolar')
      print('')
      d = input('Ingrese un numero a almacenar:\t')
      try:
        q.enqueue(d)
      except IndexError as e:
        print(e)
    elif choice == 2:
      print('de queue / desencolar')
      print('')
      try:
        q.dequeue()
      except IndexError as e:
        print(e)
    elif choice == 3:
      print('front / ver el primer dato de la cola')
      print('')
      try:
        print(f'El primer dato en ser ingresado es: {q.front()}')
      except IndexError as e:
        print(e)
    elif choice == 4:
      print('size / tamaño de la cola')
      print('')
      print(f'El tamaño de la cola es: {q.size()}')
    else:
      break
    print(sep)


def sub_menu_queue_static():
  print('')
  print(sep)
  size = None
  try:
    size = int(input('Ingresa el tamaño de la cola: '))
  except Exception:
    size = 10
  print(sep)
  print('')
  
  q = ArrayQueue()
  create_sub_menu_queue(q)


def sub_menu_queue_dynamic():
  q = LinkedListQueue()
  create_sub_menu_queue(q)

