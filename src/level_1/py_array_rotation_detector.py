

def array_rotation_detector(arr1: list, arr2: list) -> bool:
    """
    Escribe una función en Python que tome dos listas (matrices) como parámetros y determine si la segunda lista es una rotación de la primera (hacia la izquierda o hacia la derecha).

    Una rotación significa que los elementos se desplazan de forma circular. Por ejemplo, desplazar [1, 2, 3] a la derecha una posición da como resultado [3, 1, 2].

    La función debe devolver True si arr2 es una rotación de arr1, y False en caso contrario.
    Si las matrices tienen longitudes diferentes, no pueden ser rotaciones entre sí.
    Dos matrices vacías se consideran rotaciones entre sí.
    """
    if len(arr1) != len(arr2):
        return False

    if not arr1 and not arr2:
        return True

    return str(arr2)[1:-1] in str(arr1 + arr1)[1:-1]
