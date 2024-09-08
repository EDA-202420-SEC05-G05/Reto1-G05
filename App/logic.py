import time
from DataStructures.List import array_list as lt
import csv
import os
import json
from datetime import datetime


csv.field_size_limit(2147483647)
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    movies = {"fecha": None, "or_title": None, "idioma": None, "duracion": None
              , "presupuesto": None, "ingresos": None,
              "ganancias": None, "id": None, "status": None, "vote_average": None, "vote_count": None, "genero": None, "production_companies": None}

    movies["fecha"] = lt.new_list()
    movies["or_title"] = lt.new_list()
    movies["idioma"] = lt.new_list()
    movies["duracion"] = lt.new_list()
    movies["presupuesto"] = lt.new_list()
    movies["ingresos"] = lt.new_list()
    movies["ganancias"] = lt.new_list()
    movies["id"] = lt.new_list()
    movies["status"] = lt.new_list()
    movies["vote_average"] = lt.new_list()
    movies["vote_count"] = lt.new_list()
    movies['genero'] = lt.new_list()
    movies['production_companies'] = lt.new_list()
    return movies
# Funciones para la carga de datos

def load_fecha(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        release_date = row['release_date'] if row['release_date'] else "Desconocido"
        lt.add_last(movies['fecha'], release_date)

# Función para cargar los títulos originales de las películas
def load_title(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        or_title = row['title'] if row['title'] else "Desconocido"
        lt.add_last(movies['or_title'], or_title)

# Función para cargar el idioma original de las películas
def load_idioma(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        idioma = row['original_language'] if row['original_language'] else "Desconocido"
        lt.add_last(movies['idioma'], idioma)
        
# Función para cargar la duración de las películas
def load_duracion(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        duracion = row['runtime'] if row['runtime'] else "Desconocido"
        lt.add_last(movies['duracion'], duracion)

# Función para cargar el presupuesto, ingresos y calcular ganancias
def load_financials(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        presupuesto = int(row['budget']) if row['budget'].isdigit() else 0
        ingresos = int(row['revenue']) if row['revenue'].isdigit() else 0
        lt.add_last(movies['presupuesto'], presupuesto)
        lt.add_last(movies['ingresos'], ingresos)
        lt.add_last(movies['ganancias'], ingresos - presupuesto if ingresos and presupuesto else "Indefinido")

def load_id(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        movie_id = row['id'] if row['id'] else "Desconocido"
        lt.add_last(movies['id'], movie_id)

def load_status(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        status = row['status'] if row['status'] else "Desconocido"
        lt.add_last(movies['status'], status)
        
def load_vote_average(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        vote_average = row['vote_average'] if row['vote_average'] else 0
        lt.add_last(movies['vote_average'], vote_average)
        
def load_vote_count(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        vote_count = row['vote_count'] if row['vote_count'] else 0
        lt.add_last(movies['vote_count'], vote_count)

def load_genero(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        genero = row['genres'] if row['genres'] else "Desconocido"
        lt.add_last(movies['genero'], genero)

def load_production_companies(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        production_companies = row['production_companies'] if row['production_companies'] else "Desconocido"
        lt.add_last(movies['production_companies'], production_companies)


def load_data(catalog, filename):
    load_fecha(catalog, filename)
    load_title(catalog, filename)
    load_idioma(catalog, filename)
    load_duracion(catalog, filename)
    load_financials(catalog, filename)
    load_id(catalog, filename)
    load_status(catalog, filename)
    load_vote_average(catalog, filename)
    load_vote_count(catalog, filename)
    load_genero(catalog, filename)
    load_production_companies(catalog, filename)
    
        
    return catalog

# Funciones de consulta sobre el catálogo

def get_data(movies, id):
    fecha = lt.get_element(movies['fecha'], id) if lt.get_element(movies['fecha'], id) else "Desconocido"
    or_title = lt.get_element(movies['or_title'], id) if lt.get_element(movies['or_title'], id) else "Desconocido"
    idioma = lt.get_element(movies['idioma'], id) if lt.get_element(movies['idioma'], id) else "Desconocido"
    duracion = lt.get_element(movies['duracion'], id) if lt.get_element(movies['duracion'], id) else "Desconocido"
    presupuesto = lt.get_element(movies['presupuesto'], id)
    ingresos = lt.get_element(movies['ingresos'], id)
    puntaje = lt.get_element(movies['vote_average'], id) if lt.get_element(movies['vote_average'], id) else "Desconocido"
    status = lt.get_element(movies["status"], id) if lt.get_element(movies['vote_average'], id) else "Desconocido"
    total_votaciones = lt.get_element(movies['vote_count'], id) if lt.get_element(movies['vote_count'], id) else "Desconocido"
    genero = lt.get_element(movies['genero'], id) if lt.get_element(movies['genero'], id) else "Desconocido"
    production_companies = lt.get_element(movies['production_companies'], id) if lt.get_element(movies['production_companies'], id) else "Desconocido"
    id = lt.get_element(movies['id'], id) if lt.get_element(movies['id'], id) else "Desconocido"


    if presupuesto == 0:
        presupuesto = "Indefinido"
    if ingresos == 0:
        ingresos = "Indefinido"
    if isinstance(presupuesto, int) and isinstance(ingresos, int):
        ganancias = ingresos - presupuesto
    else:
        ganancias = "Indefinido"
    
    return [fecha, or_title, idioma, duracion, presupuesto, ingresos, ganancias, puntaje, status, total_votaciones, genero, production_companies, id]

def report_data(movies):
    total_movies = lt.size(movies['fecha'])
    first_five = [get_data(movies, i+1) for i in range(5)]
    last_five = [get_data(movies, total_movies - 4 + i) for i in range(5)]
    return total_movies, first_five, last_five


def req_1(catalog, min_duracion):
    """
    Retorna el resultado del requerimiento 1
    """
     # TODO: Modificar el requerimiento 1
    total_peliculas = lt.size(catalog['duracion'])
    peliculas_con_fecha = []
    for i in range(0, total_peliculas):
        duracion_str = lt.get_element(catalog['duracion'], i).strip()
        try:
            duracion = float(duracion_str)
        except ValueError:
            print(f"Advertencia: No se pudo convertir '{duracion_str}' a float.")
            continue
        if duracion >= min_duracion:
            fecha = lt.get_element(catalog['fecha'], i)
            peliculas_con_fecha.append((i, fecha))
    peliculas_con_fecha.sort(key=lambda x: x[1], reverse=True)
    
    if len(peliculas_con_fecha) == 0:
        return "No se encontraron películas que superen los minutos de duración especificados."
    else:
        peli_reciente_id = peliculas_con_fecha[0][0]
        peli_reciente = get_data(catalog, peli_reciente_id)
        return len(peliculas_con_fecha), peli_reciente
    
def req_2(movies,idioma_buscado):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    buscadas = 0
    ultima_pelicula = None
    total_peliculas = lt.size(movies['fecha'])
    for i in range(1, total_peliculas + 1):
        idioma_pelicula = lt.get_element(movies['idioma'], i)
        if idioma_pelicula == idioma_buscado:
            buscadas += 1
            ultima_pelicula = get_data(movies, i)
    if buscadas == 0:
        raise IndexError("No se encontraron películas en el idioma:" + str(idioma_buscado))
    return buscadas,ultima_pelicula

def req_3(catalog, idioma, fecha_inicio, fecha_final):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    total_peliculas = lt.size(catalog['fecha'])
    peliculas_filtradas = []
    duracion_total = 0
    formato_fecha = "%Y-%m-%d"

    for i in range(0, total_peliculas):
        fecha = lt.get_element(catalog['fecha'], i)
        idioma_pelicula = lt.get_element(catalog['idioma'], i)
        if idioma_pelicula == idioma:
            try:
                fecha_pelicula = datetime.strptime(fecha, formato_fecha)
                fecha_inicio_dt = datetime.strptime(fecha_inicio, formato_fecha)
                fecha_final_dt = datetime.strptime(fecha_final, formato_fecha)

                if fecha_inicio_dt <= fecha_pelicula <= fecha_final_dt:
                    pelicula_data = get_data(catalog, i)
                
                    pelicula_filtrada = [
                        pelicula_data[0],  
                        pelicula_data[1],  
                        pelicula_data[4],  
                        pelicula_data[5],  
                        pelicula_data[6],  
                        pelicula_data[3],  #duracion
                        pelicula_data[7],  
                        pelicula_data[8]   
                    ]
                    try: 
                        duracion_total += float(pelicula_data[3])
                    except ValueError:
                        continue
                    peliculas_filtradas.append(pelicula_filtrada)
                    duracion_total += int(pelicula_data[3]) if pelicula_data[3].isdigit() else 0
            except ValueError:
                continue
    total_filtradas = len(peliculas_filtradas)
    
    
    
    if total_filtradas == 0:
        return "No se encontraron películas para el idioma y las fechas especificadas."
    duracion_promedio = duracion_total / total_filtradas if total_filtradas > 0 else 0
    if total_filtradas > 20:
        peliculas_filtradas = peliculas_filtradas[:5] + peliculas_filtradas[-5:]
    return total_filtradas, duracion_promedio, peliculas_filtradas

def req_4(catalog,status_bs,f_inicial,f_final):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pelis_bs = []
    formato_fecha = "%Y-%m-%d"
    total_peliculas = lt.size(catalog['fecha'])
    fecha_inicio_dt = datetime.strptime(f_inicial, formato_fecha)
    fecha_final_dt = datetime.strptime(f_final, formato_fecha)
    duracion_total = 0
    peliculas_contadas = 0
    for i in range(0, total_peliculas):
        fecha = lt.get_element(catalog['fecha'], i)
        status = lt.get_element(catalog['status'], i)
        fecha_pelicula = datetime.strptime(fecha, formato_fecha)
        if status == status_bs and fecha_inicio_dt <= fecha_pelicula <= fecha_final_dt:
            pelicula_data = get_data(catalog, i)
            fecha_publicacion = pelicula_data[0]
            titulo_original = pelicula_data[1]
            presupuesto = pelicula_data[4]
            ingresos = pelicula_data[5]
            ganancias = pelicula_data[6]
            duracion = pelicula_data[3]
            puntaje = pelicula_data[7]
            idioma = pelicula_data[2]
            try:
                duracion_int = int(duracion) if duracion.isdigit() else 0
            except:
                duracion_int = 0
            duracion_total += duracion_int
            peliculas_contadas += 1
            pelis_bs.append({
                "Fecha de publicación": fecha_publicacion,
                "Título original": titulo_original,
                "Presupuesto": presupuesto,
                "Ingresos": ingresos,
                "Ganancia": ganancias,
                "Duración": duracion,
                "Puntaje de calificación": puntaje,
                "Idioma original": idioma
            })
        if peliculas_contadas > 0:
            promedio_duracion = duracion_total / peliculas_contadas
        else:
            promedio_duracion = 0
        resultado = {
        "Número total de películas": peliculas_contadas,
        "Tiempo promedio de duración": promedio_duracion,
        "Películas": pelis_bs}
    return resultado

def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
