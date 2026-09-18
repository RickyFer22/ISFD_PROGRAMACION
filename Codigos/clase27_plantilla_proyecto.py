# ============================================================
# CLASES 27-30 - Plantilla del TP integrador
# Gestor de alumnos y notas: EL ejemplo completo de la materia.
# Requisitos que cubre: menu + funciones documentadas + lista de
# diccionarios + validacion con excepciones + persistencia JSON + Git.
# ============================================================
#
# TEORIA: ARQUITECTURA DEL PROGRAMA - POR QUE ESTE ORDEN
#   1) Constantes arriba (ARCHIVO): datos de configuracion en un solo lugar.
#   2) Funciones de PERSISTENCIA (cargar/guardar): la unica seccion que toca
#      archivos. ¿Por que aislarlas? Si mañana cambias JSON por base de
#      datos, solo tocas estas dos funciones.
#   3) Funciones de LOGICA (alta, listado, promedio): cada una hace UNA cosa.
#   4) main(): el menu que coordina. ¿Por que se llama main? Convencion
#      universal: el "programa principal" se reconoce al instante.
# ¿Por que las funciones NO piden input salvo las interactivas? Separar
# "pedir datos" (interfaz) de "procesar datos" (logica) permite probar la
# logica sin teclear nada.
#
# TEORIA: FLUJO DEL DATO (recibir -> procesar -> devolver)
# alta(alumnos) recibe la lista, la MODIFICA (las listas son mutables y se
# pasan por referencia: no hace falta return para agregar) y main decide
# guardar. ¿Por que guardar() va en main y no adentro de alta()? Separacion
# de responsabilidades: alta agrega a memoria; persistir es otra decision.
#
# TEORIA: SORTED CON key - ORDENAR POR TU REGLA
# sorted(alumnos, key=lambda x: promedio(x), reverse=True)
# key recibe cada elemento y devuelve el VALOR por el que comparar. lambda
# es una funcion anonima de una linea: "para cada x, usa su promedio".
# ¿Por que existe key? Porque el criterio de orden lo define el problema
# (por nombre, por promedio, por precio...), no la estructura.
#
# ============================================================

import json

ARCHIVO = "alumnos_tp.json"   # constante: configuracion en un solo lugar

def cargar():
    """Carga los alumnos desde el archivo JSON (o devuelve lista vacia)."""
    try:
        with open(ARCHIVO, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []             # primera ejecucion: archivo todavia no existe

def guardar(alumnos):
    """Guarda todos los alumnos en el archivo JSON."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(alumnos, f, indent=2, ensure_ascii=False)

def pedir_nota(mensaje):
    """Pide una nota (0-10) validando con excepciones. Nunca devuelve basura."""
    while True:
        try:
            v = float(input(mensaje))
            if 0 <= v <= 10:
                return v
        except ValueError:
            pass
        print("Dato inválido")
    # ¿pass en el except? "No hago nada especial con el error": el print de
    # abajo es comun a ambos fallos (fuera de rango o no-numero).

def alta(alumnos):
    """Carga un alumno nuevo con sus tres notas."""
    nombre = input("Nombre: ").strip().title()
    notas = [pedir_nota(f"Nota {i}: ") for i in range(1, 4)]
    alumnos.append({"nombre": nombre, "notas": notas})
    print("Alumno agregado")
    # ¿comprension de listas para pedir notas? [pedir_nota(i) for i in ...]:
    # la misma estructura [f(x) for x in secuencia] de la unidad 4.

def listado(alumnos):
    """Muestra el listado con promedios, ordenado por promedio descendente."""
    for a in sorted(alumnos, key=lambda x: sum(x["notas"]) / len(x["notas"]), reverse=True):
        prom = sum(a["notas"]) / len(a["notas"])
        print(f"{a['nombre']:<20} {a['notas']} -> {prom:.1f}")

def promedio_general(alumnos):
    """Promedio general del curso."""
    if not alumnos:                 # lista vacia -> False: patron pythonico
        print("No hay alumnos")
        return
    todas = [n for a in alumnos for n in a["notas"]]
    print(f"Promedio general: {sum(todas) / len(todas):.2f}")

def main():
    """Programa principal: menu con while."""
    alumnos = cargar()
    while True:
        print("\n1) Alta  2) Listado  3) Promedio general  4) Salir")
        op = input("Opción: ")
        if op == "1":
            alta(alumnos)
            guardar(alumnos)      # persistir tras cada alta: anti Ctrl+C
        elif op == "2":
            listado(alumnos)
        elif op == "3":
            promedio_general(alumnos)
        elif op == "4":
            break
        else:
            print("Opción inválida")
    print("Hasta luego")

main()
# ¿Por que main() al final sin if? Forma completa profesional:
#   if __name__ == "__main__": main()
# __name__ vale "__main__" cuando corres ESTE archivo, y el nombre del modulo
# si lo importan: permite usarlo como libreria sin que el menu arranque solo.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE (nivel coloquio):
#
# P: ¿Por que cargar() dentro de main y no global?
# R: El flujo de datos queda explicito: main pide, recibe y pasa. Variables
#    globales esconden de donde salen las cosas.
#
# P: ¿Que pasa si dos integrantes editan el mismo archivo y hacen push?
# R: GitHub rechaza el segundo (conflicto). Se resuelve con git pull, editar
#    y volver a push. Por eso: coordinar quien toca que archivo.
#
# P: ¿Por que el README es obligatorio?
# R: La primera pregunta de cualquier persona frente a tu proyecto es "que
#    es y como lo corro". Si no esta escrito, no existe.
#
# P: ¿Como probas que guardar/cargar funciona?
# R: Alta -> salir -> volver a entrar: el dato debe seguir. Borrar el JSON y
#    repetir: debe arrancar igual (lista vacia) sin explotar.
# ============================================================
