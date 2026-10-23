

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    """
    Escribe una función que encuentre el elemento máximo en cada
    ventana deslizante de tamaño k en un arreglo. Devuelve una
    lista de los máximos para cada posición de ventana.

    La función debe:
    - Deslizar una ventana de tamaño k a través del arreglo
    - Encontrar el elemento máximo en cada posición de la ventana
    - Devolver una lista de valores máximos
    - Manejar casos límite (arreglo vacío, k <= 0, k > longitud del arreglo)
    - Devolver una lista vacía para entradas no válidas
    """
    result = []

    if not nums or k <= 0 or k > len(nums):
        return result

    for i in range(len(nums) - k + 1):
        maximum = nums[i]

        for j in range(i + 1, i + k):
            if nums[j] > maximum:
                maximum = nums[j]

        result.append(maximum)

    return result
