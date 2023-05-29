from funciones import*

def app(lista_jugadores:list[dict]) -> None:
    texto_generado  = ""
    jugador_segun_indice = None

    while True:
         
        mostrar_menu()
        respuesta = input("Ingrese una opcion: ")
        respuesta = validar_respuesta(r'^[1]?[0-9]{1}$|20|23', respuesta)
        match(respuesta):
            case 0: 
                print("Salió de la app")
            case 1:
                mostrar_jugadores_dt(lista_jugadores, flag_indice)
            case 2 :
                mostrar_estadisticas_jugador_por_indice(lista_jugadores)
                
            case 3:
                guardar_estadisticas_jugador_CSV(nombre_archivo, contenido)
            case 4:
                mostrar_logro_jugador__por_nombre(lista_jugadores)

            case 5:
                promedio_puntos_por_partido_DT_ascendente(lista_de_jugadores)
            case 6:
                imprimir_datos_jugadores_salon(lista_jugadores)
            case 7:
                max_rebotes = encontrar_maximo(lista_jugadores, "estadisticas", "rebotes_totales")
                imprimir_dato(max_rebotes)
            case 8:
                max_porcentaje_tiros_campo = encontrar_maximo(lista_jugadores, "estadisticas", "porcentaje_tiros_de_campo" )
                imprimir_dato(max_porcentaje_tiros_campo)
            case 9:
                max_asistencias = encontrar_maximo(lista_jugadores, "estadisticas", "asistencias_totales" )
                imprimir_dato(max_asistencias)
            case 10:
                estadistica_buscada = "promedio_puntos_por_partido"
                valor_ingresado = input("Ingrese un valor para comparar: ")
                if valor_ingresado.replace(".","").isnumeric():
                    mostrar_jugadores_promediado_mas_stat(lista_jugadores, estadistica_buscada, float(valor_ingresado))
                else:
                    print("Valor ingresado erroneo, por favor vuelva al menu e ingrese una opcion valida")
            case 11:
                estadistica_buscada = "promedio_rebotes_por_partido"
                valor_ingresado = input("Ingrese un valor para comparar: ")
                if valor_ingresado.replace(".","").isnumeric():
                    mostrar_jugadores_promediado_mas_stat(lista_jugadores, estadistica_buscada, float(valor_ingresado))
                else:
                    print("Valor ingresado erroneo, por favor vuelva al menu e ingrese una opcion valida") 
            case 12:
                estadistica_buscada = "promedio_asistencias_por_partido"
                valor_ingresado = input("Ingrese un valor para comparar: ")
                if valor_ingresado.replace(".","").isnumeric():
                    mostrar_jugadores_promediado_mas_stat(lista_jugadores, estadistica_buscada, float(valor_ingresado))
                else:
                    print("Valor ingresado erroneo, por favor vuelva al menu e ingrese una opcion valida")
            case 13:
                jugadores_max_robos = encontrar_maximo(lista_jugadores, "estadisticas", "robos_totales")
                imprimir_dato(jugadores_max_robos)
            case 14:
                jugadores_max_bloqueos = encontrar_maximo(lista_jugadores, "estadisticas", "bloqueos_totales")
                imprimir_dato(jugadores_max_bloqueos)
            case 15:
                estadistica_buscada = "porcentaje_tiros_libres"
                valor_ingresado = input("Ingrese un valor para comparar: ")
                if valor_ingresado.replace(".", "").isnumeric():
                    mostrar_jugadores_promediado_mas_stat(lista_jugadores, estadistica_buscada, float(valor_ingresado))
                else:
                    print("valor ingresado erroneo, vuelva al menu e ingrese una opcion valida")
            case 16:
                estadistica_buscada = "promedio_puntos_por_partido"
                promedio = generar_promedio_segun_stat_menos_peor_valor(lista_jugadores, estadistica_buscada)
                print("El promedio total del equipo de {0} sin contar el jugador que peor promedia es de: {1}\n".format(estadistica_buscada.replace("_"," "), promedio))
            case 17:
                dict_jugador = jugador_mas_logros(lista_jugadores)
                print("el jugador con mas logros es {}, con los siguientes:".format(dict_jugador["nombre"]))
                for logro in dict_jugador["logors"]:
                    print(logro)
            case 18:
                estadistica_buscada = "porcentaje_tiros_triples"
                valor_ingresado = input("Ingrese un valor para comparar")
                if valor_ingresado.replace(".", "").isnumeric():
                    mostrar_jugadores_promediado_mas_stat(lista_jugadores, estadistica_buscada, float(valor_ingresado))
                else:
                    print("valor ingresado erroneo, vuelva al menu e ingrese una opcion nuevamente")

            case 19:
                jugador_mas_temporadas(lista_jugadores)
            case 20:
                lista_ordenada = ordenar_lista_segun_key(lista_jugadores, "posicion")
                estadistica_buscada = "porcentaje_tiros_de_campo"
                valor_ingresado = input("ingrese un valor para comparar: ")
                if valor_ingresado.replace(".", "").isnumeric():
                    mostrar_jugadores_promediado_mas_stat(lista_ordenada, estadistica_buscada, float(valor_ingresado), True)
                else:
                    print("valor erroneo, por favor vuelva al menu e ingrese una opcion nuevamente")
        limpiar_consola()
            
archivo= "dt.json"
lista_jugadores= leer_json(archivo)
app(lista_jugadores)
