# ============================================================
# CLASE 2 - Primer programa, print() y el REPL
# ============================================================
#
# TEORIA: ¿QUE PASA CUANDO EJECUTAS UN PROGRAMA PYTHON?
#
# 1) Escribis texto en un archivo .py. Para la computadora eso es solo texto:
#    no "sabe" nada todavia.
# 2) Python tiene DOS formas de traducir ese texto a acciones:
#      a) El REPL (consola interactiva) y
#      b) El interprete ejecutando un archivo.
#    En ambos casos el proceso es el mismo: Python LEE tu linea, la PARSEA
#    (verifica que la sintaxis sea valida), la TRADUCE a un codigo intermedio
#    llamado "bytecode", y una maquina virtual (la PVM) ejecuta ese bytecode.
#    Por eso Python no es 100% interpretado ni compilado: es una mezcla.
#    Diferencia clave: el bytecode vive en memoria (o en la carpeta
#    __pycache__) y NO es un .exe: cada vez que corres el programa, Python
#    vuelve a leer y traducir. Es mas lento que C, pero MUCHO mas comodo.
#
# ¿POR QUE EXISTE EL REPL?
# "REPL" = Read-Eval-Print Loop (ciclo leer - evaluar - imprimir - repetir).
#   Read:    lee UNA instruccion que escribiste.
#   Eval:    la ejecuta (la "evalua") inmediatamente.
#   Print:   imprime el RESULTADO automaticamente (sin needing print()).
#   Loop:    espera la siguiente.
# ¿Por que print() SIEMPRE adentro del REPL? Ojo: en el REPL, escribir solo
#   2 + 2 muestra 4 porque el REPL imprime el valor de la expresion. Pero
#   print("Hola") TAMBIEN muestra Hola: esa es la ACCION de print, no el valor.
# ¿Por que entonces usar print() en archivos .py? Porque al ejecutar un
#   archivo, Python NO imprime valores automaticamente: solo hace lo que el
#   codigo le ordena. print() es la orden explicita de "mostrar esto en pantalla".
#
# ¿POR QUE PYTHON DISTINGUE MAYUSCULAS?
# Porque el lenguaje fue disenado asi (como casi todos: C, Java, JS). Es
# "case sensitive": Print, PRINT y print son tres nombres distintos. Solo
# print (minuscula) existe. Ventaja: permite diferenciar ConvencionDeClases
# de convencion_de_funciones (lo veremos en PEP 8).
#
# ¿QUE ES UNA CADENA (string) Y POR QUE LAS COMILLAS?
# Un texto es una SECUENCIA de caracteres guardada en memoria. Las comillas
# le dicen al interprete "esto es texto, no codigo". Sin comillas, print(Hola)
# busca una VARIABLE llamada Hola -> NameError: name 'Hola' is not defined.
# ¿Simple o dobles? Python acepta "..." y '...' por igual: son lo mismo.
# Las f-strings (la f antes de las comillas) permiten incrustar variables:
#   f"Bienvenida, {nombre}" -> Python reemplaza {nombre} por su valor.
# ¿Por que existirian si ya existe print(nombre)? Porque permiten CONSTRUIR
# textos complejos sin concatenar a mano con +.
#
# ============================================================

# --- ACCION 1: mostrar texto en pantalla ---
print("Hola, mundo!")
# ¿Por que "Hola, mundo"? Tradicion desde 1972 (Brian Kernighan, lenguaje B):
# es el programa mas simple que prueba que TODO el circuito funciona:
# escritura -> interpretacion -> salida.

# --- ACCION 2: print puede recibir varios valores separados por comas ---
print("2 + 2 es", 2 + 2)
# ¿Que hace la coma? print evalua cada cosa: el texto queda igual y la
# EXPRESION 2 + 2 se CALCULA (da 4). print los muestra separados por espacio.
# ¿Por que calcula? Porque antes de imprimir, Python resuelve la expresion.

# --- ACCION 3: f-strings ---
nombre = "Ana"
print(f"Bienvenida, {nombre}")
# La f activa el "modo plantilla": lo que va entre {} se EVALUA.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE (y sus respuestas):
#
# P: ¿Python compila o interpreta?
# R: Compila a bytecode internamente y luego una maquina virtual lo ejecuta.
#    Es "interpretado" desde el punto de vista del usuario: no genera .exe.
#
# P: ¿Por que en el REPL no necesito print() pero en el archivo si?
# R: El REPL muestra el VALOR de cada expresion que evalua (modo interactivo).
#    Un archivo solo hace lo que le ordenas; sin print(), el resultado se
#    calcula y se descarta silenciosamente.
#
# P: ¿Por que da error print(Hola)?
# R: Sin comillas Python cree que Hola es un nombre (variable o funcion).
#    No existe -> NameError. Con comillas es un valor de texto literal.
#
# P: ¿Puedo usar comillas simples?
# R: Si, '...' y "..." son identicas. Sirven para anidar: "dijo 'hola'".
#
# P: ¿Por que el lenguaje se llama Python, como la vibora?
# R: No: Monty Python (el grupo de comedia britanico). Guido van Rossum era fan.
#
# EXPERIMENTOS: probá en el REPL
#   >>> 2 + 2
#   >>> "Pro" + "gramacion"      (¿que hace el + con textos?)
#   >>> print("linea1\nlinea2")  (\n = salto de linea)
#   >>> exit()                   (para salir del REPL)
# ============================================================
