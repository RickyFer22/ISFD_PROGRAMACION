# ============================================================
# CLASE 6 (TALLER) - Consolidacion Unidad 1
# ============================================================
#
# TEORIA: COMO ATACAR UN PROBLEMA SIN CODIGO AUN (metodo de 4 pasos)
# 1) ENTENDER: ¿que datos entran, que salen? Escribilo con un ejemplo:
#    "si bruto=100000 -> aportes=17000 -> neto=83000".
# 2) PLANTEAR: las formulas en castellano/espacio de papel.
# 3) CODIFICAR: recien ahora, escribir el .py.
# 4) PROBAR: con el ejemplo del paso 1. ¿Da 83000? ¿y con bruto=0?
# ¿Por que este metodo? Porque el 80% de los errores de principiante no son
# de sintaxis: son de PROBLEMA MAL ENTENDIDO. El paso 1 los elimina.
#
# TEORIA: TRAZADO (DRY-RUN) - COMO EJECUTAR EL PROGRAMA EN TU CABEZA
# Dibujas una tabla: una columna por variable, una fila por linea ejecutada.
# Anotas el valor de cada variable despues de cada linea. ¿Para que sirve?
#   - Para PREDECIR la salida antes de correr (asi se rinden examenes).
#   - Para ENCONTRAR bugs: en la fila donde tu valor esperado y el real
#     difieren, esta el error.
# ¿Por que funciona? Porque un programa es un proceso DETERMINISTICO: mismo
# estado inicial + mismas entradas => mismos valores siempre. El trazado es
# "ser la computadora" a mano.
#
# ============================================================

# --- 1) Liquidacion de sueldo ---
bruto = float(input("Sueldo bruto: "))
aportes = bruto * 0.17
neto = bruto - aportes
print(f"Bruto: ${bruto:.2f} | Aportes (17%): ${aportes:.2f} | Neto: ${neto:.2f}")
# ¿Por que 0.17 y no 17? Porque el % es una relacion: 17% = 17/100 = 0.17.
# ¿Por que calcular aportes aparte y no solo neto? Porque el enunciado pide
# MOSTRAR los tres valores: cada dato pedido necesita su variable.

# --- 2) Reparto de cuenta con propina ---
total = float(input("Total de la cuenta: "))
personas = int(input("Cantidad de personas: "))
propina = total * 0.10
cada_uno = (total + propina) / personas
print(f"Con propina: ${total + propina:.2f} -> cada uno paga ${cada_uno:.2f}")
# ¿Que pasa si personas = 0? ZeroDivisionError. Todavia no lo manejamos con
# try/except; anotalo como "caso a validar" (llega en la unidad de excepciones).

# --- 3) Trazado en papel: predice la salida ANTES de ejecutar ---
x = 5
y = 2
x = x + y      # ¿x? (7: la derecha se calcula primero con x=5, y=2)
y = x - y      # ¿y? (5: ¡x ya cambió a 7! 7-2=5)
print(x, y)    # 7 5
# ¿Por que x = x + y no es una ecuacion matematica? Porque = es ASIGNACION:
# "calcula lo de la derecha y guardalo en lo de la izquierda". El x de la
# derecha es el valor VIEJO; el de la izquierda es donde se guarda el nuevo.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿Por que me piden trazado si la PC ejecuta sola?
# R: En el examen no hay PC. Y en la vida real: cuando el programa falla,
#    el trazado es como se encuentra la linea culpable (depuracion manual).
#
# P: ¿x = x + y y x += y son lo mismo?
# R: Si, += es "incremento": x += y equivale a x = x + y. Existen -= *= /=.
#
# P: ¿Por que mi programa da decimales feos como 83000.000001?
# R: Floats binarios (ver clase 3). Solucion para MOSTRAR: :.2f.
# ============================================================
