import time
from DataStructures.List import array_list as lt
import csv
import os


csv.field_size_limit(2147483647)
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    movies = {"fecha": None, "or_title": None, "idioma": None, "duaracion": None
              , "presupuesto": None, "ingresos": None,
              "ganancias": None}

    movies["fecha"] = lt.new_list()
    movies["or_title"] = lt.new_list()
    movies["idioma"] = lt.new_list()
    movies["duracion"] = lt.new_list()
    movies["presupuesto"] = lt.new_list()
    movies["ingresos"] = lt.new_list()
    movies["ganancias"] = lt.new_list()
    return movies
# Funciones para la carga de datos

def load_fecha(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        release_date = row['release_date'] if row['release_date'] else "Desconocido"
        lt.addLast(movies['fecha'], release_date)

# Función para cargar los títulos originales de las películas
def load_title(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        or_title = row['title'] if row['title'] else "Desconocido"
        lt.addLast(movies['or_title'], or_title)

# Función para cargar el idioma original de las películas
def load_idioma(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        idioma = row['original_language'] if row['original_language'] else "Desconocido"
        lt.addLast(movies['idioma'], idioma)
        
# Función para cargar la duración de las películas
def load_duracion(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        duracion = row['runtime'] if row['runtime'] else "Desconocido"
        lt.addLast(movies['duracion'], duracion)

# Función para cargar el presupuesto, ingresos y calcular ganancias
def load_financials(movies, filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for row in input_file:
        presupuesto = int(row['budget']) if row['budget'].isdigit() else 0
        ingresos = int(row['revenue']) if row['revenue'].isdigit() else 0
        lt.addLast(movies['presupuesto'], presupuesto)
        lt.addLast(movies['ingresos'], ingresos)
        lt.addLast(movies['ganancias'], ingresos - presupuesto if ingresos and presupuesto else "Indefinido")


def load_data(catalog, filename):
    load_fecha(catalog, filename)
    load_title(catalog, filename)
    load_idioma(catalog, filename)
    load_duracion(catalog, filename)
    load_financials(catalog, filename)
        
    return catalog

# Funciones de consulta sobre el catálogo

def get_data(movies, id):
    fecha = lt.getElement(movies['fecha'], id) if lt.getElement(movies['fecha'], id) else "Desconocido"
    or_title = lt.getElement(movies['or_title'], id) if lt.getElement(movies['or_title'], id) else "Desconocido"
    idioma = lt.getElement(movies['idioma'], id) if lt.getElement(movies['idioma'], id) else "Desconocido"
    duracion = lt.getElement(movies['duracion'], id) if lt.getElement(movies['duracion'], id) else "Desconocido"
    presupuesto = lt.getElement(movies['presupuesto'], id)
    ingresos = lt.getElement(movies['ingresos'], id)
    if presupuesto == 0:
        presupuesto = "Indefinido"
    if ingresos == 0:
        ingresos = "Indefinido"
    if isinstance(presupuesto, int) and isinstance(ingresos, int):
        ganancias = ingresos - presupuesto
    else:
        ganancias = "Indefinido"
    
    return [fecha, or_title, idioma, duracion, presupuesto, ingresos, ganancias]

def report_data(movies):
    total_movies = lt.size(movies['fecha'])
    first_five = [get_data(movies, i+1) for i in range(5)]
    last_five = [get_data(movies, total_movies - 4 + i) for i in range(5)]
    return total_movies, first_five, last_five

def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


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
