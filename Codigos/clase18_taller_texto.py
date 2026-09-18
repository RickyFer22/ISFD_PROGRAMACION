# ============================================================
# CLASE 18 (TALLER) - Procesamiento de texto
# ============================================================
#
# TEORIA: NORMALIZAR PRIMERO, COMPARAR DESPUES
# Regla de oro del procesamiento de texto: antes de comparar o guardar,
# LIMPIAR: strip() (espacios), lower()/title() (mayusculas), y si
# corresponde replace() (separadores raros). ¿Por que? Porque para tu
# programa " Ana ", "ana" y "ANA" son tres cadenas distintas, pero para el
# usuario son la misma persona. El 90% de los bugs de texto son comparaciones
# sin normalizar.
#
# TEORIA: split() + join() - EL DUO QUE RESUELVE EL 80%
# split convierte TEXTO -> LISTA (para procesar campo por campo);
# join convierte LISTA -> TEXTO (para mostrar/guardar). ¿Por que join es
# metodo del separador y no de la lista? Diseño de Python: el separador es
# el que sabe como pegar. "-".join(lista).
#
# TEORIA: any() Y GENERADORES - PREGUNTAS MASIVAS EN UNA LINEA
# any(c.isupper() for c in clave): ¿hay ALGUN caracter en mayuscula?
# any() se corta apenas encuentra uno (como cortocircuito). ¿Por que no un
# for clasico? Menos codigo y misma velocidad; el for es bienvenido si hay
# que contar varias cosas a la vez.
#
# ============================================================

# 1) Normalizar nombres
nombre = input("Nombre completo: ").strip().title()
print(f"Normalizado: {nombre}")
# title() capitaliza cada palabra. ¿Por que title y no capitalize?
# capitalize pone SOLO la primera letra de TODA la cadena en mayuscula.

# 2) Validador de contrasena
clave = input("Contraseña: ")
valida = len(clave) >= 8 and any(c.isupper() for c in clave) and any(c.isdigit() for c in clave)
print("Contraseña válida" if valida else "Contraseña débil")
# ¿Por que and encadenados? Las TRES reglas deben cumplirse. ¿Por que
# len primero? La mas barata de evaluar (y con cortocircuito, si falla las
# otras no se corren).
# ¿c.isupper() en un caracter? True si es letra mayuscula. ¿"1".isupper()?
# False: no es letra (por eso pedimos isupper E isdigit por separado).

# 3) Usuario institucional
nombre = input("Nombre: ").strip().lower()
apellido = input("Apellido: ").strip().lower()
usuario = nombre[0] + apellido
print(f"Usuario: {usuario}@isfd.edu.ar")
# ¿nombre[0]? Primera letra (indice 0). ¿Que pasa si el nombre viene vacio?
# ""[0] da IndexError: caso de prueba obligatorio para el alumno avanzado.

# 4) DNI verbal
dni = input("DNI (ej: 38.555.123-4): ")
partes = dni.split("-")
numero = partes[0].replace(".", "")
print(f"Número: {numero} | Verificador: {partes[1]}")
# ¿split("-") y luego replace? Primero separamos numero/verificador, luego
# limpiamos puntos del numero. Encadenar transformaciones es el estilo.

# ============================================================
# PREGUNTAS QUE PODRIAN HACERTE:
#
# P: ¿title() con "maria del carmen"?
# R: "Maria Del Carmen": capitaliza TODO, incluso "Del". Casos finos
#    requieren logica propia (es el problema de los generalizadores).
#
# P: ¿split() sin argumento vs split(" ")?
# R: split() divide por CUALQUIER espacio (y junta multiples); split(" ")
#    genera cadenas vacias por espacios dobles. Preferir split().
#
# P: ¿Por que "1" + "1" da "11" y no 2?
# R: + con cadenas es CONCATENACION. El tipo del operando decide el
#    significado del operador (sobrecarga).
# ============================================================
