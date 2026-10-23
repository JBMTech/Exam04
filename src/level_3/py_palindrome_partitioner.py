

def palindrome_partitioner(s: str) -> int:
    """
    Dada una cadena s, encuentra el número mínimo de cortes
    necesarios para particionarla de manera que cada subcadena
    resultante sea un palíndromo.

    - Devuelve el número mínimo de cortes (un entero)
    - Una cadena de longitud 1 requiere 0 cortes
    - Una cadena vacía requiere 0 cortes
    """
    n = len(s)

    if n <= 1:
        return 0

    palindrome = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(False)
        palindrome.append(row)

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i <= 1 or palindrome[i + 1][j - 1]:
                    palindrome[i][j] = True

    cuts = []

    for i in range(n):
        cuts.append(i)

    for end in range(n):
        if palindrome[0][end]:
            cuts[end] = 0
        else:
            for start in range(1, end + 1):
                if palindrome[start][end]:
                    new_cuts = cuts[start - 1] + 1
                    if new_cuts < cuts[end]:
                        cuts[end] = new_cuts

    return cuts[n - 1]
