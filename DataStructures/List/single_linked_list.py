import list_node as nd

def new_list():
    newlist = {"first": None, "last":None, "size":0}
    return newlist

def add_first(lista,element):
    nodo = nd.new_single_node(element)
    if lista["size"] == 0:
        lista["first"] = nodo
        lista["size"]+=1
    else:
        primero_antes = lista["first"]
        nodo["next"] = primero_antes
        lista["first"] = nodo
        lista["size"]+=1
    return lista

def add_last(lista, element):
    nodo = nd.new_single_node(element)
    if lista["size"] == 0:
        lista["first"] = nodo
        lista["last"] = nodo
        lista["size"]+=1
    else:
        lista["last"]["next"] = nodo 
        lista["last"] = nodo
        lista["size"]+=1
    return lista

def is_empty(lista):
    if lista["size"] == 0:
        return True
    else:
        return False
    
def size(lista):
    return lista["size"]

def first_element(lista):
    if is_empty(lista) == False:
        return nd.get_element(lista["first"])

def last_element(lista):
    if is_empty(lista) == False:
        return nd.get_element(lista["last"])
    
def get_element(lista,pos):
    if pos < 0:
        raise IndexError("La posición debe ser mayor o igual a cero.")
    i = 0
    current = lista["first"]
    while i < lista["size"]:
        if i == pos:
            return nd.get_element(current)
        i+=1
        current = current["next"]
        
def delete_element(lista,pos):
    if is_empty(lista) or pos < 0 or pos >= lista["size"]:
        raise IndexError("la lista no puede estar vacia")
    else:
        i = 0
        nodo_actual = lista["first"]
        while i < pos - 1:
            nodo_actual = nodo_actual["next"]
            i += 1
        removed = nodo_actual["next"]
        nodo_actual["next"] = removed["next"]
    lista["size"] -= 1
    return lista


def interator(lista):
    current = lista["first"]
    lista_n = []
    while current != None:
        lista_n.append(nd.get_element(current))
        current = current["next"]
    return lista_n
        
        
def change_info(lista, pos, new_info):
    if pos < 0 or pos >= lista["size"]:
        raise IndexError("Posición fuera de rango.")
    if lista["first"] is None:
        raise ValueError("La lista está vacía.")
    nodo_actual = lista["first"]
    i = 0
    while i < pos:
        if nodo_actual is None:
            raise ValueError("El nodo en la posición solicitada no existe.")
        nodo_actual = nodo_actual["next"]
        i += 1
    if nodo_actual is not None:
        nodo_actual["info"] = new_info
    else:
        raise ValueError("No se puede cambiar la información de un nodo nulo.")
    return lista

def remove_first(lista):
    if is_empty(lista): 
        raise IndexError("La lista no puede estar vacía.")
    primero = lista["first"]
    if lista["first"] == lista["last"]:
        lista["first"] = None
        lista["last"] = None
    else:
        lista["first"] = primero["next"]
    lista["size"] -= 1
    return nd.get_element(primero)