import sys
import os
import App.logic as logic


def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")
    
def load_data(control):
    data_dir = os.path.join(os.getcwd(), "Data")
    filename = input("Ingrese el nombre del archivo (ej. movies-large.csv): ")
    file_path = os.path.join(data_dir, filename)
    if os.path.isfile(file_path):
        logic.load_data(control, file_path)
        print("Datos cargados correctamente")
    else:
        print(f"El archivo {file_path} no fue encontrado. Verifique el nombre y la ubicación.")

#TODO: Realizar la función para imprimir un elemento
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    movie_data = logic.get_data(control, id)
    
    if movie_data:
        print(f"Fecha: {movie_data[0]}")
        print(f"Título original: {movie_data[1]}")
        print(f"Idioma original: {movie_data[2]}")
        print(f"Duración: {movie_data[3]}")
        print(f"Presupuesto: {movie_data[4]}")
        print(f"Ingresos: {movie_data[5]}")
        print(f"Ganancias: {movie_data[6]}")
    else:
        print("No se encontró la película con ese ID.")
        

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    try:
        min_duracion = int(input("Ingrese el tiempo mínimo de duración en minutos: "))
        resp = logic.req_1(control, min_duracion)
        if isinstance(resp, str):
            print(resp)
        else:
            total_peliculas, peli_reciente = resp
            print(f"Total de películas que cumplen con el criterio: {total_peliculas}")
            print("\nÚltima película publicada que supera el tiempo mínimo:")
            print(f"Fecha de publicación: {peli_reciente[0]}")
            print(f"Título original: {peli_reciente[1]}")
            print(f"Idioma original: {peli_reciente[2]}")
            print(f"Duración: {peli_reciente[3]} minutos")
            print(f"Presupuesto: {peli_reciente[4]}")
            print(f"Ingresos: {peli_reciente[5]}")
            print(f"Ganancias: {peli_reciente[6]}")
            print(f"Puntaje: {peli_reciente[7]}")
           
        
    except ValueError:
        print("Error: Debes ingresar un número válido para la duración mínima.")


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    idioma = input("Ingrese el idioma original en el que desea conocer la última película publicada: ")
    try:
        buscadas, ultima_pelicula = logic.req_2(control, idioma)
        print("Número de películas con ese idioma original: " + str(buscadas))
        print("Fecha de publicación de la última película: " + str(ultima_pelicula[0]))
        print("Título original de la última película: " + str(ultima_pelicula[1]))
        print("Presupuesto de la última película: " + str(ultima_pelicula[4]))
        print("Dinero recaudado de la última película: " + str(ultima_pelicula[5]))
        print("Ganancia final de la última película: " + str(ultima_pelicula[6]))
        print("Duración en minutos de la última película: " + str(ultima_pelicula[3]))
        print("Puntaje de calificación de la película: " + str(ultima_pelicula[7]))
        print("Número de votos de la película: " + str(ultima_pelicula[8]))
    except IndexError as e:
        print(e)


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    idioma = input("Ingrese el idioma original de publicación (ej.: en, fr, zh): ")
    fecha_inicio = input("Ingrese la fecha inicial del periodo a consultar (formato YYYY-MM-DD): ")
    fecha_final = input("Ingrese la fecha final del periodo a consultar (formato YYYY-MM-DD): ")
    try:
        resp = logic.req_3(control, idioma, fecha_inicio, fecha_final)
        print(resp)
    except ValueError:
        print("Error: Formato de fecha incorrecto.")
        
def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    status_bs = input("Ingrese el estado de producción (ej.: 'Released', 'Rumored', etc.): ")
    f_inicial = input("Ingrese la fecha inicial del periodo a consultar (formato: YYYY-MM-DD): ")
    f_final = input("Ingrese la fecha final del periodo a consultar (formato: YYYY-MM-DD): ")
    resultado = logic.req_4(control, status_bs, f_inicial, f_final)
    print("\nNúmero total de películas con el estado '{}' entre {} y {}: {}".format(
        status_bs, f_inicial, f_final, resultado[0]))
    #print("Tiempo promedio de duración de las películas: {:.2f} minutos\n".format(
     #   resultado["Tiempo promedio de duración"]))
    num_peliculas = len(resultado[2])
    if num_peliculas > 20:
        print("Mostrando las primeras 5 y las últimas 5 películas, ya que hay más de 20 en total:")
    # Imprimir los detalles de las películas
    print("Listado de películas que cumplen con los criterios de búsqueda:")
    for pelicula in resultado[2]:
        print("------------------------------------")
        print("Título original: " + pelicula["titulo_original"])
        print("Presupuesto: " + str(pelicula["presupuesto"]))
        print("Ingresos: " + str(pelicula["ingresos"]))
        print("Ganancia: " + str(pelicula["ganancias"]))
        print("Duración: " + str(pelicula["duracion"]) + " minutos")
        print("Puntaje de calificación: " + str(pelicula["puntaje"]))
        print("Idioma original: " + pelicula["idioma"])
        
def print_req_5(control):
    """
    Función que imprime la solución del Requerimiento 5 en consola.
    """
    # Obtener entradas del usuario
    fecha_inicial = input("Ingrese la fecha inicial del periodo a consultar (formato: YYYY-MM-DD): ")
    fecha_final = input("Ingrese la fecha final del periodo a consultar (formato: YYYY-MM-DD): ")
    
    # Convertir límites inferiores y superiores a enteros
    try:
        limite_inferior = int(input("Ingrese el limite inferior (en minutos): "))
        limite_superior = int(input("Ingrese el limite superior (en minutos): "))
    except ValueError:
        print("Error: Los límites deben ser números enteros.")
        return
    # Llamar a la función req_5 y manejar posibles errores
    try:
        rta = logic.req_5(control, fecha_inicial, fecha_final, limite_inferior, limite_superior)
        
        print(f"Número total de películas con duración entre {limite_inferior} y {limite_superior} minutos: {rta['numero total de peliculas']}")
        print(f"Tiempo promedio de duración: {rta['tiempo promedio de duracion']:.2f} minutos\n")

        # Imprimir los detalles de las películas
        print("Listado de películas que cumplen con los criterios de búsqueda:")
        peliculas = rta["peliculas"]
        
        # Mostrar solo las primeras 5 y últimas 5 si hay más de 20
        if len(peliculas) > 20:
            peliculas = peliculas[:5] + peliculas[-5:]
            print("\nNota: La lista de películas excede 20 elementos. Se han mostrado solo las primeras 5 y las últimas 5.")
        
        for pelicula in peliculas:
            print(f"Fecha de publicación: {pelicula['fecha de publicacion']}")
            print(f"Título original: {pelicula['titulo_original']}")
            print(f"Presupuesto: {pelicula['presupuesto']}")
            print(f"Ingresos: {pelicula['ingresos']}")
            print(f"Ganancia: {pelicula['ganancia']}")
            print(f"Duración: {pelicula['duracion']} minutos")
            print(f"Puntaje de calificación: {pelicula['puntaje de calificacion']}")
            print(f"Idioma original: {pelicula['idioma original']}")
            print()

    except Exception as e:
        print(f"Error al procesar el requerimiento: {e}")




def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    año_inicial_consulta = input("Año donde se quiere empezar la busqueda: ")
    año_final_consulta = input("Año donde quiere terminar la busqueda: ")
    idioma_original = input("Idioma Original: ") 
    
    rta = logic.req_6(control, idioma_original,año_inicial_consulta, año_final_consulta) 
    
    print("===== Resultados del Requerimiento 6 =====\n")
    for año, datos in sorted(rta.items()):
        print(f"Año: {año}")
        print(f"Total de películas: {datos['total_peliculas']}")
        print(f"Duración total: {datos['total_duracion']} minutos")
        print(f"Duración promedio: {datos.get('promedio_duracion', 0):.2f} minutos")
        print(f"Votación promedio: {datos.get('promedio_votacion', 0):.2f}")
        print(f"Ganancias totales: {datos['total_ganancias']}")
        print(f"Mejor película: {datos['mejor_pelicula']['titulo']} (Votación: {datos['mejor_pelicula']['votacion']:.2f})")
        print(f"Peor película: {datos['peor_pelicula']['titulo']} (Votación: {datos['peor_pelicula']['votacion']:.2f})")


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    compania = input("Ingrese el nombre de compañía productora. (ej. “Nilsen Premiere”) ")
    anio_inicio = input("Ingrese el año inicial del periodo a consultar (con formato YYYY) ")
    anio_final = input("Ingrese el año final del periodo a consultar (con formato YYYY) ")
    try:
        resp = logic.req_7(control, compania, anio_inicio, anio_final)
        print(resp)
    except ValueError:
        print("Error: el nombre de la compañia productora o los años ingresados son incorrectos.")
   




def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    anio_consulta = input("Ingrese el año de consulta (formato: YYYY): ")
    genero_consulta = input("Ingrese el género de las películas (ej.: 'Action', 'Comedy', etc.): ")
    try:
        resultado = logic.req_8(control, int(anio_consulta), genero_consulta)
        print("\nTotal de películas publicadas en el año {} de género '{}': {}".format(
            anio_consulta, genero_consulta, resultado["Total de películas publicadas"]))
        print("Promedio de votación de las películas: {:.2f}".format(
            resultado["Promedio de votación"]))
        print("Tiempo promedio de duración: {:.2f} minutos".format(
            resultado["Tiempo promedio de duración"]))
        print("Ganancias acumuladas: {}".format(
            resultado["Ganancias acumuladas"]))
        print("\nMejor película del año {} en el género '{}':".format(anio_consulta, genero_consulta))
        print("Nombre: " + resultado["Mejor película"]["Nombre"])
        print("Puntaje: {:.2f}".format(resultado["Mejor película"]["Puntaje"]))
        print("\nPeor película del año {} en el género '{}':".format(anio_consulta, genero_consulta))
        print("Nombre: " + resultado["Peor película"]["Nombre"])
        print("Puntaje: {:.2f}".format(resultado["Peor película"]["Puntaje"]))

    except Exception as e:
        print(f"Error al procesar el requerimiento: {e}")

    anio_consulta = input("Ingrese el año de consulta (formato: YYYY): ")
    genero_consulta = input("Ingrese el género de las películas (ej.: 'Action', 'Comedy', etc.): ")
    try:
        resultado = logic.req_8(control, int(anio_consulta), genero_consulta)
        print("\nTotal de películas publicadas en el año {} de género '{}': {}".format(
            anio_consulta, genero_consulta, resultado["Total de películas publicadas"]))
        print("Promedio de votación de las películas: {:.2f}".format(
            resultado["Promedio de votación"]))
        print("Tiempo promedio de duración: {:.2f} minutos".format(
            resultado["Tiempo promedio de duración"]))
        print("Ganancias acumuladas: {}".format(
            resultado["Ganancias acumuladas"]))
        print("\nMejor película del año {} en el género '{}':".format(anio_consulta, genero_consulta))
        print("Nombre: " + resultado["Mejor película"]["Nombre"])
        print("Puntaje: {:.2f}".format(resultado["Mejor película"]["Puntaje"]))
        print("\nPeor película del año {} en el género '{}':".format(anio_consulta, genero_consulta))
        print("Nombre: " + resultado["Peor película"]["Nombre"])
        print("Puntaje: {:.2f}".format(resultado["Peor película"]["Puntaje"]))

    except Exception as e:
        print(f"Error al procesar el requerimiento: {e}")



# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
