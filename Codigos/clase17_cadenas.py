# ============================================================
# CLASE 17 - Cadenas de caracteres
# ============================================================
#
# TEORIA: ¿COMO SE GUARDA UN TEXTO EN MEMORIA?
# Una cadena es una SECUENCIA numerada de caracteres, empezando por 0.
#  "P y t h o n"
#   0 1 2 3 4 5
# ¿Por que desde 0 y no desde 1? Convencion historica de la informatica:
# el indice es un "desplazamiento" desde el inicio (el primero esta a 0
# pasos del comienzo). Indices NEGATIVOS cuentan desde el final: s[-1] es
# el ultimo. ¿Por que existen? Porque "la ultima letra" es una pregunta
# natural y sin negativos habria que escribir s[len(s)-1].
#
# SLICING (rebanadas): s[a:b] = desde a INCLUIDO hasta b EXCLUIDO.
# s[0:3] de "Python" = "Pyt". Omisiones: s[:3] (desde el inicio),
# s[3:] (hasta el final), s[::-1] (invertida: paso -1).
# ¿Por que el fin excluyente? Para que s[a:b] + s[b:] == s (se corta y une
# sin perder ni repetir). ¿Y s[2:2]? Cadena vacia "".
#
# TEORIA: INMUTABILIDAD - ¿POR QUE NO PUEDO HACER s[0] = "X"?
# Porque las cadenas en Python son INMUTABLES: una vez creadas, no cambian.
# s.upper() NO cambia s: crea y devuelve una cadena NUEVA (por eso hay que
# asignarla: s = s.upper()). ¿Por que Python las hizo inmutables?
#   - Seguridad: un texto que usas como clave de diccionario no cambia de
#     repente (los dict la usan para hash).
#   - Eficiencia: Python puede compartir cadenas iguales sin miedo.
# Consecuencia practica: TODO metodo de string devuelve una nueva cadena.
#
# METODOS CLAVE (todos devuelven NUEVO texto):
#   upper/lower: mayusculas/minusculas. title: Primera Letra De Cada Palabra.
#   strip: quita espacios de los bordes. ¿Por que necesario? El teclado
#   agrega espacios invisibles: " Ana " != "Ana". Normalizar SIEMPRE antes
#   de comparar.
#   split: divide por espacios (o el separador que le pases) -> lista.
#   join: une una lista con el pegamento indicado: "-".join(["a","b"]) = a-b.
#   replace: cambia apariciones. find: posicion de la primera aparicion
#   (-1 si no esta). in: pertenece? ("py" in "python" -> True).
#
# F-STRINGS CON FORMATO: {x:.2f} (2 decimales), {s:<12} (izq., ancho 12),
# {n:>8} (derecha). ¿Por que ancho fijo? Columnas alineadas en listados.
#
# ============================================================

frase = "  Programación en Python  "
limpia = frase.strip().lower()          # normalizar: espacios + minusculas
palabras = limpia.split()
print(frase[0:7], len(palabras), "python" in limpia)
# ¿Por que encadenar strip().lower()? strip devuelve cadena nueva: sobre esa
# se aplica lower. El orden casi no importa aca, pero strip-antes-evita
# problemas con separadores raros.

s = "hola mundo"
print(s.upper(), s.replace("mundo", "Python"), s.find("mundo"))
# find devuelve 5: h-o-l-a- -m -> el segundo o... ojo: indices 0,1,2,3,4,5.

producto, precio = "Teclado", 12500.5
print(f"|{producto:<12}|${precio:>10.2f}|")
# ¿Por que los pipes |? Solo visual: separan columnas y delatan desalineos.

nombre = "ana"
print(nombre.upper())
print(nombre)           # sigue "ana": la original JAMAS cambio.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿s[10] en "Python"?
# R: IndexError: string index out of range. Longitud 6: indices validos
#    0..5 (o -6..-1).
#
# P: ¿split(",") con "a,,b"?
# R: Devuelve ['a', '', 'b']: el espacio vacio tambien es un campo. Ojo al
#    procesar CSVs imperfectos.
#
# P: ¿Cadena con comillas adentro?
# R: "dijo \"hola\"" (escapando) o 'dijo "hola"' (otro tipo de comillas).
#
# P: ¿len() de un int?
# R: TypeError: los numeros no tienen longitud. str(123) primero si queres
#    contar cifras (aunque mejor: // y %).
# ============================================================
