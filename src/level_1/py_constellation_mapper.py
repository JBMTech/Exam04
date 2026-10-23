

def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    """
    Escribe una función que proyecte una constelación de estrellas en una cuadrícula y devuelva la representación visual como una lista de cadenas.

    La función debe:
    - Tomar una lista de coordenadas de estrellas como tuplas (fila, columna) y el tamaño de la cuadrícula como entero
    - Devolver una lista de cadenas que represente la cuadrícula
    - Las estrellas se representan con '*' y los espacios vacíos con '.'
    - Las coordenadas de la cuadrícula comienzan en (0, 0) en la esquina superior izquierda
    - Ignorar las coordenadas fuera de los límites de la cuadrícula
    - Manejar coordenadas duplicadas (cada estrella aparece solo una vez)
    """
    grid = []

    for i in range(dim):
        row = []
        for j in range(dim):
            row.append(".")
        grid.append(row)

    for star in stars:
        row = star[0]
        col = star[1]

        if 0 <= row < dim and 0 <= col < dim:
            grid[row][col] = "*"

    result = []

    for row in grid:
        line = ""
        for cell in row:
            line += cell
        result.append(line)

    return result
