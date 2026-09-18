# ============================================================
# CLASE 19 - Listas y tuplas
# ============================================================
#
# TEORIA: ¿QUE ES UNA LISTA EN MEMORIA?
# Una variable comun guarda UN valor. Una lista es una secuencia de
# referencias con orden: [8, 6, 9] son tres casilleros numerados 0,1,2.
# ¿Por que existen? La alternativa (nota1, nota2, nota3, ...) no escala:
# ¿30 notas? ¿1.000 alumnos? La lista + el for son la pareja perfecta:
# la lista AGRUPA, el for RECORRE.
# MUTABLE: append/insert/remove/sort cambian la lista ORIGINAL (en el lugar).
# ¿Por que importa? lista.sort() devuelve None (ordena "in place"):
# x = lista.sort() es el bug clasico (x queda None). Copia ordenada: sorted().
#
# METODOS Y COSTO (intuicion):
#   append: al final, rapido. insert(0, x): mover TODOS los elementos:
#   caro. remove(x): busca y corre todos los siguientes: caro. ¿Por que te
#   cuento esto? Porque en programas grandes, la estructura elegida define
#   la velocidad (lo formalizan con "complejidad" en 2do año).
#
# TEORIA: ¿LISTA O TUPLA? EL CRITERIO
# Ambas son secuencias ordenadas e indexables. Diferencia: la tupla es
# INMUTABLE (no se cambia despues de crear). ¿Cuando cada una?
#   Lista: colecciones que VARÍAN (notas del curso, carrito).
#   Tupla: datos que van JUNTOS y no cambian (una fecha, coordenadas, el
#          retorno multiple de una funcion).
# ¿Por que molestarse con tuplas? Proteccion (nadie las pisa por error) y
# semantica: leen "esto es fijo". Los diccionarios las usan como claves.
#
# LISTAS POR COMPRENSION
# [n for n in notas if n >= 6] = "armá la lista de los n en notas con n>=6".
# ¿Por que existe esta sintaxis? Es la traduccion directa de la descripcion
# matematica de conjuntos {n en notas : n >= 6}. Mas corta Y mas clara para
# transformaciones simples. ¿Limite? Si necesita dos condiciones anidadas
# o mucho calculo, un for clasico se lee mejor.
#
# ============================================================

notas = [8, 6, 9, 4]
notas.append(7)                       # agrega al final
promedio = sum(notas) / len(notas)    # sum() y len(): funciones para listas
aprobadas = [n for n in notas if n >= 6]
print(sorted(notas), promedio, aprobadas)
# ¿sorted vs sort? sorted(lista) devuelve NUEVA ordenada; lista.sort() ordena
# la original y devuelve None. Elegir segun si necesitas conservar el orden
# original (sorted) o no (sort, ahorra memoria).

for i, n in enumerate(notas):
    print(f"Nota {i + 1}: {n}")
# enumerate entrega indice + valor juntos. ¿Por que i + 1? Para mostrar la
# posicion humana (empezando en 1) sin tocar el indice real.

lista = [3, 1, 2]
lista.insert(1, 99)     # en posicion 1, corrido el resto a la derecha
lista.remove(2)         # quita el PRIMER 2 que encuentra
ultimo = lista.pop()    # quita y DEVUELVE el ultimo
lista.sort()
print(lista, ultimo)

punto = (10, 20)
x, y = punto            # desempaquetado
print(f"x={x}, y={y}")
# punto[0] = 5  # TypeError: 'tuple' object does not support item assignment

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿lista[-1]?
# R: El ultimo elemento. lista[-2] el penultimo. Igual que en cadenas.
#
# P: ¿remove de un elemento que no existe?
# R: ValueError: list.remove(x): x not in list. Cuidado: probar con in antes
#    (if x in lista: lista.remove(x)).
#
# P: ¿Puedo ordenar de mayor a menor?
# R: lista.sort(reverse=True) o sorted(lista, reverse=True).
#
# P: ¿b = a copia la lista?
# R: NO: copia la ETIQUETA. a y b apuntan a LA MISMA lista: cambiar via b
#    cambia "a" tambien. Copia real: b = a.copy() o b = a[:].
# ============================================================
