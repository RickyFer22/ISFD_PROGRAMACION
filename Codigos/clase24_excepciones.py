# ============================================================
# CLASE 24 - Excepciones: programas robustos
# ============================================================
#
# TEORIA: ¿QUE ES UNA EXCEPCION, DE VERDAD?
# Cuando Python encuentra un problema en ejecucion (dividir por cero,
# convertir "hola" a int), no "se cuela" el error: SE LANZA UN OBJETO
# EXCEPCION (ValueError, TypeError...) que, si nadie lo atiende, sube hasta
# cortar el programa con un Traceback (la pila de llamadas donde ocurrio).
# ¿Por que diseño tan dramático? Porque separa el CAMINO FELIZ del manejo
# de errores: el codigo principal no se ensucia con chequeos en cada linea,
# y los errores se atienden DONDE tiene sentido atenderlos.
# try/except = "intenta esto; SI se lanza una excepcion de este tipo, haz
# esto otro". else: corre si NO hubo error. finally: corre SIEMPRE (cierre
# de recursos).
#
# TEORIA: ¿POR QUE EXCEPT ValueError Y NO EXCEPT "A SECAS"?
# except solo atrapa TODO, incluidos tus propios bugs de tipeo (NameError):
# el programa "funciona" ocultando errores reales. ¿Principio? Atrapar SOLO
# lo que sabes manejar y dejar que lo inesperado explote ruidosamente
# (fail loud). ¿Por que ValueError para int("hola")? Python lanza ese tipo
# cuando el VALOR no es convertible (la sintaxis de tu codigo estaba bien).
#
# TEORIA: VALIDAR CON IF O CON TRY? LA REGLA PROFESIONAL
# Regla EAFP vs LBYL: "Es mas facil pedir perdon que permiso" (EAFP, estilo
# Python: try y si falla, except) vs "mira antes de saltar" (LBYL: if).
# ¿Cuando cada uno? LBYL para condiciones simples y baratas (if 0 <= x <= 10);
# EAFP cuando la verificacion es cara o con condiciones de carrera (leer un
# archivo que puede desaparecer entre el chequeo y la lectura: try directo).
# La regla practica de la materia: entradas del usuario -> try/int; logicas
# de negocio -> if.
#
# ============================================================

# 1) Lectura protegida basica
try:
    n = int(input("Número: "))
except ValueError:
    print("Eso no es un número")
else:
    print("Cuadrado:", n ** 2)
# ¿Por que el print de adentro de else y no de try? Minimizar el try: solo
# la linea que PUEDE fallar. Si pones mas codigo adentro, un error lejano
# seria tragado por el mismo except y confundiria el diagnostico.

# 2) Repetir hasta dato valido (el patron definitivo de entrada)
while True:
    try:
        nota = float(input("Nota (0-10): "))
        if 0 <= nota <= 10:
            break
        print("Fuera de rango")
    except ValueError:
        print("Eso no es un número")
print("Nota aceptada:", nota)
# ¿Por que while True + break? Tres salidas posibles (valido, fuera de
# rango, no-numero): una condicion de while seria un monstruo de or/and.

# 3) Division protegida + finally
try:
    a, b = 10, 0
    print(a / b)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Esto se ejecuta siempre")
# ¿Para que sirve finally si ya se ejecuto el except? Garantia: recursos que
# deben cerrarse pase lo que pase (archivos, conexiones). Con archivos
# usaremos with, que es la version elegante de esa idea.

# Regla de la materia: nunca validar con try lo que se puede validar con if.
# try es para lo IMPREDECIBLE (el usuario, el disco, la red), no para la
# logica que ya conoces.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿Puedo tener varios except?
# R: Si: except ValueError: ... except KeyError: ... se evaluan en orden y
#    atiende el primero que coincida.
#
# P: ¿Como ver EL MENSAJE del error adentro del except?
# R: except ValueError as e: print("Detalle:", e). Muy util para logs.
#
# P: ¿El Traceback es el enemigo?
# R: Al contrario: es el diagnostico. Leerlo de abajo hacia arriba: la ultima
#    linea dice QUE tipo de error y su mensaje; las anteriores, DONDE.
#
# P: ¿Una excepcion puede quedar sin manejar?
# R: Si: sube funcion a funcion hasta cortar el programa. Eso es CORRECTO si
#    nadie sabe que hacer con ella.
# ============================================================
