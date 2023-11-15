from stark_funciones_04 import *
from data_stark import *

def stark_marvel_app(lista_principal: list):
    while True:
        print(imprimir_menu_04())
        opcion = input("Ingrese una opcion entre 1 y 6: ")
        match opcion:
            case "1":
                print(stark_imprimir_nombres_con_iniciales(lista_principal))
            case "2":
                imprimir_lista_de_nombres_y_codigos(lista_principal)
            case "3":
                stark_normalizar_datos(lista_principal)
            case "4":
                print(stark_imprimir_indice_nombre(lista_principal))
            case "5":
                stark_navegar_fichas(lista_principal)
            case "6":
                break
            case _:
                print("Error, elija una opcion entre 1 y 6")

stark_marvel_app(lista_personajes)
