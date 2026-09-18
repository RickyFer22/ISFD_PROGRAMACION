# ============================================================
# CLASE 26 (TALLER) - CSV y JSON: persistencia estructurada
# ============================================================
#
# TEORIA: CSV - LA TABLA COMO TEXTO
# CSV (Comma-Separated Values): cada linea = un registro; campos separados
# por comas (o ; segun la config regional: ¡Excel Argentina usa ;!). ¿Por
# que CSV domina el intercambio de datos? Es texto plano: lo abren todos los
# sistemas (Excel, bases de datos, otros lenguajes). ¿Su limite? Solo TABLAS
# planas: sin estructuras anidadas ni tipos (todo es texto).
# csv.DictReader entrega cada fila como DICCIONARIO usando la primera linea
# como claves: nombre;precio -> {"nombre": ..., "precio": ...}. ¿Por que es
# elegante? Tu codigo habla de "precio", no de campos[1]: autodocumentado.
#
# TEORIA: JSON - LOS DATOS CON FORMA DE PYTHON
# JSON (JavaScript Object Notation): estandar de texto para datos
# estructurados; es EL formato de las APIs web y de la configuracion moderna.
# La correspondencia es directa:
#   lista  Python <-> array    JSON
#   dict   Python <-> objeto   JSON
#   str/int/float/bool/None <-> string/number/true/false/null
# json.dump(datos, f): objetos Python -> archivo. json.load(f): archivo ->
# objetos Python EXACTAMENTE con la misma estructura (listas de diccionarios
# reviven como listas de diccionarios). ¿Por que es magico? La persistencia
# deja de ser "parsear lineas": guardas y cargas ESTRUCTURAS.
# indent=2: formato legible para humanos; ensure_ascii=False: acentos reales
# en vez de \u00e1. ¿Por que existe ensure_ascii? El JSON clasico es ASCII
# puro; con False el archivo pesa menos y se lee mejor.
#
# TEORIA: EL PATRON DEL ABM PERSISTENTE
# 1) CARGAR al iniciar (JSON -> memoria). ¿Y si no existe el archivo?
#    Primera ejecucion: except FileNotFoundError -> lista vacia. ¿Por que no
#    es un error fatal? Porque "todavia no hay datos" es un estado NORMAL.
# 2) TRABAJAR en memoria (rapido: listas/dicts en RAM).
# 3) GUARDAR al salir (memoria -> JSON).
# ¿Por que no escribir al disco en cada operacion? Seguridad vs velocidad:
# para la materia, guardar al salir + guardar tras cada alta (higiene).
#
# ============================================================

import json

# --- JSON basico: guardar y cargar ---
alumnos = [{"nombre": "Ana", "notas": [8, 9]}, {"nombre": "Luis", "notas": [6, 5]}]

with open("alumnos.json", "w", encoding="utf-8") as f:
    json.dump(alumnos, f, indent=2, ensure_ascii=False)

with open("alumnos.json", encoding="utf-8") as f:
    datos = json.load(f)
print("Leído del archivo:", datos)
# Abrí alumnos.json con el bloc de notas: ¿parece Python? Casi: es JSON.
# Diferencias: true/false/null en minuscula, y todo entre comillas dobles.

# --- ABM completo con persistencia ---
def cargar():
    try:
        with open("productos.json", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []          # primera ejecucion: no hay datos todavia

def guardar(productos):
    with open("productos.json", "w", encoding="utf-8") as f:
        json.dump(productos, f, indent=2, ensure_ascii=False)

productos = cargar()
while True:
    print("\n1) Alta  2) Listado  3) Baja  4) Salir")
    op = input("Opción: ")
    if op == "1":
        nombre = input("Producto: ")
        precio = float(input("Precio: "))
        productos.append({"nombre": nombre, "precio": precio})
    elif op == "2":
        for p in productos:
            print(f"{p['nombre']:<20} ${p['precio']:.2f}")
    elif op == "3":
        nombre = input("Producto a eliminar: ")
        productos = [p for p in productos if p["nombre"] != nombre]
    elif op == "4":
        break
guardar(productos)
print("Datos guardados en productos.json")
# ¿Por que la baja usa comprension de listas? Filtra y reasigna: los que NO
# coinciden sobreviven. ¿Limitacion? Borra TODOS los que coincidan (para el
# proyecto: borrar por codigo unico).

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿CSV o JSON: cual elijo?
# R: Tabla plana para Excel -> CSV. Estructuras anidadas (listas dentro de
#    dicts) o para API/web -> JSON.
#
# P: ¿json.load de un archivo con sintaxis rota?
# R: json.JSONDecodeError (subclase de ValueError). El archivo se edito a
#    mano y quedo mal: es el caso tipico.
#
# P: ¿Puedo guardar objetos propios (funciones, clases)?
# R: No en JSON: solo los tipos basicos. Para objetos existe pickle, pero
#    JSON es universal e intercambiable con otros lenguajes.
#
# P: ¿Por que el ABM "no recuerda" si cortan con Ctrl+C?
# R: El guardado estaba al salir del ciclo: una salida violenta se lo salta.
#    Solucion del proyecto: guardar tambien despues de cada alta/baja.
# ============================================================
