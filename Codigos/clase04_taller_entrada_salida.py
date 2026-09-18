# ============================================================
# CLASE 4 (TALLER) - Entrada, salida y tipos en problemas reales
# ============================================================
#
# TEORIA: EL PATRON E-P-S (Entrada - Proceso - Salida)
# Casi todo programa de 1er ano sigue este patron:
#   ENTRADA:  pedir datos al usuario (input) o leerlos de un archivo.
#   PROCESO:  calcular/transformar esos datos (las formulas).
#   SALIDA:   mostrar resultados (print) o guardarlos (archivos).
# ¿Por que pensar asi? Porque ANTES de escribir codigo conviene responder:
# ¿que datos entran? ¿que transformo? ¿que debe salir? Si no puedes
# responder eso en una frase, todavia no entendiste el problema.
#
# TEORIA: FORMATO DE SALIDA - POR QUE :.2f
# f"{promedio:.2f}" significa "mostralO como float con 2 decimales fijos".
# ¿Por que no round(promedio, 2)? round() CAMBIA el valor (devuelve otro
# float, y 2.675 -> 2.67 por el tema binario); :.2f solo cambia COMO SE
# MUESTRA, el valor interno queda intacto. Para mostrar, formatear; para
# seguir calculando, dejar el valor real.
#
# TEORIA: INTERCAMBIO DE VARIABLES - EL TRUCO DE PYTHON
# En otros lenguajes intercambiar requiere una variable auxiliar:
#   temp = a; a = b; b = temp
# Python permite a, b = b, a porque arma internamente una TUPLA con los
# valores de la derecha y luego los desempaqueta. Se evalua PRIMERO toda la
# derecha, DESPUES se asigna: por eso no se pierde ningun valor.
#
# ============================================================

# --- EJERCICIO 1: promedio de tres notas ---
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
print(f"Promedio: {(n1 + n2 + n3) / 3:.2f}")
# ¿Por que los parentesis? Sin ellos: n1 + n2 + (n3 / 3) por precedencia.
# ¿Por que float y no int? Las notas pueden ser 7.5. ¿Cuando int? Contadores
# de personas/objetos: no existen 2.5 alumnos.

# --- EJERCICIO 2: conversor de pesos a dolares ---
cotizacion = float(input("Cotización del dólar: "))
monto = float(input("Monto en pesos: "))
print(f"Equivalen a US$ {monto / cotizacion:.2f}")
# ¿Por que pedir la cotizacion en vez de dejarla fija? Porque cambia a diario:
# el programa sirve SIEMPRE sin tocar el codigo. Separar datos de logica.

# --- EJERCICIO 3: perimetro y area de un rectangulo ---
base = float(input("Base: "))
altura_r = float(input("Altura: "))
print(f"Perímetro: {2 * (base + altura_r)}  |  Área: {base * altura_r}")
# ¿Por que perimetro es 2*(b+h)? Son dos lados b y dos lados h: b+b+h+h.

# --- EJERCICIO 4: intercambio sin auxiliar ---
a, b = 10, 20
a, b = b, a
print("a =", a, "| b =", b)

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿Por que int(input()) falla si escribo 7.5?
# R: int() solo convierte texto de enteros validos ("7.5" tiene punto).
#    Solucion: float(input()) y si necesitas entero, int(float(input())).
#
# P: ¿Por que f"..." y no str() + concatenar con +?
# R: "El total es " + str(total) funciona, pero es tedioso y propenso a
#    errores (olvidar un str()). Las f-strings convierten automaticamente
#    y permiten formato (:.2f, alineacion).
#
# P: ¿Que pasa si el usuario escribe letras en un float(input())?
# R: ValueError: could not convert string to float. Aun no lo sabemos
#    manejar: es el tema EXCEPCIONES (clase 24). Mencionar y avanzar.
# ============================================================
