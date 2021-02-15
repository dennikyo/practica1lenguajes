import tkinter as tk
from tkinter import filedialog as arch
import os
import csv
import msvcrt



def salir():
    despedida = """
    Carnet: 201801143
    Denisse Figueroa
    dennikyo@gmail.com
    Lenguajes Formales y de Programación
    """
    print(despedida)

def cargar_archivo():
    root = tk.Tk()
    root.withdraw()
    file = arch.askopenfilename()
    open_file = open(file, 'r')
    Organizer().file_reading(open_file)

class Organizer:
    def file_reading(self,document):
        list_1 ={}
        for espace in document:
            options = {}
            name_options = espace.split("=")[0]
            better_list = espace.split("=")[1]

            if "ORDENAR" in better_list:
                options["ORDENAR"] = True

                if "BUSCAR" not in better_list:
                    options["BUSCAR"] = False
                    left_list = better_list.split("ORDENAR")[0]
                    options["data_list"] = "".join(left_list.split())
                else:
                    left_list = better_list.split("ORDENAR")[0]
                    if "BUSCAR" in left_list:
                        options["data_list"] = "".join(left_list.split("BUSCAR")[0].split())
                        options["BUSCAR"] = "".join(left_list.split("BUSCAR")[1].split())
                    else:
                        right_list = better_list.split("ORDENAR")[1]
                        options["data_list"] = "".join(left_list.split())
                        options["BUSCAR"] = "".join(right_list.split("BUSCAR")[1].split())

            else:
                options["ORDENAR"] = False
                if "BUSCAR" in better_list:
                    left_list = better_list.split("BUSCAR")[0]
                    right_list = better_list.split("BUSCAR")[1]
                    options["data_list"] = "".join(left_list.split())
                    options["BUSCAR"] = "".join(right_list.split())
                
            if options["BUSCAR"] != False:
                if options["BUSCAR"][(len(options["BUSCAR"]))-1] == ",":
                    options["BUSCAR"] = options["BUSCAR"][:-1]

            
            
            list_1[name_options] = options
        print(list_1)            




                    


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
        cargar_archivo()
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


