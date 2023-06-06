import re
import json
import csv
import os


def limpiar_consola () -> None:
    """
    Espera a que el usuario presione enter y vacia la consola (sistema operativo windows)
    """

    _ = input("Presione una tecla para continuar")
    os.system("cls")
    

def leer_json (ruta:str, encoding='utf-8'):
    with open (ruta, "r") as archivo:
        data= json.load(archivo)
        lista_jugadores = data["jugadores"]
    
    return lista_jugadores
        
"""
UTF-8 (Unicode Transformation Format-8) es una codificación de caracteres que puede representar 
prácticamente todos los caracteres utilizados en cualquier idioma.
Cuando se trabaja con archivos de texto en Python, es importante asegurarse de que la codificación 
utilizada coincida con la codificación del archivo. Si no se especifica una codificación, Python respeta
la codificación predeterminada del sistema operativo, que puede variar. 
Es una buena práctica especificar la codificación al abrir o guardar archivos para evitar problemas de caracteres incorrectos o ilegibles.
 """


def imprimir_dato(texto:str):
    """
    La funcion "imprimir_dato" comprueba si la entrada en una cadena de textoby la imprime,
    de lo contrario imprime un mensaje advirtiendo que no es una cadena lo que se ingreso.
    """
    if type(texto)== str:
        print(texto)
    else:
        print("No es una cadena de texto")

def validar_opcion(expresion:str, ingreso_usuario: str)-> str:
    """
    Esta función valida si la entrada del usuario es una opción correcta.
    
    :param expresion: un patrón de expresión regular que la entrada del usuario debe coincidir para que
    se considere válido
    :type expresion: str
    :param ingreso_usuario: La entrada del usuario que necesita ser validada. Debería ser una cadena
    :type ingreso_usuario: str
    :return: un valor entero si la entrada del usuario coincide con el patrón de expresión regular; de
    lo contrario, devuelve un valor booleano de False.
    """
    
    validacion_opcion = False
    if re.match(expresion, ingreso_usuario): #busca coincidencia entre el patron (en el inicio) y la cadena
        validacion_opcion = int(ingreso_usuario)
    return validacion_opcion

#1
def mostrar_dream_team(lista_jugadores: list[dict])-> list:   # buscar_nombre_posicion
    """
    La función "mostrar_dream_team" toma una lista de diccionarios que contienen información sobre
    jugadores de fútbol e imprime sus nombres y posiciones de forma formateada.
    """
    
    if not lista_jugadores:              # mensaje = "Error"
        print("La lista esta vacia")
        return False
    
    if lista_jugadores:
        mensaje = "indice - Nombre - Posicion\n"
        for i in range(len(lista_jugadores)):
            jugador = lista_jugadores[i]
            mensaje += "{0} - {1} - {2}".format(i, jugador['nombre'],jugador['posicion']) + "\n"
    imprimir_dato(mensaje)
           

def imprimir_menu()-> None:
    menu =\
    """
    1. Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
    2. Seleccionar un jugador por su índice y mostrar sus estadísticas
    3. Después de mostrar las estadísticas, guardar las estadísticas de ese jugador en un archivo CSV. 
    4. Buscar un jugador por su nombre y mostrar sus logros.
    5. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream
       Team, ordenado por nombre de manera ascendente.
    6. Ingresar el nombre de un jugador y mostrar si ese jugador es
       miembro del Salón de la Fama del Baloncesto.
    7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
    8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
    9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
    10. Ingresar un valor y mostrar los jugadores que han promediado
        más puntos por partido que ese valor.
    11. Ingresar un valor y mostrar los jugadores que han promediado
        más rebotes por partido que ese valor.
    12. Ingresar un valor y mostrar los jugadores que han promediado
        más asistencias por partido que ese valor.
    13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.
    14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
    15. Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un
        porcentaje de tiros libres superior a ese valor.
    16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al
        jugador con la menor cantidad de puntos por partido.
    17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
    18. Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un
        porcentaje de tiros triples superior a ese valor.
    19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
    20. Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por
        posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a
        ese valor.
    24. Determinar la cantidad de jugadores que hay por cada posición.
    25. Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente.
    26. Determinar qué jugador tiene las mejores estadísticas en cada valor.
    27. Determinar qué jugador tiene las mejores estadísticas de todos.
    """
    imprimir_dato(menu)
    
def dream_team_menu_principal(): 
    '''
    imprime el menu y toma una opcion del usuario
    devuelve la opcion elegida, en caso de False devuelve -1
    '''
    imprimir_menu()
    opcion = input("Ingresa una opción del menú: ").upper()
    validacion = re.match( r'^[1]?[0-9]{1}$|20|23|24|25|26|27', opcion)
    if validacion:
         return True
    else:
         return False
       
def validar_numeros(dato:str):
    """
    La función valida si una cadena determinada es numérica y la convierte en un número entero o
    flotante, y devuelve False si no es numérica.
    
    :param dato: una cadena que representa un número que debe validarse y convertirse en un número
    entero o flotante
    :type dato: str
    
    """

    if re.match(r"^\d+(\.\d+)?$", dato):
        try:
            return int(dato)
        except Exception as error:
            return float(dato)
    else:
        return False
    
#2


#3
def generar_texto(dicc_jugador: dict)-> str:
    """
    La función toma un diccionario de las estadísticas de un jugador y devuelve una cadena formateada
    que contiene su nombre, posición y estadísticas.
    
    :param dicc_jugador: El parámetro "dicc_jugador" es un diccionario que contiene las estadísticas de
    un jugador, incluido su nombre, posición y otras métricas de rendimiento
    :type dicc_jugador: dict
    :return: una cadena formateada que contiene el nombre, la posición y las estadísticas del jugador.
    """
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


def guardar_archivo_csv(nombre_archivo:str, contenido:str)-> bool:
    """
    Esta función guarda el contenido de una cadena en un archivo con el nombre de archivo dado y
    devuelve un valor booleano que indica si la operación fue exitosa o no.
    
    :param nombre_archivo: Una cadena que representa el nombre del archivo que se va a crear o
    sobrescribir
    :type nombre_archivo: str
    :param contenido: El contenido (texto) que se escribirá en el archivo
    :type contenido: str
    :return: La función siempre devuelve False, independientemente de si la operación se realizó
    correctamente o no.
    """
    """
    Esta funcion guarda el contenido de una cadena de un archivo con el nombre de archivo dado y
    devuelve un valor booleano que indica si la operacion fue exitosa o no
    """
    with open(nombre_archivo, "w+") as archivo:
        resultado = None
        resultado = archivo.write(contenido)
    if resultado:
        print("Se creo el archivo: {0}".format(nombre_archivo))
        return True
    
    print("Erro al crear el archivo: {0}".format(nombre_archivo))
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
    Esta función toma una lista de diccionarios que contienen información del jugador y un nombre de
    jugador como entrada, e imprime los logros del jugador con el nombre dado.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus logros
    :type lista_jugadores: list[dict]
    :param nombre: El parámetro "nombre" es una cadena que representa el nombre del jugador cuyos logros
    queremos mostrar
    :type nombre: str
    :return: La función no tiene una declaración de devolución, pero imprime información sobre los
    logros de un jugador cuyo nombre coincide con el parámetro de entrada.
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


#5
def calcular_promedio_total(lista_jugadores:list[dict], estadistica:str):
    """
    Esta función calcula el promedio total de una estadística seleccionada para una lista de jugadores.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus estadísticas
    :type lista_jugadores: list[dict]
    :param estadistica: El nombre de la estadística para la que se calculará el promedio total. Debe ser
    una cadena y debe coincidir con una de las claves del diccionario "estadisticas" de cada jugador de
    la lista
    :type estadistica: str
    :return: el promedio calculado de la estadística seleccionada para la lista de jugadores
    proporcionada como entrada. Si la lista está vacía, devuelve -1. Si la estadística seleccionada no
    se encuentra en el diccionario de estadísticas del jugador, imprime un mensaje que dice que la
    estadística no existe.
    """
    """
    Esta funcion calcula el promedio total de la estadistica seleccionada
    """
    if len(lista_jugadores) == 0:
        print("Lista vacia.")
        return -1
    lista = lista_jugadores[:]
    if len(lista) <= 1:
        return lista
    contador = 0
    acumulador = 0
    if estadistica in lista[0]["estadisticas"].keys():
        for jugador in lista:
            acumulador += jugador["estadisticas"][estadistica]
            contador += 1
        promedio = acumulador / contador
        return promedio
    else:
        print("Estadistica inexixtente")


def ordenar_lista_segun_key(lista_jugadores: list[dict], key_a_ordenar : str, flag_estadistica = False, orden_ascendente = True)-> list:
    """
    Esta función ordena una lista de diccionarios según una clave específica, con la opción de ordenar
    en orden ascendente o descendente y considerar diccionarios de estadísticas anidados.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus estadísticas
    :type lista_jugadores: list[dict]
    :param key_a_ordenar: La clave o atributo del diccionario en la lista de jugadores que se usará para
    ordenar la lista
    :type key_a_ordenar: str
    :param flag_estadistica: Una bandera booleana que indica si la clave a ordenar está anidada dentro
    de un diccionario bajo la clave "estadisticas" en cada elemento de la lista. Si es Verdadero, la
    función accederá a la clave anidada para realizar la clasificación. Si es False, se ordenará según
    la clave de nivel superior proporcionada, defaults to False (optional)
    :param orden_ascendente: Un parámetro booleano que determina si la lista debe ordenarse en orden
    ascendente (Verdadero) o descendente (Falso), defaults to True (optional)
    :return: una lista de diccionarios ordenados según la clave especificada y el orden de
    clasificación.
    """
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

#6
def buscar_jugador_sfb(lista_jugadores: list[dict], nombre: str):
    """
    Esta función busca el nombre de un jugador en una lista de diccionarios y muestra si está o no en el
    Salón de la Fama del Baloncesto.
    
    :param lista_jugadores: Una lista de diccionarios que representan a jugadores de baloncesto, donde
    cada diccionario contiene información sobre un jugador, como su nombre, logros, etc
    :type lista_jugadores: list[dict]
    :param nombre: El nombre del jugador que la función está buscando en la lista de jugadores
    :type nombre: str
    :return: La función no tiene una declaración de devolución, por lo que devuelve Ninguno de forma
    predeterminada.
    """
    """
    Esta funcion muestra un listado de jugadores, junto a su nombre y si se encuentran o no en un salon de fama. )sfb)

    """
    if len(lista_jugadores) == 0:
        print("Lista vacia")
        return False
    if nombre == " ":
        print("Nombre vacio.")
    else:
        lista = lista_jugadores[:]
        logro_sfb = "Miembro del Salon de la Fama del Baloncesto"
        lista_jugadores_sfb = []
        flag_jugador = False
        for jugador in lista:
            busqueda = buscar_por_nombre(lista, jugador, nombre)
            if busqueda:
                flag_jugador = True
                for logro in jugador["logros"]:
                    if logro == logro_sfb:
                        lista_jugadores_sfb.append([jugador["nombre"], "Si"])
                        break
                    else:
                        lista_jugadores_sfb.append([jugador["nombre"], " No"])

        mensaje = " "
        if flag_jugador == False:
            print("No existe jugador con ese nombre")
        else:
            for jugador in lista_jugadores_sfb:
                mensaje += "Nombre: {0}\nSe encuentra dentro del SFB?: {1}\n\n".format(jugador[0], jugador[1])
            print(mensaje)
    

#7
def encontrar_maximo(lista_jugadores:list[dict], clave_jugador:str, clave_valor:str)-> str:
    """
    Esta función encuentra el jugador con el valor máximo para una clave específica en una lista de
    jugadores y devuelve su nombre y valor como una cadena.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus atributos
    :type lista_jugadores: list[dict]
    :param clave_jugador: La clave en el diccionario del jugador que contiene la información a comparar
    (por ejemplo, "estadisticas")
    :type clave_jugador: str
    :param clave_valor: La clave del valor del que queremos encontrar el máximo en la lista de jugadores
    :type clave_valor: str
    :return: un mensaje de cadena que indica el jugador con el valor más alto para una clave específica
    en una lista de diccionarios. Si la lista está vacía o hay un error, devuelve un mensaje de error.
    """
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
    Esta función muestra los jugadores que superan un determinado valor en una determinada estadística
    y, opcionalmente, puede mostrar su posición.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus estadísticas
    :type lista_jugadores: list[dict]
    :param estadistica: una cadena que representa la estadística a comparar (por ejemplo, "puntos",
    "rebotes", "asistencias")
    :type estadistica: str
    :param valor_stat: El valor de la estadística que queremos comparar con las estadísticas de los
    jugadores
    :type valor_stat: float
    :param flag_mostrar_posicion: El parámetro flag_mostrar_posicion es una bandera booleana que
    determina si mostrar o no la posición de los jugadores en la salida. Si se establece en True, la
    posición de los jugadores se mostrará junto con su nombre y el valor de la estadística especificada.
    Si se establece en falso
    :type flag_mostrar_posicion: False
    :return: una lista de jugadores que tienen una estadística mayor que el valor de entrada, junto con
    su nombre y posición. Si la lista de entrada está vacía, la función devuelve False. Si ningún
    jugador cumple con los criterios, la función imprime un mensaje y devuelve una lista vacía.
    """
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
    
def generar_promedio_segun_stat_menos_peor_valor(lista_jugadores:list[dict], estadistica: str):
    """
    Esta función genera el promedio de una estadística elegida para una lista de jugadores, excluyendo
    al jugador con el peor promedio para esa estadística.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus estadísticas
    :type lista_jugadores: list[dict]
    :param estadistica: El parámetro "estadistica" es una cadena que representa el nombre de la
    estadística para la cual queremos generar el promedio
    :type estadistica: str
    :return: ya sea el promedio calculado de la estadística elegida o Falso si la lista de entrada está
    vacía.
    """
    """
    Esta funcion genera el promedio de la suma de la estadistica elegida, sin tener en cuenta el stat del jugador que peor promedia
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
    Esta función calcula el jugador con más logros en su carrera de una lista de jugadores.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y
    sus logros
    :type lista_jugadores: list[dict]
    :return: un diccionario con el jugador que más logros tiene en su carrera.
    """
    """
    Calcula el jugador con mas logros en su carrera
    recibe la lista de jugadores
    retorna el jugador con mas logros obtenidos(dict)
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
            elif "Miembro" in logro: #Verifica si el logro contiene la palabra "Miembro". Entra en el bloque si se cumple.
                acumulador_logros += 1
            else: #Si no se cumple ninguna de las condiciones anteriores, se ejecuta este bloque.
                patron = r"\d{3}" 
                if re.match(patron, logro): # si el logro empieza con 1 o 2 digitos entra.
                    acumulador_logros += int(re.findall(patron, logro)[0]) # trae el numero de cada logro, lo descompone en componentes más pequeños y significativos y lo suma al acumulador
        logros_jugadores.append(lista_de_jugadores.index(jugador)) # agrego el indice del jugador de la lista real
        logros_jugadores.append(acumulador_logros) # agrego la cantidad de logros que tenga  ese jugador
        logros_jugadores_sin_indices.append(acumulador_logros) # lista aparte solo con logros
        
        acumulador_logros = 0
    for indice in range(len(logros_jugadores_sin_indices)): # recorro segun el largo de la lista de solo logros
        if indice == 0 or float(logros_jugadores_sin_indices[maximo_indice]) < float(logros_jugadores_sin_indices[indice]):
            #Verifica si el índice actual es 0 o el valor de logros en el índice máximo es menor al valor de logros en el 
            # índice actual. Entra en el bloque si se cumple.
            maximo_indice = indice
            numero_maximo = logros_jugadores_sin_indices[maximo_indice] #Almacena el número máximo de logros.
    indice_jugador_mas_logros = logros_jugadores[logros_jugadores.index(numero_maximo) -1] # dentro del [] obtiene el indice anterior del numero_maximo,
                                                                                           # que seria el indice del jugador en la lista original. al ser jordan da 0
                                                                        # y los logros_jugadores[x] te da la posicion real del json del jugador con mas logros
    return lista_de_jugadores[indice_jugador_mas_logros]

def jugador_mas_temporadas(jugadores:list[dict])-> None:
    """
    Esta función encuentra al jugador(es) con la mayor cantidad de temporadas jugadas en base a una
    lista de diccionarios de jugadores y los imprime junto con su número de temporadas.
    
    :param jugadores: una lista de diccionarios que representan a los jugadores, donde cada diccionario
    contiene información sobre un jugador, como su nombre y estadísticas
    :type jugadores: list[dict]
    """
    """
    Esta funcion encuentra al jugador(es) con la mayor cantidad de temporadas jugadas en base a una
    lista de dicc de jugadores y los imprime uno a la vex junto con su cantidad de temporadas 
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

def cantidad_jugadores_por_posicion(lista_jugadores):
    jugadores_por_posicion = {}
    for jugador in lista_jugadores:
        posicion = jugador["posicion"]
        if posicion in jugadores_por_posicion:
            jugadores_por_posicion[posicion] += 1
        else:
            jugadores_por_posicion[posicion] = 1
    
    for posicion, cantidad in jugadores_por_posicion.items():
        print(posicion + ": " + str(cantidad))

    #Se crea un diccionario vacío llamado jugadores_por_posicion para almacenar la cantidad de jugadores por posición.
    #si ya existe se suma uno a esa posicion


def mostrar_jugadores_cantidad_allstar(lista_jugadores): #ver
    all_star_count = 0
    for jugador in lista_jugadores:
        logros = jugador.get("logros", [])
        for logro in logros:
            if "veces All-Star" in logro:
                cantidad = "".join(filter(str.isdigit, logro))
                all_star_count += int(cantidad)
                break
    return all_star_count
    
def jugador_mejores_estadisticas_por_valor(lista_jugadores, estadistica):
    pass

def jugador_mejores_estadisticas(lista_jugadores): #verrr
    mejor_jugador = max(lista_jugadores, key=lambda jugador: sum(jugador["estadisticas"].values()))
    print("Mejor jugador en todas las estadísticas: " + mejor_jugador["nombre"])
# utiliza la función max() para encontrar el jugador con el valor máximo de una determinada clave. 
# La clave se define mediante una función lambda que toma un jugador y calcula la suma de los valores en el diccionario
# de estadísticas del jugador. La función sum() se utiliza para sumar todos los valores del diccionario.
# lambda función sin nombre que se puede definir en una sola línea

# la función jugador_mejores_estadisticas encuentra el jugador con las mejores
#  estadísticas sumando los valores en el diccionario de estadísticas y muestra su nombre en la consola.













