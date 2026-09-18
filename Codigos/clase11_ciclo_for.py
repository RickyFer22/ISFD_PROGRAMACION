# ============================================================
# CLASE 11 - Ciclo for, range() y ciclos anidados
# ============================================================
#
# TEORIA: ¿COMO FUNCIONA range() DE VERDAD?
# range(inicio, fin, paso) NO es una lista: es un "objeto perezoso" que
# produce los numeros DE A UNO cuando for los pide. Por eso range(1, 1000000)
# no consume memoria: no guarda el millon, sabe calcular el siguiente.
# Reglas: inicio INCLUIDO, fin EXCLUIDO, paso por defecto 1.
# ¿Por que el fin es excluyente? Para que range(len(lista)) recorra indices
# exactos (0..len-1) y para que range(1, 11) tenga exactamente 10 elementos
# (11 - 1). ¿Como se memoriza? range(a, b) -> a, a+1, ..., b-1.
#
# TEORIA: ¿FOR O WHILE? LA REGLA
# ¿Sabes cuantas vueltas (o estas recorriendo una coleccion)? -> for.
# ¿Depende de algo que pasa DURANTE la ejecucion (entrada del usuario)? -> while.
# ¿Por que existe for si while puede hacer todo? Legibilidad y seguridad:
# for NO puede quedarse infinito por olvidar actualizar (no hay variable
# de control manual: range se mueve solo).
#
# TEORIA: CICLOS ANIDADOS - EL RELOJ
# for exterior = horas (12 vueltas), for interior = minutos (60 por hora).
# Por CADA vuelta del exterior, el interior da TODAS sus vueltas: 12 x 60.
# ¿Para que sirve? Tablas de doble entrada (producto x sucursal), matrices,
# kombinaciones. Costo: vueltas totales = exterior x interior. ¿Por que
# importa? 1000 x 1000 = un millon de vueltas: los ciclos anidados son la
# primera fuente de programas "lentos".
#
# BREAK Y CONTINUE
# break: corta TODO el ciclo YA. continue: salta A LA SIGUIENTE vuelta.
# ¿Por que existen? Salidas anticipadas por reglas de negocio ("encontre lo
# que buscaba: dejar de buscar").
#
# ============================================================

# 1) Suma de los primeros N naturales
n = int(input("N: "))
suma = 0
for i in range(1, n + 1):      # n+1 ¡porque el fin es excluyente!
    suma += i
print(f"Suma de 1 a {n}: {suma}")
# ¿Por que n + 1? Queremos incluir n: range(1, n) llegaria hasta n-1.
# Dato: Gauss de nino lo resolvio sin ciclo: n*(n+1)/2. Probar ambos.

# 2) Tabla de doble entrada
productos = ["Gaseosa", "Pan", "Leche"]
sucursales = ["Centro", "Norte"]
ventas = [[120, 90], [50, 75], [200, 180]]
print(f"{'':10}", end="")
for s in sucursales:
    print(f"{s:>8}", end="")
print()
for i, p in enumerate(productos):
    print(f"{p:10}", end="")
    for j in range(len(sucursales)):
        print(f"{ventas[i][j]:>8}", end="")
    print()
# ¿Por que end=""? print() salta linea por defecto; end="" le dice "no saltes:
# sigo en la misma linea". ¿Por que :10 y :>8? Formato: ancho fijo, numeros
# alineados a la derecha -> columnas prolijas.

# 3) Contar vocales recorriendo la frase
frase = input("Frase: ").lower()
vocales = 0
for letra in frase:
    if letra in "aeiou":
        vocales += 1
print(f"Tiene {vocales} vocales")
# ¿for letra in frase? for recorre CUALQUIER secuencia: una frase es una
# secuencia de caracteres. ¿Por que .lower()? Para contar tambien las
# mayusculas: normalizamos primero (siempre normalizar antes de comparar).

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿range(10), range(1, 10), range(0, 10, 2)?
# R: 0..9; 1..9; 0,2,4,6,8. Y range(10, 0, -1) cuenta al reves: 10..1.
#
# P: ¿Por que range(len(lista)) y no range(1, len(lista)+1)?
# R: Los indices empiezan en 0. La posicion humana 1 es el indice 0.
#
# P: ¿break sale de los dos ciclos anidados?
# R: No: solo del mas interno. Para salir de ambos se usan banderas o
#    reestructurar el codigo en una funcion con return.
#
# P: ¿Puedo modificar la lista mientras la recorro?
# R: Mala idea: los indices se corren y te salteas elementos. Patron
#    correcto: recorrer una copia o armar una lista nueva.
# ============================================================
