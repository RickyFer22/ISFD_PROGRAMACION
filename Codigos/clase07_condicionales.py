# ============================================================
# CLASE 7 - Estructuras condicionales: if / elif / else
# ============================================================
#
# TEORIA: ¿POR QUE EXISTEN LAS CONDICIONALES?
# Hasta hoy todos nuestros programas ejecutan TODAS sus lineas, siempre, en
# orden. Eso no sirve: la vida real tiene caminos distintos (aprobado o no,
# noche o dia). La condicional permite que el programa ELIJA un camino segun
# una condicion (un bool). Es el segundo pilar de la programacion:
#   1) secuencia  2) seleccion (if)  3) repeticion (while/for).
# Con estos tres se puede escribir cualquier programa que exista (teorema
# de Böhm-Jacopini, base de la "programacion estructurada").
#
# TEORIA: ¿POR QUE LA INDENTACION ES OBLIGATORIA EN PYTHON?
# En casi todos los lenguajes los bloques van entre llaves { } y la
# indentacion es opcional (estetica). Python decidio: SI YA INDENTAS PARA
# LEER, ¿por que no hacer que la indentacion SEA el bloque? Resultado:
#   - Codigo uniforme (todos indentan igual: 4 espacios, PEP 8).
#   - Menos un tipo de error clasico de C: bloque que parece de una cosa
#     y es de otra.
# Consecuencia practica: mezclar TABS y ESPACIOS da TabError. En VS Code la
# tecla Tab genera 4 espacios automaticamente: no lo cambies.
# ¿Cuales son los bloques? Todo lo indentado debajo de if/elif/else/def/while.
#
# TEORIA: ¿COMO ELIGE PYTHON QUE CAMINO TOMAR?
# if nota >= 7: -> Python EVALUA la condicion: da True o False.
#   True  -> ejecuta el bloque indentado y SALTA el resto de elif/else.
#   False -> prueba el siguiente elif; si ninguno da True -> else.
# ¿Por que solo UNA rama se ejecuta? Porque las ramas son excluyentes por
# diseño: es una decision, no una lista de tareas.
# elif = "else if": solo se evalua si lo anterior fue False (importante por
# eficiencia y porque condiciones posteriores asumen las anteriores falsas).
#
# ============================================================

nota = float(input("Nota (0 a 10): "))
if nota >= 7:
    print("Promociona")
elif nota >= 4:
    print("Aprueba")
else:
    print("Desaprobado")
# ¿Por que elif nota >= 4 y no elif nota >= 4 and nota < 7?
# Porque si llego al elif, ya sabemos que nota < 7 (el if fallo). Las
# condiciones siguientes APROVECHAN lo ya descartado. Orden descendente.

# Mayor de tres numeros
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))
mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c
print(f"El mayor es {mayor}")
# ¿Por que esta forma (campeonato) y no if/elif gigante? Porque funciona con
# cualquier cantidad de numeros y es mas facil de leer. ¿Por que dos if
# separados y no elif? Porque el segundo if depende del RESULTADO del primero:
# son comparaciones encadenadas, no caminos excluyentes.

# Menu con if/elif/else
print("1) Sumar  2) Restar  3) Multiplicar  4) Salir")
opcion = input("Elegí una opción: ")
x = float(input("Primer operando: "))
y = float(input("Segundo operando: "))
if opcion == "1":
    print("Resultado:", x + y)
elif opcion == "2":
    print("Resultado:", x - y)
elif opcion == "3":
    print("Resultado:", x * y)
elif opcion == "4":
    print("Chau!")
else:
    print("Opción inválida")
# ¿Por que comparar con "1" (texto) y no 1? input() devuelve TEXTO. ¿Por que
# el else final si ya tengo 4 casos? Para capturar CUALQUIER otra cosa: un
# buen programa nunca deja una entrada rara sin respuesta.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿Puedo tener if sin else?
# R: Si. else es opcional: si la condicion es False, simplemente no pasa nada.
#
# P: ¿Puedo anidar un if dentro de otro if?
# R: Si (if dentro del bloque de otro). Se indenta doble. Pero si hay mas de
#    2 niveles, conviene reordenar con and/or: legibilidad.
#
# P: ¿if nota >= 7 and < 4?
# R: SyntaxError: < 4 no tiene con que compararse. Cada comparacion necesita
#    su variable: nota >= 7 or nota < 4 (aunque eso siempre es... nota? no:
#    es imposible que ambas se cumplan; ojo con la logica).
#
# P: ¿Por que "elif" y no "else if" como otros lenguajes?
# R: Es el azucar sintactico de Python: else: + if indentado en una sola
#    palabra. "else if" con indentacion tambien funciona, es solo mas largo.
# ============================================================
