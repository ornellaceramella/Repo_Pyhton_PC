import re
import json
import csv
import os



def limpiar_consola () -> None:
    """
    Espera a que el usuario presione enter y vacia la consola
    """

    _ = input("Presione una tecla para continuar")
    os.system("cls")

def imprimir_dato(dato:str):
    """
    La funcion "imprimir_dato" comprueba si la entrada en una cadena de texto y la imprime,
    de lo contrario imprime un mensaje advirtiendo que no es una cadena lo que se ingreso.
    """
    if (type(dato)== str):
        print(dato)
    else:
        print("No es una cadena de texto")

def validar_respuesta(expresion: str, ingreso_usuario: str) -> str:
    """
    Esta funcion valida que la opcion ingresada sea correcta
    """
    respuesta_validada = False
    if re.match(expresion, ingreso_usuario):
        respuesta_validada =int(ingreso_usuario)

    return respuesta_validada



def mostrar_menu()-> None:
    menu= '''\n\t------------------- Menu---------------------------------------\n
    
    0. SALIR
    1. Mostrar los jugadores y su respectiva posicion
    2. Mostrar estadisticas de jugador
    3. Guardar el jugador seleccionado en el punto 
    4. Buscar jugadore por nombre y mostrar sus logros
    5. Calcular y mostrar el promedio de puntos por partido del DT
    6. Ingresar un jugador y mostrar si es miembro del Salon de la Fama
    7. Calcular y mostrar el jugadore con mayor cantidad de rebotes
    8. Calcular y mostrar con el mayor porcentaje de tiros de campo
    9. Calcular y mostrar el jugador con mayor cantidad de asistencias
    10. Ingresar un valor y calcular los jugadores que han promediado mayor cantidad de puntos por partido que ese valor
    11. Ingresar un valor y calcular los jugadores que han promediado mas rebotes por partido que ese valor
    12. Ingresar un valor y calcular los jugadores que han promediado mas asistencias por partido que ese valor 
    13. Mostrar el jugador con mas robos totales
    14. Mostrar el jugador con mas bloqueos totales
    15. Ingresar un valor y calcular los jugadores que tienen un porcentaje de tiros libres superior a ese valor
    16. Mostrar el promedio de puntos por partido del DT excluyendo al jugador con la menor cantidad de puntos por partido
    17. Mostrar el jugador con la mayor cantidad de logros obtenidos
    18. Ingresar un valor y calcular los jugadores que tienen un porcentaje de tiros triples superior a ese valor
    19. Mostrar el jugador con la mayor cantidad de temporadas jugadas
    20. Ingresar un valor y mostrar los jugadores, ordenados por su posicion en cancha, que hayan obtenido un porcentaje de tiros de campo mayor a ese valor
    '''
    imprimir_dato(menu)

def dream_team_menu_principal(): 
    '''
    imprime el menu y toma una opcion del usuario
    devuelve la opcion elegida, en caso de False devuelve -1
    '''
    mostrar_menu()
    opcion = input("Ingresa una opción del menú: ").upper()
    validacion = re.match( r'^[1]?[0-9]{1}$|20|23', opcion)
    if validacion:
        return True
    else:
        return False
       
def validar_numeros(dato:str):
    """
    valida si el dato pasado es numerico, y si lo es lo convierte en int o float
    recibe un str
    retorna un int o float en caso de ser numerico, si no lo es retorna False
    """
    if re.match(r"^\d+(\.\d+)?$", dato):
        try:
            return int(dato)
        except Exception as error:
            return float(dato)
    else:
        return False

def leer_json (ruta:str, encoding='utf-8'):
    with open (ruta, "r") as archivo:
        data= json.load(archivo)
        lista_jugadores = data["jugadores"]
    
    return lista_jugadores

    
def mostrar_jugadores_dt (lista_jugadores: list): #1
    """
    
    Recibe por parametro una lista con el formato del JSON trabajado, retorna 0 si la lista está vacía. 
    De lo contrario, pide al usuario que ingrese el índice de un jugador en la lista, y valida que este sea mayor a
    0 y menor o igual a la cantidad de elementos de la lista. Retorna al jugador y su posicion segun el indice
    
    """
    cantidad_jugadores= len(lista_jugadores)
    if cantidad_jugadores<= 0:
        return 0
    for jugador in lista_jugadores:
        print("{} - {}".format(jugador["nombre"], jugador["posicion"]))




def obtener_nombre_estadisticas(lista_jugadores:list[dict])-> dict:
    """
    Esta funcion toma una lista de diccionarios que representan a los jugadores y un indice, recupera al
    al jugador en ese indice, imprime su nombre y estadisticas y devuelve el diccionario que representa a ese jugador.

    """
    if lista_jugadores:

        indice = input("Seleccione un jugador por su indice para ver sus caracteristicas: ")
        indice = validar_respuesta(r'^[0-9]{1,2}$', indice)

        if indice >= 0 and indice < len(lista_jugadores):
            jugador_con_ese_indice = lista_jugadores[indice]
            
            dic_estadisticas = {}
            dic_estadisticas = jugador_con_ese_indice["estadisticas"]

            print(jugador_con_ese_indice["nombre"])
            
            for clave, valor in dic_estadisticas.items():
                print(clave, valor)
        else:
            print("El indice es incorresto {0}".format(indice))
    
    return jugador_con_ese_indice

#3
def generar_texto(dicc_jugador: dict)-> str:
    """
    Esta funcion toma un diccionario de las estadisticas de un jugador y devuelve una cadena formateada
    que contiene su nombre, posicion y estadisticas
    """
    jugador_indice = dicc_jugador
    jugador_estadisticas = jugador_indice["estadisticas"]
    nombre_posicion = "{0}, {1}".format(jugador_indice["nombre"],  jugador_indice["posicion"])

    lista_claves = ["nombre", "posicion"]
    lista_valores =[]

    for clave, valor in jugador_estadisticas.items():
        lista_claves.append(clave)
        lista_valores.append(str(valor))
    
    claves_str = ",".join(lista_claves)
    valores_str = ",".join(lista_valores)
    
    datos_str = "{0}\n{1}, {2}".format(claves_str, nombre_posicion, valores_str)
    return datos_str



def guardar_estadisticas_jugador_CSV(nombre_archivo:str, contenido:str)-> bool:
    """
    Esta funcion guarda el contenido de una cadena de un archivo con el nombre de archivo dado y
    devuelve un valor booleano que indica si la operacion fue exitosa o no
    """
    with open(nombre_archivo, "w+") as archivo:
        resultado = None
        resultado = archivo.write(contenido)
    if resultado:
        print("Se creo el archivo: {0}".format(nombre_archivo))
        return False
    
    print("Error al crear el archivo: {0}".format(nombre_archivo))
    return False
    

def buscar_por_nombre(lista_jugadores:list[dict], jugador: dict, nombre: str):
    """
    Esta funcion busca a traves de RegEx la coincidencia entre el paramtro "nombre" y 
    el nombre pasado como parametro
     
    parametros:
    lista_jugadores : list[dict]-> la lista original que se importo del JSON
    busqueda : tipo match.object  | null-> el resultado del re.match utilizado
    """
    if len(lista_jugadores) == 0:
        print("La lista esta vacia")
        return -1
    if nombre == " ":
        print("Ingrese un nombre valido")

    else:
        busqueda = re.search(f'{nombre}', jugador["nombre"], re.I)
        return busqueda
    

#4
def mostrar_logros_por_busqueda(lista_jugadores: list[dict], nombre: str):
    """
    """
    if len(lista_jugadores) == 0:
        print("Lista vacia")
        return False
    if nombre == " ":
        print("Ingrese un nombre valido")

    else:
        lista = lista_jugadores
        flag_jugador = False
        for jugador in lista:
            busqueda =  buscar_por_nombre(lista_jugadores, jugador, nombre) 
            if busqueda:
                flag_jugador = True
                print(jugador["nombre"] + "\n")
                for logro in jugador["logros"]:
                    print("- " + logro + "\n")
        if flag_jugador == False:
            print("No existe jugador con ese nombre")



def mostrar_estadistica_por_jugador_ordenado(lista_jugadores : list[dict], key_orden : str, estadistica: str):
    """
    Esta función toma una lista de diccionarios que contienen información del jugador, la ordena según
    una clave determinada y muestra el nombre del jugador y una estadística específica para cada
    jugador.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus estadísticas
    :type lista_jugadores: list[dict]
    :param key_orden: La clave por la que se ordenará la lista de jugadores
    :type key_orden: str
    :param estadistica: El parámetro "estadistica" es una cadena que representa la estadística
    específica que queremos mostrar para cada jugador en la lista. Se utiliza para acceder al valor
    correspondiente en el diccionario "estadisticas" del diccionario de cada jugador de la lista
    :type estadistica: str
    :return: una lista de listas, donde cada lista interna contiene el nombre de un jugador y su valor
    correspondiente para la estadística especificada. Sin embargo, la función también tiene una
    declaración condicional que devuelve False si la lista de entrada está vacía.
    """
    """
    Esta funcion muestra un listado ordenado segun "key_orden", del nombre de los jugadores
    junto a la estadistica pasada por param. 
    """   
    if len(lista_jugadores) == 0:
        print("Lista vacia")
        return False
    lista_aux = lista_jugadores[:]
    lista = ordenar_lista_segun_key(lista_aux, key_orden)
    lista_jugador_nombre = []
    for jugador in lista:
        lista_jugador_nombre.append([jugador["nombre"], jugador["estadisticas"][estadistica]])
    estadistica_str = estadistica.replace("_"," ").capitalize()
    for jugador in lista_jugador_nombre:
        mensaje = "Jugador: {0}\n{1}: {2}\n".format(jugador[0], estadistica_str, jugador[1])
        print(mensaje)
    return lista_jugador_nombre


def imprimir_datos_jugadores_salon(lista_jugadores: list[dict])-> None: #6
    """   
    La función recorre la lista de jugadores y verifica si cada jugador tiene el logro 
    "Miembro del Salon de la Fama del Baloncesto". Si es así, imprime el nombre del jugador y el logro. 
    Si ningún jugador tiene ese logro, se muestra un mensaje indicando que el jugador no pertenece al Salón de la
    Fama del Baloncesto.
    """
    if lista_jugadores:
        for jugador in lista_jugadores:
            logros = jugador["logros"]
            flag = True
            for logro in logros:
                if "Miembro del Salon de la Fama del Baloncesto" == logro:
                    print(jugador["nombre"], logro)
                    flag = False
            if flag:
                print("el jugador no pertenece al salon de la fama")
    else:
        print("No se encontraron jugadores que coincidan con el parámetro de búsqueda.")


def encontrar_maximo(lista_jugadores:list[dict], clave_jugador:str, clave_valor:str)-> str:
    """
    Esta funcion encuentra el valor maximo de una clave especifica en la lista de jugadores y devuelve
    el nombre del jugador que tiene ese valor maximo, junto con el valor mismo, en forma de cadena de texto
    """                     
    nombre_maximo = None
    maximo = 0
    if lista_jugadores:
        for jugador in lista_jugadores:
            valor = jugador[clave_jugador][clave_valor]
            if nombre_maximo == None or valor > maximo:
                maximo = valor
                nombre_maximo = jugador["nombre"]
        clave_valor = clave_valor.replace("_"," ")
    if nombre_maximo:
        mensaje = "El jugador {0} tiene la mayor cantidad de {1}: {2}.".format(nombre_maximo, clave_valor, maximo)
    return mensaje

def mostrar_jugadores_promediado_mas_stat(lista_jugadores:list[dict], estadistica: str, valor_stat: float, flag_mostrar_posicion: False ):
    """
    Esta funcion muestra los jugadores que superen el valor de la estadistica deseada.
    """
    if len(lista_jugadores) == 0:
        print("Lista vacia")
        return False
    lista = lista_jugadores[:]
    estadistica_str = estadistica.replace("_"," ")
    lista_jugadores_prom_mayor = []
    for jugador in lista:
        if jugador["estadisticas"][estadistica] > valor_stat:
            lista_jugadores_prom_mayor.append([jugador["nombre"], jugador["estadisticas"][estadistica], jugador["posicion"]])
        if not lista_jugadores_prom_mayor:
            print("Ningun jugador posee un mayor valor que el ingresado en {0}",format(estadistica_str))
        else:
            mensaje = "\nValor Ingresado: {0}\nJugadores que superar ese valor en {1}:\n".format(valor_stat, estadistica_str)
            for jugador in lista_jugadores_prom_mayor:
                if flag_mostrar_posicion == False:
                    mensaje += "{0} - {1}\n".format(jugador[0], jugador[2], jugador[1])
            print(mensaje)
            return lista_jugadores_prom_mayor
    
def ordenar_lista_segun_key(lista_jugadores: list[dict], key_a_ordenar : str, flag_estadistica = False, orden_ascendente = True)-> list:
    """
    Esta funcion genera una lista ordenada segun param "key_a_odenar" a traves de un metodo de ordenamiento
    """
    if len(lista_jugadores)== 0:
        print("Lista vacia")
        return False
    lista = lista_jugadores[:]
    rango_a = len(lista)
    flag_swap = True
    contador = 0
    while flag_swap:
        flag_swap = False
        for indice_A in range(rango_a -1):
            contador += 1
            if flag_estadistica == False:
                if orden_ascendente == True:
                    if lista[indice_A][key_a_ordenar] > lista[indice_A+1][key_a_ordenar]:
                        lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                        flag_swap = True
                elif orden_ascendente == False:
                    if lista[indice_A][key_a_ordenar] < lista[indice_A+1][key_a_ordenar]:
                        lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                        flag_swap = True
            elif flag_estadistica == True:
                if orden_ascendente == True:
                    if lista[indice_A]["estadisticas"][key_a_ordenar] > lista[indice_A+1]["estadisticas"][key_a_ordenar]:
                        lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                        flag_swap = True
                elif orden_ascendente == False:
                    if lista[indice_A]["estadisticas"][key_a_ordenar] < lista[indice_A+1]["estadisticas"][key_a_ordenar]:
                        lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                        flag_swap = True
    return lista
    
def generar_promedio_segun_stat_menos_peor_valor(lista_jugadores:list[dict], estadistica: str):
    """
    Esta funcion genera el promedio de la suma de la estadistica elegida, sin tener en cuenta el stat del jugador que 
    peor promedia
    """
    if len(lista_jugadores) == 0:
        print("Lista vacia")
        return False
    lista_aux = lista_jugadores[:]
    contador = 0
    acumulador = 0
    if estadistica in lista_aux[0]["estadisticas"].keys():
        lista_ordenada = ordenar_lista_segun_key(lista_aux, estadistica, True, False)
        lista_ordenada.pop()
        for jugador in lista_ordenada:
            acumulador += jugador["estadisticas"][estadistica]
            contador += 1
        promedio = acumulador / contador
        return promedio
    else:
        print("Estadistica inexistente")

def jugador_mas_logros(lista_jugadores:list[dict])-> dict:
    """
    Calcula el jugador con mas logros en su carrera
    recibe la lista de jugadores
    retorna el jugador con mas logros obtenidos(dict)
    crea una copia de la lista original, recorre los logros de cada jugador, si el logro tiene un año, 
    se incrementa el contador 
    """
    lista_de_jugadores = lista_jugadores[:]

    acumulador_logros = 0
    logros_jugadores = []
    logros_jugadores_sin_indices = []

    for jugador in lista_de_jugadores:
        for logro in jugador["logros"]:
            patron_cuatro_digitos = r"\d{4}"
            if re.search(patron_cuatro_digitos, logro):  # si hay un año en el logro entra
                acumulador_logros += len(re.findall(patron_cuatro_digitos, logro))  # busca esos años, y el len va a indicar cuantos son y se suman al acumulador
            elif "Miembro" in logro:
                acumulador_logros += 1
            else:
                patron = r"\d{3}"
                if re.match(patron, logro): # si el logro empieza con 1 o 2 digitos entra.
                    acumulador_logros += int(re.findall(patron, logro)[0]) # trae el numero de cada logro, lo parsea y lo suma al acumulador
        logros_jugadores.append(lista_de_jugadores.index(jugador)) # agrego el indice del jugador de la lista real
        logros_jugadores.append(acumulador_logros) # agrego la cantidad de logros que tenga  ese jugador
        logros_jugadores_sin_indices.append(acumulador_logros) # lista aparte solo con logros
        
        acumulador_logros = 0
    for indice in range(len(logros_jugadores_sin_indices)): # recorro segun el largo de la lista de solo logros
        if indice == 0 or float(logros_jugadores_sin_indices[maximo_indice]) < float(logros_jugadores_sin_indices[indice]):
            maximo_indice = indice
            numero_maximo = logros_jugadores_sin_indices[maximo_indice]
    indice_jugador_mas_logros = logros_jugadores[logros_jugadores.index(numero_maximo) -1] # dentro del [] obtiene el indice anterior del numero_maximo,
                                                                                           # que seria el indice del jugador en la listaoriginal. al ser jordan da 0
                                                                        # y los logros_jugadores[x] te da la posicion real del json del jugador con mas logros
    return lista_de_jugadores[indice_jugador_mas_logros]

def jugador_mas_temporadas(jugadores:list[dict])-> None:
    """
    Esta funcion encuentra al jugador(es) con la mayor cantidad de temporadas jugadas en base a una
    lista de dicc de jugadores y los imprime uno a la vez junto con su cantidad de temporadas
    (como cuando sacamos un max o min, compara el maximo en cada vuelta con el valor de temporadas que encuentra)
    """
    max_temporadas = 0
    jugadores_max_temporadas = []

    for jugador in jugadores:
        temporadas = jugador["estadisticas"]["temporadas"]
        if temporadas > max_temporadas:
            max_temporadas = temporadas
            jugadores_max_temporadas = [(jugador["nombre"], temporadas)]
        elif temporadas == max_temporadas:
            jugadores_max_temporadas.append((jugador["nombre"], temporadas))
    print("Jugadores con la mayor cantidad de temporadas jugadas:")
    for jugador, temporadas in jugadores_max_temporadas:
        print("Jugador: {} | Temporadas: {}".format(jugador, temporadas))


    
def determinar_cant_jugadores_por_posicion(lista_de_jugadores:list):
    
    cantidad_jugadores_por_posicion = {}
    for jugador in lista_jugadores:
        posicion = jugador["posicion"]

        if posicion in cantidad_jugadores_por_posicion:
            cantidad_jugadores_por_posicion[posicion] += 1
        else:
            cantidad_jugadores_por_posicion[posicion] = 1

    return cantidad_jugadores_por_posicion

def mostrar_lista_jugadores_cantidad_All_Star_descendente(lista_jugadores):
    pass
# La salida por pantalla debe tener un formato similar a este:
# Michael Jordan (14 veces All Star)
# Magic Johnson (12 veces All-Star)



def jugador_mejores_estadisticas(jugadores:list[dict])-> None:
    pass



