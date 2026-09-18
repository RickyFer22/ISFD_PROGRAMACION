# ============================================================
# CLASE 8 (TALLER) - Problemas de decision
# ============================================================
#
# TEORIA: PROBAR UN PROGRAMA CON CONDICIONALES = CUBRIR LAS RAMAS
# Cada if tiene caminos. Si tu if/elif/else tiene 3 ramas, necesitas 3
# pruebas (una por camino) para saber que funciona. ¿Por que? Porque aprobar
# "mi nota 9 da Promociona" NO prueba que "nota 5 da Aprueba": cada rama es
# un codigo distinto que puede estar mal. Esto se llama cobertura de ramas
# (branch coverage) y es la base del testing.
#
# TEORIA: LEER CONSIGNAS COMO UN PROFESIONAL
# "Tarifa nocturna +20%" -> ¿sobre el total o sobre los km? El enunciado
# manda: si no lo aclara, PREGUNTAR (en la vida real) o decidir y DOCUMENTAR
# con un comentario. ¿Por que documentar supuestos? Porque quien lea tu
# codigo (o vos en 6 meses) debe poder reconstruir tu razonamiento.
#
# ============================================================

# 1) Tarifa de taxi
bandera = 500.0        # constante del problema: se escribe MAYUSCULA
por_km = 90.0
km = float(input("Kilómetros recorridos: "))
noche = input("¿Viaje nocturno? (s/n): ").lower() == "s"
tarifa = bandera + km * por_km
if km < 2:
    tarifa = bandera
if noche:
    tarifa = tarifa * 1.20
print(f"Total del viaje: ${tarifa:.2f}")
# ¿Por que dos if y no if/else? Son dos decisiones INDEPENDIENTES: puede
# cumplirse ninguna, una, o ambas. if/elif seria incorrecto (solo una rama).
# ¿Por que .lower() == "s"? Para aceptar "S", "s", "S ". Normalizar entrada.
# ¿Por que * 1.20 y no + 20%? 20% de recargo = multiplicar por 1.20.

# 2) Beca
promedio = float(input("Promedio: "))
ingresos = float(input("Ingresos familiares: "))
if promedio >= 7 and ingresos < 500000:
    print("Apto para la beca")
else:
    print("No apto para la beca")
# ¿Por que and y no dos if seguidos? Porque las DOS condiciones deben cumplir
# juntas para UNA misma decision. Dos if serian dos decisiones distintas.

# 3) Anio bisiesto (regla completa del calendario gregoriano)
anio = int(input("Año: "))
bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
print(bisiesto)
# ¿Por que tan enredado? Es la REGLA REAL: divisible por 4, salvo los
# multicplos de 100, salvo los multiplos de 400. 1900 no fue bisiesto
# (mult. de 100), 2000 si (mult. de 400). Los problemas del mundo real
# tienen reglas raras: el trabajo es traducirlas SIN simplificarlas.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿En que orden evalua Python (a and b)?
# R: Izquierda a derecha con cortocircuito: si a es False, b ni se evalua.
#
# P: ¿Por que anio % 4 == 0 y no anio % 4?
# R: anio % 4 da un NUMERO (0, 1, 2, 3); la condicion necesita un BOOL.
#    (Python acepta numeros como bool - 0 es False - pero se considera
#    mala practica: escribir la comparacion explicita.)
#
# P: ¿Puedo escribir if km < 2: tarifa = bandera en una linea?
# R: Si (ternaria): tarifa = bandera if km < 2 else tarifa. Existe, pero en
#    1er ano recomendamos la forma clasica: mas clara.
# ============================================================
