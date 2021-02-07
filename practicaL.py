from archivo import *
import os
import csv
import msvcrt
cargar = []
listado = []

def salir():
    despedida = """
    Carnet: 201801143
    Denisse Figueroa
    dennikyo@gmail.com
    Lenguajes Formales y de Programación
    """
    print(despedida)

def Cargar_Archivo():
    global cargar
    global listado

    datos = input("Escriba el nombre del archivo que desea cargar: ")
    archivo = open(datos, "r", encoding='UTF-8')
    linea = archivo.readlines()
    archivo.close()
    for i in linea:
        cargar = i.split("=")
        cargar = cargar[1].split(",")
        listado.append(Cargar_Archivos(name=cargar[0], num1=cargar[1], num2=cargar[2], num3=cargar[3], num4=cargar[4], num5=cargar[5], num6=cargar[6]))



def menu():
    menu = """
    1. Cargar Archivo
    2. Desplegar Listas
    3. Desplegar Búsquedas
    4. Desplegar Todas
    5. Desplegar Todas a Archivo
    6. Salir
    """
    print(menu)


inicio = 0
while inicio !=2:
    menu()
    inicio = int(input("Ingrese una opción: "))
    if inicio == 1:
        Cargar_Archivo()
    if inicio == 2:
        print("Desplegar Listas")
    if inicio == 3:
        print("Desplegar Búsquedas")
    if inicio == 4:
        print("Desplegar todas")
    if inicio == 5:
        print("Desplegar todas a archivo")
    if inicio == 6:
        salir()
        quit()


