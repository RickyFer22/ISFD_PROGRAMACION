# ============================================================
# CLASE 20 (TALLER) - Colecciones ordenadas en problemas
# ============================================================
#
# TEORIA: ESTADISTICA BASICA EN PYTHON
#   Promedio = sum(lista) / len(lista).
#   Mediana  = el valor del medio de la lista ORDENADA. ¿Por que ordenar?
#              Porque la mediana es posicion, no promedio: en [1, 2, 100]
#              el promedio (34) no representa a nadie; la mediana (2) si.
#              Posicion: ordenadas[len//2] (si cantidad impar).
#   Moda     = el mas repetido (con diccionario de frecuencias, clase 21).
# ¿Por que conocer los tres? Porque describen distinto el mismo dato y el
# enunciado de un problema puede pedir cualquiera.
#
# TEORIA: LISTAS PARALELAS - LA SOLUCION FRAGIL (y por que existe una mejor)
# productos = ["Teclado", "Mouse"]; precios = [12500, 8000]: el vinculo entre
# producto y precio es SOLO la posicion. Riesgos: agregar a una y no a la
# otra, ordenar una sola (¡todo se desalinea!), borrar mal. ¿Por que la
# ensenamos igual? Porque aparece en todo el mundo real (planillas heredadas)
# y porque su fragilidad MOTIVA el diccionario de la clase que viene:
# {"nombre": "Teclado", "precio": 12500} no puede desalinearse.
#
# TEORIA: sort CON CLAVE (key)
# sorted(ventas, reverse=True)[:3]: el top-N es ordenar descendente + slicing.
# ¿Y ordenar por un criterio propio? key=funcion que dice "por que comparar":
# sorted(personas, key=lambda p: p["edad"]). Lo retomamos con diccionarios.
#
# ============================================================

# 1) Encuesta de edades: promedio, mediana, mayores de edad
edades = []
for i in range(5):
    edades.append(int(input(f"Edad {i + 1}: ")))
print(f"Promedio: {sum(edades) / len(edades):.1f}")
ordenadas = sorted(edades)
print(f"Mediana: {ordenadas[len(ordenadas) // 2]}")
print(f"Mayores de edad: {sum(1 for e in edades if e >= 18)}")
# sum(1 for e in ... if e >= 18): cuenta los que cumplen (True=1). ¿Por que
# len(ordenadas)//2? Indice del medio: 5 elementos -> 5//2 = 2 (tercero).

# 2) Carrito con listas paralelas
productos = ["Teclado", "Mouse", "Monitor"]
precios = [12500, 8000, 95000]
total = 0
for i in range(len(productos)):
    print(f"{productos[i]:<10} ${precios[i]:>8}")
    total += precios[i]
print(f"TOTAL: ${total}")
# ¿Por que range(len())? Necesito el INDICE i para leer la MISMA posicion en
# las dos listas. Con zip() tambien: for prod, pre in zip(productos, precios).
# ¿Que falla si agrego "Cable" a productos y olvido su precio? IndexError al
# recorrer: la fragilidad en persona.

# 3) Top 3 de ventas
ventas = [120, 90, 300, 150, 75]
top3 = sorted(ventas, reverse=True)[:3]
print(f"Top 3: {top3}")
# [:3]: slicing sobre la lista ordenada: los tres primeros. ¿Por que
# reverse=True? Descendente: los mayores primero.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿Mediana con cantidad PAR de elementos?
# R: El promedio de los dos centrales: (ordenadas[n//2 - 1] + ordenadas[n//2]) / 2.
#
# P: ¿zip() que hace?
# R: Empareja listas elemento a elemento: zip(["a","b"], [1,2]) -> ("a",1),("b",2).
#    Se corta con la mas corta.
#
# P: ¿Por que no ordenar `edades` directamente y perder el orden de carga?
# R: sorted() devuelve copia: el original queda intacto. sort() lo pisa:
#    elegir segun si el orden de ingreso importa (en una encuesta, no).
# ============================================================
