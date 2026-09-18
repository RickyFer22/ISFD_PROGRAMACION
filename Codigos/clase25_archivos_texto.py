# ============================================================
# CLASE 25 - Archivos de texto
# ============================================================
#
# TEORIA: ¿POR QUE ARCHIVOS? LA MEMORIA ES VOLATIL
# Todas las variables viven en RAM: cuando el programa termina, TODO se
# pierde. El archivo es la memoria PERSISTENTE: vive en el disco y sobrevive
# al programa. ¿Por que esto importa? Un registro de notas que desaparece al
# cerrar no sirve: la persistencia es lo que convierte un programa en un
# SISTEMA.
#
# TEORIA: LOS MODOS DE APERTURA - POR QUE EXISTEN TRES
#   "r" (read): leer; si no existe -> FileNotFoundError.
#   "w" (write): escribir desde cero; SI EL ARCHIVO EXISTE LO PISA ENTERO
#        sin preguntar. ¿Por que tan violento? Es el contrato del modo: w
#        significa "reemplaza el contenido". El error clasico: querer
#        agregar con "w" y borrar todo el historial.
#   "a" (append): escribir AL FINAL, creando el archivo si no existe.
#        ¿Por que separarlo? Porque "agregar un log" y "reescribir el
#        reporte" son operaciones distintas y el modo lo explicita.
#
# TEORIA: with open(...) as f - POR QUE ESTA FORMA ES LA CORRECTA
# Un archivo abierto es un recurso del sistema operativo (hay un limite de
# archivos abiertos por proceso). Si olvidas cerrarlo, puede quedar bloqueado
# o sin vaciar el buffer. with garantiza el cierre SIEMPRE, incluso si hay
# una excepcion a mitad de bloque. ¿Por que existe el BUFFER? Escribir al
# disco es lento: Python junta datos en memoria y vuelca por tandas; close()
# (o el fin del with) fuerza el vuelco. Sintoma del olvido: el archivo se ve
# vacio mientras el programa corre.
#
# TEORIA: LINEAS Y ENCODING
# Un archivo de texto es una secuencia de caracteres; las "lineas" son
# convencion: separadas por \n. for linea in f las entrega UNA POR UNA
# (eficiente: no carga el archivo entero en memoria). Cada linea trae su
# \n final: por eso strip() al mostrar/comparar.
# encoding="utf-8": el mapa bytes->caracteres. ¿Por que explicito? Sin el,
# Windows puede asumir otra tabla y los acentos se ven mal (mojibake "Ã±").
# UTF-8 es el estandar universal de la web.
#
# ============================================================

from datetime import datetime

# 1) Diario de clase: agregar con modo "a"
with open("diario.txt", "a", encoding="utf-8") as f:
    entrada = input("Anota algo de la clase: ")
    f.write(f"[{datetime.now():%Y-%m-%d %H:%M}] {entrada}\n")
print("Guardado en diario.txt")
# ¿Por que \n al final? write NO agrega salto: sin el, la proxima entrada
# quedaria pegada en la misma linea.

# 2) Leer linea por linea
with open("diario.txt", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())
# ¿Modo "r" omitido? Es el default. ¿strip()? Quita el \n de cada linea.

# 3) Notas estructuradas: escribir, leer y promediar
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("Ana;8;9\n")     # formato propio: nombre;nota;nota
    f.write("Luis;6;5\n")

with open("notas.txt", encoding="utf-8") as f:
    todas = []
    for linea in f:
        campos = linea.strip().split(";")
        nombre, notas = campos[0], [int(n) for n in campos[1:]]
        print(nombre, notas, "->", sum(notas) / len(notas))
        todas.extend(notas)   # extend agrega TODOS los elementos de la lista
print("Promedio general:", sum(todas) / len(todas))
# ¿Por que inventar un formato con ;? Porque CSV (clase 26) es exactamente
# esto con un modulo que lo formaliza. ¿append vs extend? append mete la
# lista COMO un elemento; extend vuelca los elementos sueltos.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿Leer un archivo que no existe?
# R: FileNotFoundError. Solucion profesional: try/except y decidir (usar
#    lista vacia, avisar, etc.). Lo aplicamos en la clase 26.
#
# P: ¿Puedo leer y escribir a la vez ("r+")?
# R: Existe, pero es facile equivocarse con el "cursor". Regla: abrir con UN
#    proposito por bloque with.
#
# P: ¿f.write(123)?
# R: TypeError: write exige texto. str(123) o f"{123}".
#
# P: ¿Que pasa si abro con "w" solo para leer despues?
# R: "w" PISA todo al abrir (aunque no escribas nada). Detectar el modo
#    correcto antes de abrir.
# ============================================================
