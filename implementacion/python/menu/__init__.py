option_not_valid = lambda: 'Opción no válida.'
sep = '------------------------'


def get_option():
  choice = 1
  try:
    choice = int(input('opcion:\t'))
  except Exception:
    choice = 0
  finally:
    return choice

