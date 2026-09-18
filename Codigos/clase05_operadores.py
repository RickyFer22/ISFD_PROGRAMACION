# ============================================================
# CLASE 5 - Operadores, expresiones y precedencia
# ============================================================
#
# TEORIA: ¿QUE ES UNA EXPRESION?
# Todo lo que, al evaluarse, PRODUCE UN VALOR: 2 + 2 (-> 4), nota >= 6
# (-> True), "pro" + "grama" (-> "programa"). Una instrucciones como
# x = 5 es una SENTENCIA (no produce valor: cambia el estado). Esto explica
# por que no puedes escribir print(x = 5) esperando asignar: la asignacion
# no es una expresion en Python.
#
# LOS OPERADORES ARITMETICOS Y SUS PORQUES:
#   + - *  -> como en matematica.
#   /      -> division REAL: siempre devuelve float (7 / 2 = 3.5, incluso
#             6 / 2 = 3.0). ¿Por que siempre float? Para no sorprenderte:
#             el tipo del resultado es predecible.
#   //     -> division ENTERA (floor): redondea HACIA ABAJO. 7 // 2 = 3.
#             ¿Para que sirve? Contar cuantas veces "entra" B en A:
#             cuantos paquetes de 12 entran en 100? 100 // 12 = 8.
#   %      -> RESTO (modulo): lo que SOBRA. 100 % 12 = 4.
#             Par/impar: n % 2 == 0. Ultima cifra: n % 10.
#             ¿Por que el resto resuelve tanta cosa? Porque muchos problemas
#             son "ciclos que se repiten": los dias de la semana (7), las
#             cifras (10), los minutos (60).
#   **     -> potencia: 2 ** 10 = 1024.
#
# TEORIA: PRECEDENCIA - POR QUE 2 + 3 * 4 ES 14
# Python respeta la precedencia matematica: ** > * / // % > + -.
# Igualdad de nivel -> se evalua de IZQUIERDA a DERECHA (asociatividad).
# ¿Por que existe la precedencia? Para no escribir parentesis en cada
# formula; es un acuerdo universal heredado de la matematica. Ante la duda:
# PONER PARENTESIS. Codigo claro > codigo "listo".
#
# COMPARACION Y LOGICA:
#   == igualdad, != distinto, < > <= >= -> devuelven bool (True/False).
#   and: True solo si TODAS; or: True si ALGUNA; not: invierte.
#   ¿Por que == y no =? Porque = ya significa asignacion. Es herencia de C
#   y evita el clasico bug "if (x = 5)" de otros lenguajes.
#   Cortocircuito: en A and B, si A es False, B NI SE EVALUA. ¿Por que
#   importa? Permite escribir seguro: if n != 0 and 10/n > 1: ...
#
# ============================================================

nota1, nota2 = 8, 6                 # asignacion multiple: derecha primero
promedio = (nota1 + nota2) / 2
aprobado = promedio >= 6            # comparacion -> bool
resto = 17 % 5                      # 2: lo que sobra de 17 = 3*5 + 2
print(promedio, aprobado, resto, 2 ** 10)

# Par o impar
n = int(input("Número: "))
if n % 2 == 0:
    print("Es par")
else:
    print("Es impar")
# ¿Por que funciona? Todo par es multiplo de 2 -> resto 0.

# Descuento
precio = float(input("Precio: "))
descuento = float(input("% de descuento: "))
final = precio * (1 - descuento / 100)
# ¿Por que (1 - d/100) y no precio - precio*d/100? Son equivalentes; la
# primera factoriza. 20% de descuento = quedarse con el 80% = *0.8.
print(f"Precio final: ${final:.2f}")

# Precedencia en accion
print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿-7 // 2 da -3 o -4?
# R: -4. La division entera redondea HACIA ABAJO (al entero menor), no hacia
#    el cero. El resto acompana: -7 % 2 = 1. (¡pregunta trampa clasica!)
#
# P: ¿"5" + 5?
# R: TypeError. Python no adivina: o convences vos ("5" + str(5) = "55") o
#    sumas numeros (5 + 5 = 10).
#
# P: ¿True y False son 1 y 0?
# R: De hecho SI en Python: True == 1 y False == 0 (bool es subclase de int).
#    sum([True, True, False]) = 2: por eso sumar comparaciones cuenta casos.
#
# P: ¿Operador <> para distinto?
# R: Existia en Python 2, fue ELIMINADO en Python 3. Solo !=.
# ============================================================
