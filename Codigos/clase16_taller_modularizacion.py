# ============================================================
# CLASE 16 (TALLER) - Modularizacion, biblioteca estandar, Git y GitHub
# ============================================================
#
# TEORIA: IMPORT - ¿COMO FUNCIONA?
# import math carga un MODULO: un archivo .py de la biblioteca estandar
# (que viene con Python, escrita por sus desarrolladores). Los nombres del
# modulo viven en su propio ambito: math.sqrt, por eso el prefijo. ¿Por que
# prefijar? Para que tus nombres no choquen con los del modulo.
# from datetime import date: trae SOLO date al ambito actual (sin prefijo).
# ¿Cuando cada uno? import modulo: general y claro; from X import Y: para
# usar mucho una sola cosa. ¿Que tiene math? dir(math) lo lista: Herramienta
# de exploracion.
#
# TEORIA: REFACTORIZAR - MEJORAR SIN CAMBIAR EL COMPORTAMIENTO
# Refactorizar = reorganizar el codigo (extraer funciones) SIN que el
# programa deje de hacer lo mismo. ¿Por que no se hace "de una vez"? Porque
# cada paso chico se puede probar: refactorizo -> pruebo -> refactorizo.
# Si cambio y no pruebo, cuando falle no sabras si fue la logica o la
# reorganizacion. ¿Como se llama la red de seguridad? Tests (los veras en
# 2do ano; hoy: probar a mano despues de cada paso).
#
# TEORIA: GIT Y GITHUB - ¿POR QUE EXISTEN?
# Problema real: "trabajo_final_v2_FINAL_definitivo_con_correcciones.py".
# Git guarda la HISTORIA completa del proyecto: cada commit es una foto del
# estado de los archivos, con fecha, autor y mensaje. ¿Por que es revolucionario?
#   - Volves a cualquier punto del pasado (¿rompi algo? vuelvo a ayer).
#   - ¿Quien cambio que y cuando? git log / la web de GitHub.
#   - Varias personas trabajan sin pisarse (ramas, mas adelante).
# Git = la herramienta (local, offline). GitHub = la web donde los
# repositorios se COMPARTEN (backup + colaboracion + historial publico).
# Los 3 comandos del dia:
#   git init      -> convierte la carpeta en repositorio (empieza a grabar).
#   git add file  -> marca cambios para incluir en la proxima foto (staging).
#   git commit -m "mensaje" -> toma la foto. ¿Por que el -m? El mensaje es
#   la documentacion del cambio: "Alta de producto con validacion", nunca "asd".
# ¿Por que add y commit separados? Permite elegir QUE entra en cada foto:
# puedes cambiar 5 archivos y comprometer solo 2 juntos.
#
# ============================================================

import math
import random
from datetime import date

# math: funciones matematicas ya escritas por otros
print(math.sqrt(144), math.ceil(3.2), math.floor(3.8))
# sqrt = raiz cuadrada, ceil = techo (redondea arriba), floor = piso (abajo).
# ¿Por que usarlas y no escribir mi propia raiz? Reutilizacion: probada por
# millones de usuarios. No reescribas lo que la biblioteca resuelve.

# random: el juego de adivinanza con numero aleatorio real
secreto = random.randint(1, 100)
intentos = 0
while True:
    intento = int(input("Adiviná (1-100): "))
    intentos += 1
    if intento < secreto:
        print("Es mayor")
    elif intento > secreto:
        print("Es menor")
    else:
        print(f"¡Acertaste en {intentos} intentos!")
        break
# ¿randint incluye los extremos? SI (1 y 100 validos): diferencia con range.
# ¿while True + break? El ciclo termina por un suceso (acertar), no por una
# cuenta: es la forma natural de expresarlo.

# datetime: edad a partir del anio de nacimiento
anio = int(input("Año de nacimiento: "))
print(f"Tienes aprox. {date.today().year - anio} años")
# ¿date.today()? Se pregunta al sistema operativo la fecha actual: el
# programa funciona en 2027 sin tocar una linea. Datos del sistema > hardcodear.

# Refactorizacion del cajero en funciones
SALDO_INICIAL = 100000.0     # constante: MAYUSCULAS por convencion (PEP 8)

def depositar(saldo, monto):
    return saldo + monto

def extraer(saldo, monto):
    if monto > saldo:
        print("Saldo insuficiente")
        return saldo         # devuelve el saldo INTACTO
    return saldo - monto

saldo = SALDO_INICIAL
saldo = depositar(saldo, 5000)
saldo = extraer(saldo, 200000)
print(f"Saldo final: ${saldo:.2f}")
# ¿Por que "saldo = depositar(saldo, ...)" y no depositar modifica solo?
# Porque las funciones NO pueden cambiar una variable global sin global;
# el patron "recibir y devolver" es mas limpio: el flujo del dato es visible.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿Git necesita internet?
# R: NO: commit es local. Internet solo para push/pull con GitHub.
#
# P: ¿Puedo hacer commit sin add?
# R: El commit quedaria vacio ("nothing to commit"): add marca que incluir.
#    Atajo: git commit -am "mensaje" (add + commit de los ya rastreados).
#
# P: ¿random es realmente aleatorio?
# R: Usa un generador pseudoaleatorio (determinista con semilla). Para
#    juegos sobra; para criptografia existe el modulo secrets.
#
# P: ¿Por que GIT y no "guardar copias en carpetas"?
# R: Las copias no dicen QUE cambio ni permiten volver a un punto exacto con
#    un mensaje. Git guarda diferencias (deltas) compactas y etiquetadas.
# ============================================================
