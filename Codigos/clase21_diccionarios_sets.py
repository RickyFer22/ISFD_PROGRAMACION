# ============================================================
# CLASE 21 - Diccionarios y conjuntos
# ============================================================
#
# TEORIA: EL DICCIONARIO - BUSQUEDA POR NOMBRE, NO POR POSICION
# Hasta hoy para encontrar "Ana" en una lista tenias que RECORRERLA
# (posicion 0, 1, 2...). El diccionario mapea CLAVE -> VALOR:
#   alumno = {"nombre": "Ana", "notas": [8, 9]}
# ¿Por que es revolucionario? Consulta directa por clave: alumno["nombre"].
# Internamente usa una TABLA HASH: la clave se convierte en una posicion de
# memoria mediante una funcion matematica -> buscar es casi instantaneo
# (tiempo constante), sin importar el tamano. ¿Por que las claves deben ser
# inmutables (str, numeros, tuplas)? Porque si la clave pudiera cambiar
# despues de guardar, su posicion hash cambiaria y el dato se "perderia".
# ¿Por que desde Python 3.7 conservan el orden de insercion? Garantia del
# lenguaje: lo que ves en el orden en que lo cargaste.
#
# METODOS: acceso con [] (si no existe la clave -> KeyError) vs .get(clave,
# default) (si no existe, devuelve el default SIN explotar). ¿Cuando cada
# uno? [] cuando la clave DEBE existir (que explote si no es señal de error);
# .get() cuando la ausencia es normal (frecuencias: .get(palabra, 0) + 1).
# .items() recorre pares; .keys() y .values() sus partes.
#
# TEORIA: LISTA DE DICCIONARIOS - EL ESTANDAR UNIVERSAL DE DATOS
# alumnos = [{"nombre": "Ana", "notas": [8, 9]}, {...}]
# ¿Por que esta estructura gana siempre? Cada registro se describe por NOMBRE
# (imposible desalinear como las listas paralelas), los registros pueden
# tener campos distintos, y es EXACTAMENTE el formato de un JSON (clase 26)
# y de una fila de base de datos. Aprender esto = entender como se mueven
# los datos en la industria.
#
# TEORIA: SETS - UNICIDAD Y ALGEBRA DE CONJUNTOS
# set = coleccion SIN orden y SIN repetidos. ¿Para que? Eliminar duplicados
# (set(lista)) y operaciones de conjuntos:
#   a & b interseccion (en ambos), a | b union (todos), a - b diferencia
#   (en a pero no en b), a ^ b XOR (solo en uno).
# ¿Por que sin orden? No les importa: su negocio es la pertenencia (in) y
# la unicidad, con la misma velocidad hash que los diccionarios.
#
# ============================================================

# 1) Frecuencia de palabras: el patron .get() + 1
texto = "el profe dijo que el examen es fácil y el TP también"
frecuencia = {}
for palabra in texto.lower().split():
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
print(frecuencia)
# ¿Que hace .get(palabra, 0)? Si la palabra ya esta, devuelve su conteo;
# si no, 0. Sumamos 1 y guardamos: contador de primeras veces en una linea.
# ¿Por que lower()? "El" y "el" deben contar juntos.

# 2) Lista de diccionarios con promedio calculado
alumnos = [
    {"nombre": "Ana", "notas": [8, 9]},
    {"nombre": "Luis", "notas": [6, 5]},
]
for alumno in alumnos:
    alumno["promedio"] = sum(alumno["notas"]) / len(alumno["notas"])
    print(f"{alumno['nombre']}: {alumno['promedio']:.1f}")
# ¿Por que comillas simples adentro del f-string? El f-string usa dobles
# por fuera: adentro deben ser simples (o escapar). ¿Por que agregar el
# campo promedio al dict? Es mutable: agregar claves nuevas es natural.

for clave, valor in alumnos[0].items():
    print(clave, "→", valor)

# 3) Sets: cruce de cursos
prog = {"Ana", "Luis", "Marta"}
redes = {"Marta", "Pedro", "Ana"}
print("Cursan ambas:", prog & redes)
print("Solo una:", prog ^ redes)
print("Todos:", prog | redes)
# ¿set({"Ana"}) desde una lista con repetidos? set(lista) los elimina.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿Puedo tener diccionario dentro de diccionario?
# R: Si: {"alumno": {"nombre": "Ana", "notas": [8,9]}}. Acceso encadenado:
#      datos["alumno"]["notas"][0].
#
# P: ¿"Ana" in prog si prog es set?
# R: Si: in funciona en listas, sets y claves de diccionarios. En set/dict
#    es instantaneo; en lista recorre uno por uno.
#
# P: ¿Por que set() no mantiene el orden?
# R: Por diseño hash: la posicion interna sale de la clave, no del orden de
#    carga. Si necesitas sin-repetidos PERO ordenado: sorted(set(lista)).
#
# P: ¿Dos claves iguales en un literal?
# R: La ultima pisa a la primera (silenciosamente): {"a":1,"a":2} es {"a":2}.
# ============================================================
