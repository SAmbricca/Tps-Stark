from data_stark import *
import json
import codecs
import csv
from stark_funciones_03 import *

#1.1.
def validar_lista(lista:list) -> bool:
    if len(lista) > 0 and type(lista) == list:
        return True
    else:
        return False

def leer_archivo(nombre_archivo:str):
    try:
        with codecs.open(nombre_archivo, 'r', encoding='UTF-8') as archivo:  #con with no necesito cerrar archivos. Lo hace automaticamente. codecs es para codificar con UTF-8 
            contenido = archivo.read()
            return contenido
        
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró")
        return False
    except:
        print(f"Error al leer el archivo'{nombre_archivo}':")
        return False

#leer_archivo(nombre_archivo)

#1.2
def guardar_archivo(nombre_archivo:str, contenido:str):
    try:
        with codecs.open(nombre_archivo, 'w+', encoding='UTF-8') as archivo:
            archivo.write(contenido)
        print(f"Se creó el archivo: {nombre_archivo}")
        return archivo
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró")
        return False
    except:
        print(f"Error al crear el archivo: {nombre_archivo}:")
        return False

# contenido_guardar_archivo = 'prueba'
# guardar_archivo("prueba", contenido_guardar_archivo)

#1.3
def generar_csv(archivo_superheroes_csv:csv, lista_superheroes:list):
    if not validar_lista(lista_superheroes):
        return False
    primer_elemento = lista_superheroes[0]
    csv_string = ",".join(primer_elemento.keys()) + "\n"  #las keys de los diccionarios son iguales para cada elemento, por eso obtengo las keys del primer elemento
    
    for personaje in lista_superheroes:
        personaje['altura'], personaje['peso'], personaje['fuerza'] = str(personaje['altura']), str(personaje['peso']), str(personaje['fuerza'])
        csv_string += str(",".join(personaje.values()) + "\n")

    if guardar_archivo(archivo_superheroes_csv, csv_string):
        return True
    else:
        return False

#archivo_superheroes_csv = "heroes.csv"
#generar_csv(archivo_superheroes_csv, lista_personajes)

#1.4
def leer_csv(nombre_archivo_csv):
    try:
        with codecs.open(nombre_archivo_csv, 'r', encoding='UTF-8') as archivo:
            lector_csv = csv.DictReader(archivo)  #Funcion de csv que lee el archivo CSV y genera un diccionario por fila, utilizando las cabeceras del CSV como claves del dict
            lista_csv = []
            for fila in lector_csv:
                lista_csv.append(dict(fila))

            return lista_csv
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo_csv}' no se encontró.")
        return False
    except:
        print(f"Error al leer el archivo'{nombre_archivo_csv}':")
        return False

#leer_csv("data_05.csv")
#print(lista_personajes)

#1.5
def generar_json(nombre_archivo_a_guardar:json, lista_superheroes:list, nombre_lista:str):
    dict_json = {nombre_lista: lista_superheroes}
    
    with open(nombre_archivo_a_guardar, 'w') as archivo:
        json.dump(dict_json, archivo, indent=4)
    
    print(f"Se creó el archivo: {nombre_archivo_a_guardar}")

#generar_json("heroes.json", lista_personajes, "heroes")

#1.6
def leer_json(nombre_archivo, nombre_lista):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = json.load(archivo)
            lista_obtenida = contenido.get(nombre_lista)
            return lista_obtenida
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except:
        print(f"Error al leer el archivo'{nombre_archivo}':")
    return False

# lista_pjs = leer_json('heroes.json','heroes')
# print(lista_pjs)

#2.1
def orden_ascendente_clave_numerica(lista_heroes:list, clave:str):
    for i in range(len(lista_heroes)-1):
        for j in range(i+1, len(lista_heroes)):
            valor_i = float(lista_heroes[i][clave])
            valor_j = float(lista_heroes[j][clave])
            if valor_i > valor_j:
                aux = lista_heroes[i]
                lista_heroes[i] = lista_heroes[j]
                lista_heroes[j] = aux

    for personaje in lista_heroes:
        print(f'Nombre: {personaje["nombre"]}, {clave}: {personaje[clave]}')
# stark_normalizar_datos(lista_personajes, "fuerza", "altura", "peso")
# orden_ascendente_clave_numerica(lista_personajes, 'altura')

#2.2
def orden_descendente_clave_numerica(lista_heroes:list, clave:str):
    for i in range(len(lista_heroes)-1):
        for j in range(i+1, len(lista_heroes)):
            valor_i = float(lista_heroes[i][clave])
            valor_j = float(lista_heroes[j][clave])
            if valor_i < valor_j:
                aux = lista_heroes[i]
                lista_heroes[i] = lista_heroes[j]
                lista_heroes[j] = aux

    for personaje in lista_heroes:
        print(f'Nombre: {personaje["nombre"]}, {clave}: {personaje[clave]}')

#2.3
def orden_ascendente_o_descendente_clave_numerica(lista_heroes:list, clave:str, accion:str):
    if accion == 'ASC':
        orden_ascendente_clave_numerica(lista_heroes, clave)
    elif accion == 'DESC':
        orden_descendente_clave_numerica(lista_heroes, clave)


def imprimir_menu_05():
    mensaje = '''● 1-Normalizar datos
● 2-Generar CSV
● 3-Listar heroes del archivo CSV ordenados por altura ASC
● 4-Generar JSON
● 5-Listar heroes del archivo JSON ordenados por peso DESC
● 6-Ordenar Lista por fuerza (De manera Ascendente o Descendente)
● 7-Salir'''
    return mensaje
