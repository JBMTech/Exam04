

def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    """
    Escribe una función que encuentre la intersección de varias
    listas ordenadas. Devuelve una nueva lista que contenga los
    elementos que aparecen en TODAS las listas de entrada, en orden ordenado.

    La función debe:
    - Devolver los elementos que aparecen en TODAS las listas
    - El resultado debe estar ordenado en orden ascendente
    - Eliminar duplicados del resultado
    - Manejar adecuadamente las entradas vacías o listas vacías
    - Si alguna lista está vacía, la intersección está vacía
    """
    result = []

    if not lists:
        return result

    for number in lists[0]:
        found = True

        for current_list in lists:
            if number not in current_list:
                found = False
                break

        if found and number not in result:
            result = result + [number]

    return result
