def cyk_algorithm(grammar, string):
    # Inicializar la tabla CYK
    n = len(string)
    r = len(grammar)
    table = [[set() for _ in range(n)] for _ in range(n)]
    
    # Llenar la tabla para los símbolos terminales
    for i in range(n):
        for lhs, rhs in grammar.items():
            if string[i] in rhs:
                table[i][i].add(lhs)

    # Rellenar la tabla para las producciones no terminales
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            for k in range(i, j):
                for lhs, rhs in grammar.items():
                    for production in rhs:
                        if len(production) == 2:
                            B, C = production
                            if B in table[i][k] and C in table[k+1][j]:
                                table[i][j].add(lhs)

    # Verificar si el símbolo inicial está en la parte superior derecha de la tabla
    return 'S' in table[0][n-1]

# Gramática en forma normal de Chomsky
grammar = {
    'S': [['NP', 'VP']],
    'NP': [['D', 'N']],
    'VP': [['V', 'NP']],
    'D': [['the'], ['a']],
    'N': [['cat'], ['dog']],
    'V': [['sees'], ['pets']]
}

# Cadena a verificar
string = "the cat sees a dog".split()

# Ejecutar el algoritmo CYK
result = cyk_algorithm(grammar, string)
print("¿La cadena pertenece al lenguaje?:", result)
