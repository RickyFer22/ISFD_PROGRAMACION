# ============================================================
# CLASE 9 - Ciclo while: repeticion con condicion
# ============================================================
#
# TEORIA: ¿POR QUE EXISTEN LOS CICLOS?
# Copiar y pegar 30 veces "input + acumular" seria un desastre: si cambia el
# enunciado (30 -> 50), hay que editar 50 lineas. El ciclo repite un bloque
# MIENTRAS una condicion sea verdadera. Es el tercer pilar (con secuencia y
# seleccion) de la programacion: con esos tres se construye todo.
#
# TEORIA: ANATOMIA DEL WHILE - LOS 3 INGREDIENTES OBLIGATORIOS
#   1) INICIALIZAR:  la variable de control ANTES del ciclo (monto = ...).
#   2) CONDICION:    while <condicion>: se evalua ANTES de cada vuelta.
#   3) ACTUALIZAR:   algo DENTRO del ciclo debe, tarde o temprano, volver la
#      condicion falsa.
# ¿Por que se llama "while" (mientras)? Porque se lee literal:
#   "mientras monto != 0: hacé este bloque".
# ¿Como funciona por dentro? La condicion se re-evalua en CADA vuelta: si es
#   True ejecuta el bloque y VUELVE A PREGUNTAR; si es False salta a la
#   primera linea fuera del ciclo. Si la condicion nunca se vuelve falsa:
#   CICLO INFINITO (el programa se cuelga; Ctrl+C para cortarlo).
# ¿Por que es "pre-test"? Porque pregunta ANTES de ejecutar: si la condicion
#   arranca falsa, el bloque NO corre ni una vez. (Do-while, que corre al
#   menos una vez, no existe en Python: se simula con while True + break.)
#
# TEORIA: CONTADOR, ACUMULADOR Y CENTINELA
#   contador    -> cuenta VUELTAS: cantidad += 1.
#   acumulador  -> suma VALORES: total += monto.
#   centinela   -> valor especial que avisa "terminemos" (0 en ventas).
# ¿Por que centinela y no preguntar "cuantas ventas"? Porque a veces no se
# sabe de antemano cuantas hay (un dia de caja). ¿Que valor de centinela
# elegir? Uno IMPOSIBLE en los datos reales (una venta de $0 no existe).
#
# ============================================================

# 1) Suma de ventas hasta 0
total, cantidad = 0.0, 0
monto = float(input("Venta (0 termina): "))
while monto != 0:
    total += monto
    cantidad += 1
    monto = float(input("Venta (0 termina): "))
print(f"Total: {total} en {cantidad} ventas")
# ¿Por que el primer input va ANTES del while? Ingredientes 1 y 2: hay que
# inicializar monto para poder preguntar la primera vez. ¿Por que el input
# de nuevo al FINAL del bloque? Ingredientes 3: actualizar para la proxima
# pregunta. Ese patron "leer-procesar-leer" se llama lectura con priming.

# 2) Adivinar el numero con pistas
secreto = 42
intento = int(input("Adiviná el número: "))
while intento != secreto:
    if intento < secreto:
        print("Es mayor")
    else:
        print("Es menor")
    intento = int(input("Otro intento: "))
print("¡Acertaste!")
# ¿Por que if/else ADENTRO del while? En cada vuelta se da UNA pista, luego
# se vuelve a preguntar. La condicion del while (intento != secreto) se
# re-evalua sola con el nuevo valor.

# 3) Validacion: repetir hasta recibir algo correcto
nota = int(input("Nota entre 1 y 10: "))
while nota < 1 or nota > 10:
    print("Valor inválido")
    nota = int(input("Nota entre 1 y 10: "))
print(f"Nota aceptada: {nota}")
# ¿Por que or y no and? La nota es invalida si falla UNA u OTRA cosa.
# ¿Por que no acepta 10.5? int() ya trunco: mejor float() y comparar bien.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿Como corto un ciclo infinito?
# R: Ctrl+C en la terminal (KeyboardInterrupt). Prevenir: revisar el
#    ingrediente 3 (¿algo cambia la condicion?).
#
# P: ¿While con condicion True?
# R: while True: es ciclo infinito intencional; se sale con break. Se usa
#    en menus: "mientras no pidan salir". Lo vemos en el taller.
#
# P: ¿Puedo usar el valor del contador despues del ciclo?
# R: Si: la variable sobrevive al ciclo (su ultimo valor es el que hizo
#    fallar la condicion). Detalle util.
#
# P: ¿Diferencia entre while y for?
# R: while = cuando NO sabes cuantas vueltas (depende del usuario/datos).
#    for = cuando SABES (o recorres una coleccion). Regla practica.
# ============================================================
