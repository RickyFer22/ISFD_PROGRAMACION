# 💻 Tecnicatura Superior en Desarrollo de Software (TSDS)
## Cátedra de Programación — 1.er Año (2.do Cuatrimestre 2026)
### Instituto Superior de Formación Docente "Juan García de Cossio" — San Roque, Corrientes

---

[![Python Version](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![IDE](https://img.shields.io/badge/IDE-Visual%20Studio%20Code-007ACC?logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![Version Control](https://img.shields.io/badge/Git%20%26%20GitHub-Colaborativo-181717?logo=github&logoColor=white)](https://github.com/)
[![Modalidad](https://img.shields.io/badge/Formato-Te%C3%B3rico--Pr%C3%A1ctico%20%2B%20Taller-success)]()
[![Enfoque](https://img.shields.io/badge/Arquitectura-Offline--First-orange)]()

---

## 📋 Información General del Espacio Curricular

- **Institución:** Instituto Superior de Formación Docente "Juan García de Cossio"
- **Carrera:** Tecnicatura Superior en Desarrollo de Software (TSDS)
- **Asignatura:** Programación
- **Ubicación en el Plan de Estudios:** 1.er Año · 2.do Cuatrimestre
- **Carga Horaria:** 5 horas didácticas semanales
  - **Miércoles (3 hs):** Teórico - Práctico (conceptos fundamentales, diseño algorítmico y demostraciones en vivo).
  - **Viernes (2 hs):** Taller de Laboratorio (programación intensiva en máquina, resolución de problemas y acompañamiento guiado).
- **Profesor Titular:** Fernández, Ricardo
- **Lenguaje Principal y Entorno:** Python 3 (CPython 3.x) + Visual Studio Code + Git & GitHub

---

## 🎯 Fundamentación Pedagógica

La materia **Programación** adopta a **Python** como lenguaje principal y único de la cursada desde el primer día, prescindiendo deliberadamente de intermediaciones con herramientas simplificadas o pseudocódigos no estandarizados.

Python combina una sintaxis limpia y cercana al lenguaje natural —lo que permite concentrarse plenamente en el desarrollo del **pensamiento computacional**— con un ecosistema robusto, una biblioteca estándar amplísima y un liderazgo indiscutido en la industria del software, la ciencia de datos y la inteligencia artificial.

El dictado articula teoría rigurosa y práctica intensiva: más del 50% del tiempo total se destina a la resolución efectiva de desafíos en laboratorio. Desde la primera semana se inculcan estándares profesionales de ingeniería:
1. **Convenciones de estilo:** Aplicación estricta de la guía oficial **PEP 8**.
2. **Claridad léxica:** Nombres de identificadores autoexplicativos y semánticos.
3. **Manejo de excepciones:** Construcción de software tolerante a fallos y validación exhaustiva de entradas.
4. **Control de versiones:** Trazabilidad de código mediante commits atómicos en Git y colaboración en GitHub.

---

## 🚀 Expectativas de Logro (Objetivos de Aprendizaje)

Al finalizar el cursado, los estudiantes serán capaces de:

1. **Pensamiento Computacional:** Analizar, descomponer y modelar formalmente problemas de la realidad mediante algoritmos precisos.
2. **Entorno Profesional:** Configurar, escribir, ejecutar y depurar aplicaciones en Python utilizando Visual Studio Code y su terminal integrada.
3. **Control de Flujo:** Implementar estructuras de secuencia, selección condicional e iteración controlada para resolver lógicas complejas.
4. **Modularización:** Diseñar programas estructurados en funciones puras y cohesivas con paso de parámetros y retornos tipados.
5. **Estructuras de Datos:** Seleccionar y manipular eficientemente colecciones nativas (listas, tuplas, diccionarios y conjuntos).
6. **Persistencia y Robustez:** Leer y persistir información en archivos de texto plano, CSV y JSON, gestionando errores en tiempo de ejecución mediante `try/except`.
7. **Control de Versiones:** Versionar colaborativamente proyectos de software aplicando el ciclo de vida de Git (`add`, `commit`, `push`, `branch`, `merge`).
8. **Integración de Software:** Desarrollar, documentar y defender oralmente una aplicación completa de consola que resuelva un caso de negocio real.

---

## 🗂️ Estructura de Unidades Didácticas

### 🔹 Unidad 1: Introducción a la Programación y Pensamiento Computacional
- Algoritmos formales e informales. El rol del pensamiento computacional en el desarrollo de software.
- Ecosistema Python y VS Code: instalación, intérprete interactivo (REPL) y estructura de scripts `.py`.
- Variables y tipado dinámico (`int`, `float`, `str`, `bool`). Entrada/salida (`input()`, `print()`) y casting de tipos.
- Operadores aritméticos, de comparación y lógicos. Precedencia y evaluación en cortocircuito.

### 🔹 Unidad 2: Estructuras de Control: Decisión y Repetición
- Estructuras condicionales: `if`, `elif`, `else`. Condiciones anidadas y compuestas.
- Iteración indeterminada: ciclo `while`, diseño de centinelas, contadores, acumuladores y banderas (*flags*).
- Iteración determinada: ciclo `for`, función generadora `range()` y ciclos anidados.
- Interrupción y control de bucles: `break` y `continue`.
- Depuración profesional: inspección de variables, puntos de interrupción (*breakpoints*) y *call stack* en VS Code.

### 🔹 Unidad 3: Funciones y Modularización
- Definición de funciones con `def`, argumentos posicionales, por palabra clave y valores por omisión.
- Valores de retorno (`return`), ámbito de variables (regla LEGB: Local, Enclosing, Global, Built-in).
- Documentación interna mediante *docstrings*.
- Modularización con la biblioteca estándar de Python: `math`, `random`, `datetime`.
- Introducción al control de versiones con Git: configuración de usuario, `git init`, `git add`, `git commit`.

### 🔹 Unidad 4: Estructuras de Datos Básicas (Colecciones)
- Cadenas de texto (`str`): indexación, *slicing*, inmutabilidad, métodos de transformación y *f-strings*.
- Listas (`list`) y tuplas (`tuple`): mutabilidad, métodos de inserción/borrado, ordenamiento y listas por comprensión (*list comprehensions*).
- Diccionarios (`dict`): tablas hash, claves únicas, accesos seguros con `.get()` y colecciones de registros.
- Conjuntos (`set`): unicidad y operaciones algebraicas (unión, intersección, diferencia).

### 🔹 Unidad 5: Archivos, Errores y Tratamiento de Datos
- Manejo estructurado de excepciones: bloques `try`, `except`, `else` y `finally`. Filosofía *EAFP* vs *LBYL*.
- Persistencia en disco: apertura y cierre seguro de archivos con contexto (`with open(...) as ...`).
- Procesamiento de formatos estructurados de intercambio: módulos nativos `csv` y `json`.
- Implementación del patrón de persistencia para operaciones **ABM / CRUD** (Alta, Baja, Modificación y Consulta).
- Trazabilidad y entrega remota de proyectos a través de repositorios en GitHub.

### 🔹 Unidad 6: Proyecto Integrador Final
- Arquitectura en capas para aplicaciones de consola: separación entre interfaz de usuario, lógica de negocio y capa de datos.
- Trabajo colaborativo en equipo mediante control de versiones en GitHub.
- Redacción de documentación técnica profesional (`README.md`, manual de instalación y requerimientos).
- Defensa oral individual y en vivo (*Live Code Defense*) de la solución informática desarrollada.

---

## 🗺️ Mapa Curricular: Presentaciones y Códigos Fuente

A continuación se detalla la correlación exacta entre las diapositivas de clase disponibles en [`Presentaciones/`](Presentaciones/) y los scripts didácticos ejecutables alojados en [`Codigos/`](Codigos/):

| Clase | Tema de la Clase | Unidad | Presentación (Diapositivas) | Código Didáctico Ejecutable | Conceptos Clave |
| :---: | :--- | :---: | :--- | :--- | :--- |
| **01** | Introducción a la Informática y Python | U1 | [`Clase 01`](Presentaciones/Clase%2001%20-%20¿Qué%20es%20programar%20-%20Entorno%20y%20primer%20programa%20en%20Python.pptx) | [`clase02_primer_programa.py`](Codigos/clase02_primer_programa.py) | ¿Qué es programar?, intérprete, VS Code, primer script. |
| **02** | Variables, Tipos de Datos e I/O | U1 | [`Clase 02`](Presentaciones/Clase%2002%20-%20Variables,%20tipos%20de%20datos%20y%20entrada-salida.pptx) | [`clase03_variables_y_tipos.py`](Codigos/clase03_variables_y_tipos.py) | Memoria, tipado dinámico, `input()`, `print()`, conversión de tipos. |
| **03** | Operadores, Expresiones y Algoritmia | U1 | [`Clase 03`](Presentaciones/Clase%2003%20-%20Operadores,%20expresiones%20y%20método%20de%20resolución.pptx) | [`clase04_taller_entrada_salida.py`](Codigos/clase04_taller_entrada_salida.py) <br> [`clase05_operadores.py`](Codigos/clase05_operadores.py) | Operadores aritméticos, lógicos y relacionales, método de 4 pasos. |
| **04** | Estructuras Condicionales | U2 | [`Clase 04`](Presentaciones/Clase%2004%20-%20Estructuras%20condicionales%20-%20if,%20elif%20y%20else.pptx) | [`clase06_taller_consolidacion.py`](Codigos/clase06_taller_consolidacion.py) <br> [`clase07_condicionales.py`](Codigos/clase07_condicionales.py) | Bloques `if-elif-else`, indentación, álgebra booleana. |
| **05** | Ciclo Indeterminado: `while` | U2 | [`Clase 05`](Presentaciones/Clase%2005%20-%20Ciclo%20while%20-%20repetir%20mientras%20se%20cumpla%20una%20condición.pptx) | [`clase08_taller_decision.py`](Codigos/clase08_taller_decision.py) <br> [`clase09_ciclo_while.py`](Codigos/clase09_ciclo_while.py) | Bucles mientras, condiciones de parada, bucle infinito, centinela. |
| **06** | Ciclo Determinado: `for` y Rangos | U2 | [`Clase 06`](Presentaciones/Clase%2006%20-%20Ciclo%20for,%20range()%20y%20ciclos%20anidados.pptx) | [`clase10_taller_ciclos.py`](Codigos/clase10_taller_ciclos.py) <br> [`clase11_ciclo_for.py`](Codigos/clase11_ciclo_for.py) | `for-in`, `range()`, contadores, acumuladores, ciclos anidados. |
| **07** | Repaso y Evaluación Parcial 1 | U1-U2 | [`Clase 07`](Presentaciones/Clase%2007%20-%20Repaso%20integrador%20y%20Examen%20Parcial%201.pptx) | *Ejercicios de Consolidación* | Evaluación escrita e individual en máquina (Unidades 1 y 2). |
| **08** | Modularización: Funciones | U3 | [`Clase 08`](Presentaciones/Clase%2008%20-%20Funciones%20-%20parámetros,%20retorno%20y%20ámbito.pptx) | [`clase14_intro_funciones.py`](Codigos/clase14_intro_funciones.py) <br> [`clase15_funciones_parametros.py`](Codigos/clase15_funciones_parametros.py) | Parámetros, argumentos, valor de retorno, ámbito LEGB. |
| **09** | Módulos y Control de Versiones | U3 | [`Clase 09`](Presentaciones/Clase%2009%20-%20Módulos,%20biblioteca%20estándar%20y%20control%20de%20versiones%20con%20Git.pptx) | [`clase16_taller_modularizacion.py`](Codigos/clase16_taller_modularizacion.py) | `import`, módulos estándar (`math`, `random`), `git init/commit`. |
| **10** | Cadenas y Procesamiento de Texto | U4 | [`Clase 10`](Presentaciones/Clase%2010%20-%20Cadenas%20de%20caracteres%20y%20procesamiento%20de%20texto.pptx) | [`clase17_cadenas.py`](Codigos/clase17_cadenas.py) <br> [`clase18_taller_texto.py`](Codigos/clase18_taller_texto.py) | Indexación, *slicing*, inmutabilidad, `split()`, `join()`, sanitización. |
| **11** | Listas y Tuplas | U4 | [`Clase 11`](Presentaciones/Clase%2011%20-%20Listas%20y%20tuplas.pptx) | [`clase19_listas_tuplas.py`](Codigos/clase19_listas_tuplas.py) <br> [`clase20_taller_colecciones.py`](Codigos/clase20_taller_colecciones.py) | Mutabilidad, métodos de lista, comprensión de listas, inmutabilidad de tuplas. |
| **12** | Diccionarios y Conjuntos | U4 | [`Clase 12`](Presentaciones/Clase%2012%20-%20Diccionarios%20y%20conjuntos.pptx) | [`clase21_diccionarios_sets.py`](Codigos/clase21_diccionarios_sets.py) | Clave-valor, tablas hash, operaciones de conjuntos, registros estructurados. |
| **13** | Repaso y Evaluación Parcial 2 | U3-U4 | [`Clase 13`](Presentaciones/Clase%2013%20-%20Repaso%20de%20estructuras%20de%20datos%20y%20Examen%20Parcial%202.pptx) | *Ejercicios de Consolidación* | Evaluación escrita e individual en máquina (Unidades 3 y 4). |
| **14** | Excepciones y GitHub Remoto | U5 | [`Clase 14`](Presentaciones/Clase%2014%20-%20Excepciones%20y%20GitHub%20-%20trabajar%20con%20un%20repositorio%20remoto.pptx) | [`clase24_excepciones.py`](Codigos/clase24_excepciones.py) | `try-except-finally`, robustez, repositorios remotos en GitHub. |
| **15** | Persistencia: Archivos de Texto | U5 | [`Clase 15`](Presentaciones/Clase%2015%20-%20Archivos%20de%20texto%20-%20guardar%20datos%20que%20sobreviven%20al%20programa.pptx) | [`clase25_archivos_texto.py`](Codigos/clase25_archivos_texto.py) | Modos `r`, `w`, `a`, context managers (`with`), codificación UTF-8. |
| **16** | Persistencia Estructurada: CSV y JSON | U5 | [`Clase 16`](Presentaciones/Clase%2016%20-%20Formatos%20CSV%20y%20JSON.pptx) | [`clase26_taller_csv_json.py`](Codigos/clase26_taller_csv_json.py) | `csv.reader`/`DictWriter`, serialización con `json.dump`/`load`. |
| **17** | Proyecto Integrador: Arquitectura | U6 | [`Clase 17`](Presentaciones/Clase%2017%20-%20Proyecto%20integrador%20-%20especificación%20y%20arquitectura.pptx) | [`clase27_plantilla_proyecto.py`](Codigos/clase27_plantilla_proyecto.py) | Arquitectura en capas, especificación del CRUD, validaciones. |
| **18** | Desarrollo en Equipo con Git | U6 | [`Clase 18`](Presentaciones/Clase%2018%20-%20Desarrollo%20del%20proyecto%20en%20equipo%20con%20Git%20y%20GitHub.pptx) | *Repositorio de Equipo* | Ramas (`branch`), *pull requests*, resolución de conflictos. |
| **19** | Entrega y Coloquio de Defensa | U6 | [`Clase 19`](Presentaciones/Clase%2019%20-%20Entrega%20del%20TP%20integrador%20y%20coloquio%20de%20defensa.pptx) | *Proyectos de los Alumnos* | Presentación grupal, trazado de código y defensa oral individual. |
| **20** | Recuperatorios y Cierre de Cursada | Cierre | [`Clase 20`](Presentaciones/Clase%2020%20-%20Recuperatorios%20y%20cierre%20de%20la%20cursada.pptx) | *Cierre Administrativo* | Cierre de actas, devoluciones pedagógicas y regularidad final. |

---

## 💡 Metodología de los Códigos Fuente Didácticos

Cada archivo contenido en [`Codigos/`](Codigos/) no es un mero ejemplo aislado, sino un **mini-apunte teórico ejecutable** diseñado bajo una estricta estructura de tres niveles:

1. **Bloque Teórico Inicial:** Explica el funcionamiento interno del intérprete (gestión de memoria, punteros de objetos, ámbito léxico) y las razones de ingeniería por las cuales Python fue diseñado de esa manera.
2. **Código Fuente Exhaustivamente Comentado:** Cada línea detalla su justificación técnica, advierte errores conceptuales frecuentes y analiza qué ocurriría si se escribiera de un modo alternativo.
3. **Preguntas Frecuentes y Casos Borde ("Preguntas que podrían hacerte"):** Banco de dudas y trampas habituales de examen con sus respectivas respuestas y demostraciones.

---

## 🤖 Política sobre el Uso de Inteligencia Artificial (Live Code Defense)

La cátedra entiende que las herramientas generativas (asistentes de IA basados en LLMs) forman parte indispensable del flujo de trabajo moderno en la industria del software. En consecuencia, la materia promueve su uso guiado y crítico bajo un principio inquebrantable:

> ### 📌 Regla de Oro
> **"La Inteligencia Artificial puede ayudarte a ENTENDER, nunca a ENTREGAR algo que no entendés."**  
> *El estudiante es siempre el autor legal y académico responsable del código que presenta.*

### ✅ Usos Fomentados por la Cátedra
- **Traductor de Errores y Tracebacks:** Copiar un error de consola y solicitar a la IA la explicación pedagógica de su origen y cómo prevenirlo.
- **Tutor Conceptual Continuo:** Solicitar analogías alternativas o ejemplos complementarios sobre conceptos teóricos complejos.
- **Generador de Casos de Prueba Borde:** Descubrir entradas anómalas (valores vacíos, tipos incompatibles, límites numéricos) para poner a prueba la tolerancia a fallos de un script.
- **Revisor de Estilo:** Validar el apego a la convención PEP 8 y sugerir nombres de variables más claros en código ya resuelto por el estudiante.

### ❌ Usos Inadmisibles
- Solicitar la resolución integral de un ejercicio y presentarla sin comprensión propia.
- Copiar y pegar bloques de código que el estudiante no pueda explicar línea por línea.
- Utilizar asistentes durante los exámenes parciales o el coloquio final.

### 🛡️ Mecanismo de Acreditación: *Live Code Defense*
La acreditación de saberes no se apoya en la entrega estática de archivos, sino en la **defensa en vivo**:
- En los parciales y en el coloquio final, el docente solicita al estudiante trazar la ejecución de su código y realizar **modificaciones funcionales en tiempo real**.
- Quien no sea capaz de justificar su código o aplicar un cambio menor solicitado en el momento, **desaprueba la instancia**, independientemente de que el programa original funcione.
- El uso honesto y documentado de IA no penaliza: los aportes de herramientas externas deben consignarse explícitamente en los comentarios del código o en el `README` del proyecto.

---

## 🛠️ Instalación y Puesta en Marcha del Entorno

### 1. Requisitos Previos
- **Sistema Operativo:** Windows 10/11, GNU/Linux o macOS.
- **Python 3.12 o superior:** Descargar desde [python.org](https://www.python.org/downloads/) *(importante: marcar la casilla "Add python.exe to PATH" durante la instalación en Windows)*.
- **Visual Studio Code:** Descargar desde [code.visualstudio.com](https://code.visualstudio.com/).
  - Extensión recomendada: **Python** (oficial de Microsoft).
- **Git:** Descargar desde [git-scm.com](https://git-scm.com/).

### 2. Clonar el Repositorio
Abre tu terminal (PowerShell, Git Bash o Command Prompt) y ejecuta:
```bash
git clone https://github.com/RickyFer22/ISFD_PROGRAMACION.git
cd ISFD_PROGRAMACION
```

### 3. Ejecutar los Ejemplos Didácticos
Cada archivo puede abrirse directamente en VS Code y ejecutarse con el botón superior derecho `▶ Run Python File`, o ejecutarse vía consola:
```bash
python Codigos/clase02_primer_programa.py
```

---

## 📊 Régimen de Evaluación y Acreditación

Para regularizar y/o promocionar la asignatura se requiere:

1. **Asistencia:** Cumplir con el porcentaje reglamentario institucional (80% para promoción / 70% para regularidad).
2. **Exámenes Parciales:** Aprobación de dos instancias individuales teórico-prácticas en laboratorio con su correspondiente recuperatorio:
   - **Primer Parcial:** Unidades 1 y 2 (Algoritmos, E/S, Selección e Iteración).
   - **Segundo Parcial:** Unidades 3 y 4 (Funciones, Modularización y Colecciones de Datos).
3. **Trabajo Práctico Integrador:** Aprobación de un desarrollo de software en parejas/tríadas que integre menú interactivo, arquitectura modular, persistencia en archivos (CSV/JSON), tratamiento de excepciones y control de versiones en GitHub.
4. **Coloquio Final:** Defensa individual en vivo de la solución presentada.

---

## 📚 Bibliografía y Recursos de Consulta

### Bibliografía Abierta en Español (Disponible en el Repositorio)
- **González Duque, R.** *Python para todos.* — 📄 [Descarga directa en este repositorio (PDF)](Bibliografia/2010_python-para-todos.pdf) | [Enlace alternativo (Internet Archive)](https://archive.org/download/2010PythonParaTodos/2010_python-para-todos.pdf)
- *Python Intermedio (traducción al español).* — 📄 [Descarga directa en este repositorio (PDF)](Bibliografia/python-intermedio-readthedocs-io-es-latest.pdf) | [Documentación en línea](https://python-intermedio.readthedocs.io/es/latest/)
- **Severance, C.** *Python para todos: explorando la información con Python 3.* — [Libro web interactivo (py4e)](https://es.py4e.com/book)
- **Delgado Quintero, S.** *Aprende Python.* — [Plataforma interactiva en línea](https://aprendepython.es)

### Bibliografía Complementaria
- **Sweigart, A. (2019).** *Automate the Boring Stuff with Python* (2.ª ed.). No Starch Press. [Lectura libre en línea](https://automatetheboringstuff.com)
- **Gaddis, T. (2021).** *Starting Out with Python* (5.ª ed.). Pearson.
- **Deitel, P. & Deitel, H. (2019).** *Python for Programmers: with Big Data and AI Case Studies*. Pearson.
- **Joyanes Aguilar, L. (2008).** *Fundamentos de Programación: Algoritmos, Estructuras de Datos y Objetos* (4.ª ed.). McGraw-Hill.

### Enlaces Oficiales y Documentación de Referencia
- [Documentación Oficial de Python en Español](https://docs.python.org/es/3/)
- [Guía de Estilo Oficial PEP 8](https://peps.python.org/pep-0008/)
- [Documentación de Python en Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Guías y Recursos de Git / GitHub en Español](https://docs.github.com/es)

---

## 🏛️ Créditos Institucionales

**Instituto Superior de Formación Docente "Juan García de Cossio"**  
San Roque, Provincia de Corrientes, República Argentina  
Tecnicatura Superior en Desarrollo de Software (TSDS) — Ciclo Lectivo 2026  
**Profesor:** Ricardo Fernández
