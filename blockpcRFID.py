import sys
import os
import serial
import time
import signal
import subprocess

def beep():
    os.system('play --no-show-progress --null --channels 1 synth .05 sine 1000')


def streamCardReader():
    ''' Devuelve el numero de la tarjeta '''
    ser = serial.Serial('/dev/ttyUSB0', 57600)
    while True:
        try:
            tarjeta = ser.readline().strip()
            beep()
            yield tarjeta
            time.sleep(.3)

        except:
            ser.close()
            del ser
            print('recuperandose de un error')
            time.sleep(1.5)
            ser = serial.Serial('/dev/ttyUSB0', 57600)
            print('continuar...')
            pass

def cardReader():
    ser = serial.Serial('/dev/ttyUSB0', 57600)
    try:
        tarjeta = ser.readline().strip()
        beep()
        time.sleep(1.0)
        return tarjeta
    except:
        del ser
        print('saliendose por error garrafal')

def card2File(cardNo, filename='currentCard.txt'):
    with open(filename,'w') as file:
        file.write(str(cardNo))
    return True

def get_pid(nombre):
    ''' devuelve el numero de proceso para nombre'''
    try:
        return subprocess.check_output(['pidof', nombre])
    except:
        return None

def lockScreen():
    ''' ejecuta el comando slock, que hace que se bloquee la pantalla '''
    p = subprocess.Popen('slock', shell=True)
    

def killProc(pid):
    ''' mata el proceso que le indiques '''
    try:
        os.kill(pid, signal.SIGKILL)
    except:
        pass




if __name__ == "__main__":

    for a in streamCardReader():
        a = a.decode()
        card2File(a)
        print(a)
        # Si existe el proceso slock hay que matarlo para desbloquear la pantalla
        if a == '8D4FEED5' and get_pid('slock'):
            pid = int(get_pid('slock'))
            killProc(pid)
        elif a == '8D4FEED5':
            lockScreen()

        time.sleep(1)
