# ============================================================
# CLASE 3 - Variables y tipos de datos
# ============================================================
#
# TEORIA: ¿QUE ES REALMENTE UNA VARIABLE?
# La memoria RAM es una cadena enorme de casilleros numerados (direcciones).
# Un valor (por ejemplo el numero 33) vive en alguno de esos casilleros.
# Una VARIABLE es una ETIQUETA con nombre que apunta a ese casillero.
# ¿Por que etiquetas? Porque recordar "el valor que esta en la direccion
# 0x7ffe..." es imposible para un humano. nombre = "Ana" crea el valor y
# una etiqueta 'nombre' que lo referencia.
#
# ¿POR QUE EN PYTHON NO DECLARO EL TIPO (int edad;)?
# Porque Python es de TIPADO DINAMICO: el tipo pertenece al VALOR, no a la
# etiqueta. edad = 33 -> la etiqueta apunta a un int. Si manana haces
# edad = "treinta", la misma etiqueta apunta a un str. El tipo se verifica
# EN EJECUCION, no al escribir. Ventaja: menos codigo, mas flexibilidad.
# Riesgo: errores de tipo aparecen cuando el programa corre (por eso
# validamos con try/except mas adelante).
#
# ¿POR QUE input() DEVUELVE SIEMPRE TEXTO?
# Porque input() lee LO QUE LA PERSONA ESCRIBE EN EL TECLADO, y el teclado
# produce caracteres, no numeros. "33" son DOS caracteres ('3' y '3').
# ¿Por que entonces 33 + "33" no es 66 ni "3333"? Porque sumar int + str es
# ambiguo y Python prefiere no adivinar: lanza TypeError. TU decides la
# conversion: int("33") -> 33. Eso se llama CASTING (conversion de tipo).
# ¿Y si la persona escribe "hola" y haces int("hola")? ValueError. Por eso
# mas adelante usamos try/except para proteger estas conversiones.
#
# LOS TIPOS FUNDAMENTALES:
#   int  -> enteros: 33, -7, 0. Sin limite de tamano en Python (¡puedes
#           calcular 2**1000!). ¿Por que? Python maneja el desborde solo.
#   float-> decimales: 1.75, -0.5. OJO: los floats tienen precision limitada
#           (binario): 0.1 + 0.2 da 0.30000000000000004. ¿Por que? Los
#           decimales se guardan en base 2 y 0.1 no tiene representacion
#           binaria exacta (como 1/3 en decimal). No es un bug de Python:
#           pasa en casi todos los lenguajes.
#   str  -> texto: "Ana". INMUTABLE: no se puede cambiar un caracter; los
#           metodos devuelven cadenas NUEVAS.
#   bool -> True o False (con mayuscula: son palabras reservadas). Es el
#           tipo de las comparaciones: 3 > 2 devuelve True.
#
# ============================================================

edad = int(input("¿Cuántos años tenés? "))     # texto -> int
altura = float(input("Altura en metros: "))    # texto -> float
es_alumno = True                               # bool

print(type(edad), edad, altura, es_alumno)
# type() devuelve el tipo actual del valor: la herramienta para "ver" tipos.

print(f"Naciste aproximadamente en {2026 - edad}")

# Diferencia clave valor numerico vs texto que parece numero:
print("10" == 10)   # False: el texto "10" (2 caracteres) NO es el numero 10.
print(int("10") == 10)  # True: convertimos texto a numero.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿Que pasa si declaro dos veces la misma variable?
# R: No hay "declarar": la segunda asignacion REAPUNTA la etiqueta al nuevo
#    valor. El valor anterior queda sin etiqueta y el recolector de basura
#    (garbage collector) lo elimina de memoria automaticamente.
#
# P: ¿Por que True con mayuscula?
# R: Porque True/False/None son CONSTANTES del lenguaje (keywords), y la
#    convencion de Python para keywords es minuscula... salvo estas tres,
#    herencia del diseno original. True/False con minuscula dan NameError.
#
# P: ¿Puedo poner acentos o ñ en nombres de variables?
# R: Desde Python 3 si es valido, pero NO se hace: las convenciones (PEP 8)
#    piden minusculas y guion bajo: anio_nacimiento, no año ni AnioNacimiento.
#    ¿Por que anio y no año? Por compatibilidad y legibilidad universal.
#
# P: ¿Variable llamada print o input?
# R: Tecnicamente puedes, pero PISAS la funcion nativa: despues print("x")
#    daria TypeError. Nunca uses nombres de funciones del lenguaje.
#
# P: ¿Por que 0.1 + 0.2 != 0.3?
# R: Representacion binaria de decimales. Para dinero exacto se usan otras
#    tecnicas (modulo decimal); para nuestra materia, formatear con :.2f.
# ============================================================
