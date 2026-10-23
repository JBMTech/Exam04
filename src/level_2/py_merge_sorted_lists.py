

def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    """
    Escribe una función que fusione múltiples listas ordenadas
    en una sola lista ordenada de forma eficiente.

    La función debe:
    - Tomar como entrada una lista de listas de enteros ordenadas
    - Devolver una única lista fusionada en orden ascendente
    - Conservar todos los elementos duplicados en el resultado final
    - Manejar listas vacías y entradas vacías de forma adecuada
    - Mantener una eficiencia óptima para entradas grandes
    """
    def merge_two(left: list[int], right: list[int]) -> list[int]:
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    current = lists[:]

    while len(current) > 1:
        merged = []
        i = 0

        while i < len(current):
            if i + 1 < len(current):
                merged.append(merge_two(current[i], current[i + 1]))
            else:
                merged.append(current[i])

            i += 2

        current = merged

    if current:
        return current[0]

    return []
