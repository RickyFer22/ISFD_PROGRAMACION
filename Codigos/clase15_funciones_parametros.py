# ============================================================
# CLASE 15 - Funciones: parametros, retorno y ambito
# ============================================================
#
# TEORIA: AMBITO (SCOPE) - ¿POR QUE LAS VARIABLES DE UNA FUNCION NO SE VEN AFUERA?
# Cada llamada a una funcion crea su propio "espacio de nombres" local.
# Una variable creada adentro vive SOLO durante esa llamada y muere al
# terminar (return). ¿Por que Python hace esto? PROTECCION: si cada funcion
# pudiera pisar las variables de las demas, un programa grande seria
# ingobernable (colisiones de nombres). La regla de lectura: Python busca
# el nombre PRIMERO en el ambito local; si no esta, en el global (regla LEGB
# simplificada: Local, Enclosing, Global, Built-in).
# ¿Por que evitar variables globales en funciones? Porque entonces la
# funcion depende del "estado del mundo": mismo argumento podria dar
# resultados distintos -> imposible de probar y razonar.
#
# TEORIA: PARAMETROS CON VALOR POR DEFECTO
# def presentacion(nombre, curso="1er Año"): si quien llama no pasa curso,
# se usa el default. ¿Por que existe? Para funciones con opciones comunes:
# la llamada corta sirve para el caso tipico y el detallado para el raro.
# REGLA DE ORO: los parametros con default van DESPUES de los obligatorios
# (def f(a, b=2) ok; def f(a=1, b) es SyntaxError: ¿como saber si f(3) es
# para a o para b?).
# Argumentos posicionales (por orden) vs nombrados (curso="X"): los nombrados
# permiten pasar en cualquier orden y autodocumentan la llamada.
#
# TEORIA: UNA FUNCION, UNA RESPONSABILIDAD
# Si no podes describir tu funcion en una frase sin decir "y", probablemente
# sean dos funciones. ¿Por que? Funciones chicas se prueban, se entienden y
# se reutilizan mejor. Es el principio单一 responsabilidad aplicado.
#
# ============================================================

def presentacion(nombre, curso="1er Año"):
    """Devuelve una presentación formal."""
    return f"{nombre} — {curso}"

print(presentacion("Ricardo", curso="Profesor"))   # argumento nombrado
print(presentacion("Ana"))                          # usa el default
# ¿Por que el resultado se imprime afuera? La funcion SOLO construye y
# devuelve el texto: decidir que hacer con el es del que llama.

def doble(n):
    resultado = n * 2     # 'resultado' es LOCAL
    return resultado

print(doble(21))
# print(resultado)  # NameError: 'resultado' no existe fuera de la llamada.
# ¿Por que NO existe? El ambito local se destruyo al terminar la llamada.

# Validador reutilizable: while + return + parametro default
def pedir_nota(mensaje="Nota (0-10): "):
    """Pide una nota y repite hasta que sea un numero entre 0 y 10."""
    while True:
        try:
            valor = float(input(mensaje))
            if 0 <= valor <= 10:
                return valor           # return corta el while: salida limpia
            print("Debe estar entre 0 y 10")
        except ValueError:
            print("Eso no es un número")

print("Nota cargada:", pedir_nota())
# ¿Por que while True + return en vez de una condicion de while? La condicion
# de salida depende de DOS cosas (numero valido y en rango): es mas claro
# "ciclar para siempre; cuando el dato sirva, RETURN". return adentro de un
# while corta el while tambien: termina la funcion entera.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿Puedo modificar una global desde una funcion?
# R: Solo leyendo. Para reasignar necesitas global x (existe, pero esta
#    MAL VISTO: rompe la independencia de la funcion).
#
# P: ¿El default se evalua cada llamada?
# R: NO: se evalua UNA vez al definir. Con valores inmutables (números,
#    strings) no importa; con listas da sorpresas (el default mutable "se
#    acuerda" de cambios entre llamadas). Regla: nunca listas como default.
#
# P: ¿Que pasa si llamo con mas argumentos que parametros?
# R: TypeError: presentacion() takes from 1 to 2 positional arguments but
#    3 were given. Python verifica la cantidad.
# ============================================================
