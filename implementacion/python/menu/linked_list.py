# -*- coding: utf-8 -*-
from . import sep, option_not_valid, get_option
from data_structures.linked_list.linear_singly import LinkedListLinearSingly


def menu_linked_list():
  choice = 1
  while choice != 0:
    print('')
    print(sep)
    print('Escoge un tipo de estructura de datos:')
    print(sep)
    print('')
    print('1.- Linked List Linear Singly / Lista enlazada simple')
    print('0.- Salir')
    print('')

    choice = get_option()

    print(sep)
    print('')
    
    options = {
      1: sub_menu_linked_list_singly,
    }
    
    sub_menu = options.get(choice, option_not_valid) 
    sub_menu()


def create_sub_menu_linked_list(ll):
  choice = 1
  while choice != 0:
    print('')
    print(sep)
    print('Selecciona una accion:')
    print(sep)
    print('')
    print('1.- agregar un nodo')
    print('2.- eliminar un nodo')
    print('3.- buscar un nodo')
    print('4.- mostrar la lista completa')
    print('5.- mostrar el tamaño de la lista')
    print('0.- salir')
    print(sep)
    print('')

    choice = get_option()

    print(sep)
    print('')
    
    ll_options =  {
        1: _insert_choice,
        2: _remove_choice,
        3: _search_choice,
        4: _display_choice,
        5: _size_choice,
      }

    ll_option = ll_options.get(choice, lambda x: 'Opción no valida.')
    
    ll_option(ll)
    print(sep)


def sub_menu_linked_list_singly():  
  ll = LinkedListLinearSingly()
  create_sub_menu_linked_list(ll)



def _insert_choice(ll):
  print('agregar un nuevo nodo')
  print('')
  print(sep)
  print('Selecciona una estrategia para insertar el nuevo nodo')
  print(sep)
  print('')
  print('1.- push / insertar al principio')
  print('2.- insert after / insertar despues de un nodo en particular')
  print('3.- append / insertar al final de la lista')
  print('0.- atras')
  print(sep)
  print('')

  choice = get_option()
  
  new_key = None
  print('')
  print(sep)
  if choice == 1:
    print('push')
    print('')
    d = int(input('Ingrese un numero a almacenar:\t'))

    new_key = ll.push(d)

  elif choice == 2:
    print('insert after')
    print('')

    d = int(input('Ingrese un numero a almacenar:\t'))
    key = int(input('Ingrese el id de un nodo ya existente:\t'))

    try:
      new_key = ll.insert(d, key)
    except ValueError as e:
      print(e)

  elif choice == 3:
    print('append')
    print('')

    d = int(input('Ingrese un numero a almacenar:\t'))

    new_key = ll.append(d)
  
  else:
    print('Opción no valida.')
    return
  print('')
  print('ID del nuevo nodo: {}'.format(new_key))

def _remove_choice(ll):
  print('eliminar un nodo')
  print('')
  
  key = int(input('Ingrese el id de un nodo ya existente:\t'))

  print('')
  try:
    ll.remove(key)
  except (IndexError, ValueError) as e:
    print(e)
  else:
    print('Nodo eliminado correctamente.')

def _search_choice(ll):
  print('buscar un nodo')
  print('')

  key = int(input('Ingrese el id de un nodo ya existente:\t'))

  print('')

  try:
    node = ll.search(key)
  except (IndexError, ValueError) as e:
    print(e)
  else:
    print(sep)
    print('Nodo encontrado!')
    print('')
    print(node)
    print('')

def _display_choice(ll):
  print('imprimir toda la lista')
  print('')

  try:
    for node in ll.display():
      print(node)
  except IndexError as e:
    print(e)

def _size_choice(ll):
  print('ver el tamaño de la lista')
  print('')

  print('El tamaño de la lista es: {}'.format(len(ll)))
