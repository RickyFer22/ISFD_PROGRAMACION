# ============================================================
# CLASE 14 - Introduccion a funciones
# ============================================================
#
# TEORIA: ¿POR QUE EXISTEN LAS FUNCIONES? (tres razones de peso)
# 1) REUTILIZACION: escribir es_aprobado UNA vez y usarla en 10 lugares.
#    Si cambia la regla (aprobar con 6), se cambia EN UN LUGAR. ¿Por que es
#    critico? Porque duplicar codigo = duplicar lugares donde puede haber
#    un bug (y actualizar solo la mitad es el clasico desastre).
# 2) ABSTRACCION: quien llama a es_aprobado(nota) no necesita saber COMO
#    decide: le alcanza el QUE. Igual que vos usas len() sin saber como
#    cuenta. ¿Por que importa? Permite combinar piezas grandes sin entender
#    cada ladrillo.
# 3) PROBAR POR PARTES: una funcion aislada se prueba sola. Si el programa
#    falla, encontras el culpable probando funciones de a una.
#
# TEORIA: ANATOMIA - def, parametros, return
# def nombre(parametros):  -> DEFINE (guarda) la funcion: no se ejecuta aca.
# nombre(argumento)        -> LA LLAMA: recien ahora se ejecuta su bloque.
# return valor             -> DEVUELVE un resultado a quien llamo Y termina.
# ¿Diferencia entre print() y return? print MUESTRA en pantalla (efecto
# visible, valor perdido); return ENTREGA el valor al que llamo (invisible,
# pero utilizable). ¿Por que es LA confusion nro 1? Porque en el REPL los
# dos "se ven". Regla: una funcion que CALCULA algo -> return; print es
# tarea del programa principal.
#
# TEORIA: ¿DONDE VIVE UNA FUNCION EN MEMORIA?
# def crea un objeto funcion y una etiqueta con su nombre. Por eso se define
# ANTES de usarla: Python lee el archivo de arriba hacia abajo; si llegas a
# una llamada y la etiqueta no existe todavia -> NameError.
# Los PARAMETROS son variables locales que nacen en cada llamada con los
# valores pasados (los argumentos) y mueren al terminar.
#
# ============================================================

def es_aprobado(nota):
    """Devuelve True si la nota alcanza para aprobar (4 o más)."""
    return nota >= 4
# El docstring ("""...""") documenta QUE hace. ¿Por que ahi? Python lo guarda
# dentro de la funcion y se consulta con help(es_aprobado).

nota = float(input("Nota: "))
if es_aprobado(nota):
    print("Felicitaciones")
else:
    print("A recuperar")
# Flujo: la llamada "salta" a la funcion, la funcion calcula, return vuelve
# con True/False, y el if decide. ¿Por que sirve usarla en un if? Porque
# devuelve un bool: es una expresion utilizable como condicion.

# Reutilizacion: la MISMA funcion en un ciclo
notas = [8, 3, 6, 9, 2]
aprobadas = []
for n in notas:
    if es_aprobado(n):
        aprobadas.append(n)
print("Aprobadas:", aprobadas)
# ¿Por que aprobar 3 no rompe nada? La funcion no sabe de donde viene la
# nota: esa independencia es la abstraccion.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿Que devuelve una funcion sin return?
# R: None (el "nada" de Python). print(None) muestra None. Por eso una
#    funcion calculadora SIN return "no devuelve nada".
#
# P: ¿Puedo tener varios return?
# R: Si: se ejecuta el primero que llegue y la funcion termina ahi.
#
# P: ¿Funcion con dos salidas?
# R: return a, b devuelve una tupla; se desempaqueta: s, p = suma_promedio(x).
#
# P: ¿Parametro y argumento son lo mismo?
# R: Parametro = la variable en la definicion (nota). Argumento = el valor
#    que pasas en la llamada (8.0). Distincion fina pero real.
# ============================================================
