#!/usr/bin/env python3

def leerSwitch():
    ''' Devuelve True si el contenido del archivo switch.txt es 1 si no False '''

    with open('switch.txt', 'r') as switch:
        try:
            status = int(switch.read())
        except:
            return False
    if status == 1:
        return True
    else:
        return False
