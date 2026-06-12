# Proyecto Final Matemática Discreta

## Ruta Óptima entre Ciudades mediante Grafos Ponderados

### Integrantes

* Pablo Urra
* Compañero 2
* Compañero 3
* Compañero 4


Por Dios consideren que tienen que hacer commits y PR legibles y descriptivos como ingenieros duros, como seguramente leyeron Código Limpio esto ni siquiera deberia decirlo!!!

# Descripción del Proyecto

Para este proyecto tendremos que hacer una red de ciudades usando un grafo ponderado. Vamos a desarrollarlo con Python para poder calcular la ruta entre la ciudad de origen y las ciudad de destino.

Las ciudades serán representadas como vértices y las conexiones entre ellas como aristas ponderadas utilizando distancias reales en kilómetros.

El sistema permitirá:

* Seleccionar una ciudad de origen.
* Seleccionar una ciudad de destino.
* Calcular la ruta óptima mediante un algoritmo de camino mínimo.
* Mostrar el costo total del recorrido.
* Visualizar gráficamente el grafo y la ruta encontrada.

---

# Tecnologías Utilizadas

* Python
* NetworkX
* Matplotlib
* CustomTkinter

---

# Estructura del Proyecto

```text
Proyecto-Mate/
│
├── data/
│   └── conexiones.csv
│
├── src/
│   ├── app.py
│   ├── graph_manager.py
│   ├── shortest_path.py
│   └── visualization.py
│
├── docs/
│
├── requirements.txt
│
└── README.md
```

---

# Distribución de Trabajo

## Pablo Urra

### Arquitectura, Modelamiento Matemático y Algoritmos

Responsabilidades:

* Diseñar la estructura general del proyecto.
* Definir el modelo matemático del grafo.
* Definir los conjuntos V y E.
* Definir la función de peso w.
* Verificar que el grafo sea conexo.
* Implementar el algoritmo de Dijkstra.
* Comparar Dijkstra con una alternativa.
* Integrar todos los módulos del proyecto.
* Gestionar el repositorio principal.

Archivos asociados:

* shortest_path.py
* graph_manager.py

---

## Compañero 2

### Construcción y Validación de Datos

Responsabilidades:

* Seleccionar las 15 ciudades.
* Buscar conexiones reales entre ciudades.
* Obtener distancias verificables.
* Documentar las fuentes utilizadas.
* Construir el archivo conexiones.csv.
* Verificar consistencia de los datos.

Archivos asociados:

* data/conexiones.csv
* documentación de fuentes

---

## Compañero 3

### Interfaz Gráfica

Responsabilidades:

* Implementar la interfaz utilizando CustomTkinter.
* Crear selección de ciudad de origen.
* Crear selección de ciudad de destino.
* Implementar botones y controles.
* Mostrar resultados de la búsqueda.

Archivos asociados:

* app.py

---

## Compañero 4

### Visualización, Informe y Presentación

Responsabilidades:

* Implementar visualización del grafo.
* Resaltar la ruta óptima encontrada.
* Mantener documentación del repositorio.
* Colaborar en la elaboración del informe técnico.
* Colaborar en la preparación de la presentación final.

Archivos asociados:

* visualization.py
* documentación del proyecto

---

# Instalación

Clonar el repositorio:

```bash
git clone https://github.com/PabloUrra2233/Proyecto-Mate.git
```

Entrar al directorio:

```bash
cd Proyecto-Mate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
python src/app.py
```

---

# Estado Actual

* [ ] Selección de ciudades
* [ ] Construcción del grafo
* [ ] Implementación de Dijkstra
* [ ] Interfaz gráfica
* [ ] Visualización del grafo
* [ ] Informe técnico
* [ ] Presentación final

---

# Licencia

Proyecto académico desarrollado para la asignatura de Matemática Discreta.
