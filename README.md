# Algoritmo CYK - Análisis de Complejidad

Este repositorio contiene una implementación del **algoritmo CYK** en Python para determinar si una cadena pertenece al lenguaje definido por una gramática libre de contexto en forma normal de Chomsky.

## Implementación

El archivo `cyk_algorithm.py` contiene la implementación del algoritmo CYK. La gramática utilizada incluye producciones terminales y no terminales, y puede probar diferentes cadenas y gramáticas.

## Instalación y ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Zephyrodes/Complejidad-Algoritmo-CYK.git
   cd cyk-algorithm

2. Ejecuta el algoritmo:
   ```bash
   python3 cyk_algorithm.py

## Pruebas de complejidad

Este proyecto incluye diferentes pruebas para evaluar la complejidad del algoritmo desde varias perspectivas: temporal, espacial, I/O, paralelización y más.

1. Complejidad Temporal

La complejidad temporal del algoritmo CYK es \(O(n^3 \cdot |G|)\), donde \(n\) es la longitud de la cadena y \(|G|\) es el número de reglas en la gramática.
