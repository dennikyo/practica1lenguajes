import tkinter as tk
from tkinter import filedialog as arch
import os
import csv
import msvcrt
import webbrowser

file = ""


def salir():
    despedida = """
    Carnet: 201801143
    Denisse Figueroa
    dennikyo@gmail.com
    Lenguajes Formales y de Programación
    """
    print(despedida)

def cargar_archivo():
    global file 
    root = tk.Tk()
    root.withdraw()
    file = arch.askopenfilename()


def listas_ordenadas():
    open_file = open(file, 'r')
    lists_dictionary = Organizer().file_reading(open_file)
    data = ""
    for key,v in lists_dictionary.items():
        if v["ORDENAR"] == True:
            data_list = v["data_list"].split(",")
            for i in range(len(data_list)):
                least = i
                for k in range(i+1, len(data_list)):
                    if int(data_list[k]) < int(data_list[least]):
                        least = k

                ordenar_temp = data_list[least]
                data_list[least] = data_list[i]
                data_list[i] = ordenar_temp

            data += key + ": ORDENADOS=" + ",".join(data_list) + "\n"
    data = data[:-1]
    return data

def buscar_listas():
    open_file = open(file, 'r')
    lists_dictionary = Organizer().file_reading(open_file)
    data2 = ""
    for key,v in lists_dictionary.items():
        if v["BUSCAR"] is not False:
            contador = 0
            a = ""
            data_list = v["data_list"].split(",")
            for n in data_list:
                if v["BUSCAR"] == n:
                    a += str(contador) + ","
                contador +=1
            if a != "":
                a = a[:-1]
            else:
                a = "NO ENCONTRADO"
            listado = ",".join(data_list)
            data2 += key+":"+listado+" BUSQUEDA POSICIONES = "+a+ "\n"
    data2 = data2[:-1]
    return data2
                    


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
        return list_1        


def found():
    ordenadas = listas_ordenadas()
    buscadas = buscar_listas()
    return ordenadas + "\n" + buscadas
    

def html_file():
    complete = found()
    print(complete)
    fixi = ""
    for g in found().split("\n"):
        fixi += '<li class="gato">' + g + '</li>\n'
    
    f = open('archivo.html', 'w')
    message = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {background-color: powderblue;}
    h1   {color: rgb(106, 158, 236);}
    p    {color: rgb(153, 0, 255);}
    </style>
        </head><h1></h1>
        <body>
        <ul class="miau">"""
    message += fixi 
    message += """>/ul>
    
        <p></p>

    </body>
    </html>
    """

    f.write(message)
    f.close()
    webbrowser.open_new_tab('archivo.html') 
    return complete
               


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
        lo = listas_ordenadas()
        print(lo)
    if inicio == 3:
        print("Desplegar Búsquedas")
        bu =buscar_listas()
        print(bu)
    if inicio == 4:
        print("Desplegar todas")
        print("Búsquedas -------------------------")
        print(buscar_listas())
        print("Ordenadas -------------------------")
        print(listas_ordenadas())
    if inicio == 5:
        print("Desplegar todas a archivo")
        go = html_file()
        print(go)
       
    if inicio == 6:
        salir()
        quit()


