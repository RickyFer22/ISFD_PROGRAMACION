# ============================================================
# CLASE 10 (TALLER) - Problemas con ciclos
# ============================================================
#
# TEORIA: EL MENU INFINITO - EL PATRON MAS IMPORTANTE DEL CUATRIMESTRE
# while True + if opcion == "salir": break. ¿Por que while True? Porque la
# condicion de salida no se conoce hasta leer la opcion: es mas claro "corre
# para siempre hasta que digan salir" que calcular una condicion compleja.
# ¿Por que es importante? Porque ESTE patron es el esqueleto del proyecto
# integrador y de casi todo programa interactivo del mundo (cajeros, ATMs,
# consolas de videojuegos).
#
# TEORIA: BANDERAS (FLAGS)
# acceso = False ... luego acceso = True. ¿Por que una variable que guarda
# un bool? Porque a veces el resultado de un proceso largo se necesita
# DESPUES del ciclo (para el mensaje final). La bandera "recuerda" lo que
# paso adentro. Alternativa moderna: usar break + else del while (poco
# conocido: el else del while corre si NO hubo break). Nosotros usamos
# banderas: mas explicitas.
#
# ============================================================

# 1) Cajero: menu con while
saldo = 100000.0
opcion = ""
while opcion != "4":
    print("\n1) Consultar saldo  2) Depositar  3) Extraer  4) Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        print(f"Saldo: ${saldo:.2f}")
    elif opcion == "2":
        saldo += float(input("Monto a depositar: "))
    elif opcion == "3":
        monto = float(input("Monto a extraer: "))
        if monto > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= monto
print("Gracias por usar el cajero")
# ¿Por que condicion while opcion != "4" y no while True/break? Dos formas
# validas: esta es mas "clara" para quien empieza. ¿Por que validar
# monto > saldo? Regla de negocio: no se puede extraer mas de lo que hay.
# La validacion de NEGATIVOS y letras queda para la unidad de excepciones.

# 2) Tabla de multiplicar validada
n = int(input("Tabla del (1-10): "))
while n < 1 or n > 10:
    n = int(input("Tabla del (1-10): "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
# ¿Por que while para validar y for para la tabla? Validar = "mientras sea
# invalido" (while); repetir 10 veces sabidas = for. Cada ciclo para lo suyo.

# 3) Login con 3 intentos (bandera)
clave = "python2026"
intentos = 0
acceso = False
while intentos < 3 and not acceso:
    if input("Contraseña: ") == clave:
        acceso = True
    else:
        intentos += 1
        print(f"Incorrecto. Intentos restantes: {3 - intentos}")
print("Acceso concedido" if acceso else "Cuenta bloqueada")
# ¿Por que intentos < 3 AND not acceso? Dos razones para seguir: quedan
# intentos Y todavia no entro. ¿Por que 3 - intentos y no mostrar intentos?
# A la persona le importa cuanto LE QUEDA (medir en lo que le sirve).

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿El while del login se fija en la condicion despues de acceso = True?
# R: Si: al terminar la vuelta vuelve a preguntar; como acceso es True,
#    not acceso es False -> sale. La condicion siempre se re-evalua.
#
# P: ¿Por que print("\n...") con el \n al inicio?
# R: Deja una linea en blanco antes del menu: separa visualmente las vueltas.
#    \n es el caracter de salto de linea.
#
# P: ¿Puedo anidar un while dentro de un while?
# R: Si (un cajero que atiende varios clientes = while exterior). Cuidado
#    con las variables de cada nivel.
# ============================================================
