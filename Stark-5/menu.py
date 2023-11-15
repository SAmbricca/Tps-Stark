from stark_funciones_05 import *
from data_stark import *

nombre_archivo_csv = 'data_05.csv'
nombre_archivo_json = 'heroes_05.json'

def stark_marvel_app(lista_principal: list):
    flag_normalizado = False
    while True:
        print(imprimir_menu_05())
        opcion = input("Ingrese una opcion entre 1 y 7: ")
        if opcion == "1":
            stark_normalizar_datos(lista_principal, "fuerza", "altura", "peso") #lo traje del stark 3
            flag_normalizado = True
        elif flag_normalizado == False:
            print("Primero debe normalizar los datos")
        elif flag_normalizado == True:
            match opcion:
                case "2":
                    generar_csv(nombre_archivo_csv, lista_principal)
                case "3":
                    leer_csv(nombre_archivo_csv)
                    orden_ascendente_clave_numerica(leer_csv(nombre_archivo_csv), 'altura')
                case "4":
                    generar_json(nombre_archivo_json, lista_principal, 'heroes')
                case "5":
                    leer_json(nombre_archivo_json, 'heroes')
                    orden_descendente_clave_numerica(lista_principal, 'peso')
                case "6":
                    accion = input('Escriba "ASC" si desea orden ascendente o "DESC" si desea orden descendente: ')
                    while accion != "ASC" and accion != "DESC":
                        accion = input('Escriba "ASC" si desea orden ascendente o "DESC" si desea orden descendente: ')
                    orden_ascendente_o_descendente_clave_numerica(lista_principal, 'fuerza', accion)
                case "7":
                    break
                case _:
                    print("Error, elija una opcion entre 1 y 7")

stark_marvel_app(lista_personajes)
