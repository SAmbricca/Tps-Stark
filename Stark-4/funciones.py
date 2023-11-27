from data_stark import *
import re

def validar_str(string):
    if string != "" and type(string) == str:
        return True
    else:
        return False

def validacion_int_float(dato:str) -> bool:
    if type(dato) == int or type(dato) == float:
        return True
    else:
        return False
    
def validar_dict_con_nombre(diccinario):
    if type(diccinario) == dict and 'nombre' in diccinario:
        return True
    else:
        return False 
    
def validar_lista(lista:list) -> bool:
    if len(lista) > 0 and type(lista) == list:
        return True
    else:
        return False
    
def validar_genero(string):
    if string == "M" or string == "F" or string == "NB":
        return True
    else:
        return False

#1.1 Crear la funcion 'extraer_iniciales'    
def extraer_iniciales(nombre_heroe:str):
    if not validar_str(nombre_heroe):
        return "N/A"

    if '-' in nombre_heroe:
        nombre_heroe = nombre_heroe.replace("-", " ")

    palabras = re.findall(r'\b(?!the\b)\w', nombre_heroe) #findall(r'\b(?!the\b)\w') es una expresion regular (regex) que busca todas las palabras que no coincidan con 'the'
    lista_iniciales = []
    for palabra in palabras:
        lista_iniciales.append(palabra[0].upper())
    
    if lista_iniciales:
        iniciales_str = '.'.join(lista_iniciales) + '.'
        return iniciales_str

#print(extraer_iniciales('Spider-Man'))

#1.2 formato snake_case. palabras en minusculas separadas por guiones bajos. por ej, edad_del_personaje
def obtener_dato_formato(dato_especifico: str):
    if not validar_str(dato_especifico):
        return False
    
    dato_snake_case = re.sub(r'\s+', '_', dato_especifico.lower())  #\s es una secuencia de regex que busca espacios en blanco. re.sub reemplaza \s por '_'
    
    return dato_snake_case

#print(obtener_dato_formato("Howard the Duck"))
#1.3
def stark_imprimir_nombre_con_iniciales(dict_heroe: dict):
    if not validar_dict_con_nombre(dict_heroe):
        return False
    
    iniciales = extraer_iniciales(dict_heroe["nombre"])
    dato_snake_case = obtener_dato_formato(dict_heroe["nombre"])

    retorno = '* ' + dato_snake_case + f' ({iniciales})'

    return retorno

# dict_howard = lista_personajes[0]
# print(stark_imprimir_nombres_con_iniciales(dict_howard))

#1.4
def stark_imprimir_nombres_con_iniciales(lista_heroes: list):
    if not validar_lista(lista_heroes):
        return False
    
    retorno = ""
    for personaje in lista_heroes:
        retorno += stark_imprimir_nombre_con_iniciales(personaje) + "\n"
    
    return retorno

#print(stark_imprimir_nombres_con_iniciales(lista_personajes))

#2.1
def generar_codigo_heroe(dict_heroe: dict, id: int):
    if 'genero' not in dict_heroe or not validar_genero(dict_heroe["genero"]) or id > 9999999: #maximo numero de 7 digitos
        return 'N/A'
    
    if dict_heroe['genero'] == 'M':
        primer_numero = 1
        relleno_id = str(id).zfill(7)[:7]
        codigo_heroe = f'M-{primer_numero}{relleno_id}'

    elif dict_heroe['genero'] == 'F':
        primer_numero = 2
        relleno_id = str(id).zfill(7)[:7]
        codigo_heroe = f'F-{primer_numero}{relleno_id}'

    else:
        relleno_id = str(id).zfill(7)[:7]
        codigo_heroe = f'NB-{relleno_id}'
    
    return codigo_heroe

# dict_thor = lista_personajes[9]
# print(generar_codigo_heroe(dict_thor, 3214))

#2.2
def stark_generar_codigos_heroes(lista_heroes: list):
    if not validar_lista(lista_heroes):
        return False
    
    string_codigos = ""
    cantidad_generada = ""
    for i in range(len(lista_heroes)):
        if not validar_dict_con_nombre(lista_heroes[i]):
            return False
        string_codigos += "\n" + stark_imprimir_nombre_con_iniciales(lista_heroes[i]) + " | "
        string_codigos += generar_codigo_heroe(lista_heroes[i], i)
        cantidad_generada = cantidad_generada + "#"
    print(string_codigos)
    print("---------------------------------------------")
    print(f'Se asignaron {cantidad_generada} códigos')

    return string_codigos, cantidad_generada

#stark_generar_codigos_heroes(lista_personajes)

#3.1
def sanitizar_entero(numero_str: str):
    numero_str = numero_str.strip() #.strip elimina los caracteres especificados (por defecto, espacios en blanco) tanto al principio y al final del string
    try:
        numero_entero = int(numero_str)
        if numero_entero < 0:
            return -2
        else:
            return numero_entero
    except ValueError:  #ValueError verifica la conversion de un dato al valor esperado, es decir, al volverlo un int, verifica que solo tenga caracteres de int
        return -1
    except:             #Caulquier otro error al convertir
        return -3
    
#3.2
def sanitizar_flotante(numero_str: str):
    numero_str = numero_str.strip() 
    try:
        numero_entero = float(numero_str)
        if numero_entero < 0:
            return -2
        else:
            return numero_entero
    except ValueError:  
        return -1
    except:             
        return -3
    
#3.3
def sanitizar_string(valor_str: str, valor_por_defecto = '-'):
    if valor_str == "" and valor_por_defecto:
        return valor_por_defecto.lower()

    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    for letra in valor_str:
        if letra.isdigit():
            return 'N/A'
    
    valor_str = valor_str.replace('/', ' ') #Lo realizo despues del for para no generar inconvenientes

    return valor_str.lower()

#3.4
def sanitizar_dato(dict_heroe: dict, clave: str, tipo_dato: str):
    if not validar_str(tipo_dato) or (tipo_dato.lower() != "entero" and tipo_dato.lower() != "flotante"):
        return "Tipo de dato no reconocido"
    
    if clave not in dict_heroe:
        return "La clave especificada no existe en el héroe"
    
    retorno = False
    if tipo_dato.lower() == "string":
        sanitizar_string(clave)
        retorno = True
    elif tipo_dato.lower() == "entero":
        sanitizar_entero(clave)
        retorno = True
    elif tipo_dato.lower() == "flotante":
        sanitizar_flotante(clave)
        retorno = True
    
    return retorno

#3.5
def stark_normalizar_datos(lista_heroes: list):
    if not validar_lista(lista_heroes):
        return print("Error: Lista de héroes vacía")
    
    for personaje in lista_heroes:
        sanitizar_dato(personaje, personaje['altura'], "flotante")
        sanitizar_dato(personaje, personaje['peso'], "flotante")
        sanitizar_dato(personaje, personaje['color_ojos'], "string")
        sanitizar_dato(personaje, personaje['color_pelo'], "string")
        sanitizar_dato(personaje, personaje['fuerza'], "entero")
        sanitizar_dato(personaje, personaje['inteligencia'], "string")
    
    print("Datos normalizados")

#4.1
def stark_imprimir_indice_nombre(lista_heroes: list):
    indice_nombre = ""

    for personaje in lista_heroes:
        palabras = re.findall(r'\b(?!the\b)\w+', personaje['nombre']) #A diferencia de la funcion extraer_iniciales(), agregue un '+' al final de la expresion r'\b(?!the\b)\w+' para quedarme con todo el nombre
        indice_nombre += '-'.join(palabras) + '-'
    
    indice_nombre = indice_nombre.rstrip('-') #Analogo a strip pero solo con el ultimo caracter
    return indice_nombre

#print(stark_imprimir_indice_nombre(lista_personajes))

#5.1
def generar_separador(patron: str, largo: int, imprimir = True):
    if not validar_str(patron) or len(patron) < 1 or len(patron) > 2 or not validacion_int_float(largo) or (largo < 1 or largo > 235):
        return "N/A"
    separador = ""
    for i in range(largo):
        separador += patron
    
    if imprimir:
        return print(separador)
    else:
        return separador

#generar_separador('*', 10)

#5.2
def generar_encabezado(titulo: str):
    if not validar_str(titulo):
        return False
    
    encabezado = f"{generar_separador('*', 60, False)}\n{titulo.upper()}\n{generar_separador('*', 60, False)}"
    return encabezado

#generar_encabezado("Principal")

#5.3
def imprimir_ficha_heroe(dict_heroe: dict, id):
    if not validar_dict_con_nombre(dict_heroe):
        return False
    
    nombre = dict_heroe['nombre'].lower()
    identidad = dict_heroe['identidad'].lower()
    identidad = identidad.replace(" ", "_")
    consultora = dict_heroe['empresa'].lower()
    consultora = consultora.replace(" ", "_")
    codigo = generar_codigo_heroe(dict_heroe, id)

    altura = '{:.0f}'.format(float(dict_heroe['altura'])) + " cm."
    peso = '{:.2f}'.format(float(dict_heroe['peso'])) + ' kg.'
    fuerza = dict_heroe['fuerza'] + " N"

    ficha_heroe = f"{generar_encabezado('Principal')}\n      NOMBRE DEL HÉROE:            {nombre} ({extraer_iniciales(dict_heroe['nombre'])})\n      IDENTIDAD SECRETA:           {identidad}\n      CONSULTORA:                  {consultora}\n      CÓDIGO DE HÉROE:             {codigo}\n{generar_encabezado('FISICO')}\n      ALTURA:                      {altura}\n      PESO:                        {peso}\n      FUERZA:                      {fuerza}\n{generar_encabezado('señar particulares')}\n      COLOR DE OJOS:               {dict_heroe['color_ojos']}\n      COLOR DE PELO:               {dict_heroe['color_pelo']}"

    return ficha_heroe

#print(imprimir_ficha_heroe(lista_personajes[5]))

#5.5
def stark_navegar_fichas(lista_heroes: str):
    if not validar_lista(lista_heroes):
        return False
    iteracion = 0
    id = 1
    while True:
        print(imprimir_ficha_heroe(lista_heroes[iteracion], id))
        opcion = input("\nIngrese alguna de las siguientes opciones:\n[1] Ir a la izquierda      [2] Ir a la derecha     [3] Salir\nOpcion:")
        while opcion != "1" and opcion != "2" and opcion != "3":
            opcion = input("\nIngrese alguna de las siguientes opciones:\n[1] Ir a la izquierda      [2] Ir a la derecha     [3] Salir\nOpcion:")
        if opcion == "1":
            if iteracion == 0:
                iteracion = len(lista_heroes) - 1
                id = len(lista_heroes)
            else:
                iteracion -= 1
                id -= 1
        elif opcion == "2":
            if iteracion == len(lista_heroes) - 1:
                iteracion = 0
                id = 1
            else:
                iteracion += 1
                id += 1
        elif opcion == "3":
            break
        print(iteracion)
        
#stark_navegar_fichas(lista_personajes)

def imprimir_menu_04():
    mensaje = '''1 - Imprimir la lista de nombres junto con sus iniciales
2 - Imprimir la lista de nombres y el código del mismo
3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
6 - Salir'''
    return mensaje
            
#EXTRAS

def imprimir_lista_de_nombres_y_codigos(lista_heroes):
    retorno = ""
    id = 1
    for personaje in lista_heroes:
        retorno += f'{personaje["nombre"]}-{generar_codigo_heroe(personaje, id)}\n'
        id += 1

    return print(retorno)
