# 📊 Proyecto EDA Básico en Python

Este proyecto es un ejemplo **simple y didáctico** para aprender:

- Cómo organizar un proyecto en Python
- Cómo crear tu propio paquete con funciones reutilizables
- Cómo usar esas funciones desde un archivo principal
- Cómo generar una gráfica a partir de datos reales

Usamos el dataset **penguins** de `seaborn` como excusa para practicar estructura y buenas prácticas.

---

## 🧠 Idea principal

En proyectos reales **no todo vive en un solo archivo**.

Aquí separamos:
- Funciones de análisis (EDA)
- Código que ejecuta el análisis

Esto hace el código:
- más limpio
- más reutilizable
- más fácil de mantener

---

## 📁 Estructura del proyecto

eda_project/
|
|-- eda_utils/
|   |-- __init__.py
|   |-- stats.py
|   |-- plots.py
|
|-- main.py
`-- requirements.txt


### ¿Qué es cada cosa?

- **`eda_utils/`**  
  Es un *paquete* de Python con funciones reutilizables.

- **`stats.py`**  
  Funciones de análisis básico (resúmenes, valores faltantes).

- **`plots.py`**  
  Funciones para generar gráficas.

- **`main.py`**  
  Archivo principal que:
  - carga los datos
  - llama a las funciones
  - genera resultados

---

## 🧩 Paquete `eda_utils`

### `stats.py`

Contiene funciones de análisis exploratorio básico.

Ejemplos:
- resumen estadístico
- conteo de valores nulos

Estas funciones:
- reciben un DataFrame
- devuelven resultados
- **no ejecutan nada por sí solas**

---

### `plots.py`

Contiene funciones para visualización.

Ejemplo:
- histograma de una variable numérica

Cada función:
- recibe datos
- genera una gráfica
- no depende del archivo principal

---

## 🚀 Archivo principal (`main.py`)

`main.py` es el punto de entrada del proyecto.

Aquí:
1. Se cargan los datos
2. Se llaman las funciones del paquete
3. Se muestran resultados y gráficas

Incluye esta estructura:

```python
if __name__ == "__main__":
    main()

Esto asegura que el código:

- solo se ejecute cuando el archivo se corre directamente
- no se ejecute si se importa desde otro archivo

## ▶️ Cómo ejecutar el proyecto

1. Crea si no tienes ya y activa un entorno conda, instala las dependencias y ejecuta el proyecto desde la carpeta raíz:

```bash
conda create -n eda_env python=3.12 -y
conda activate eda_env
python -m pip install -r requirements.txt
python main.py
```



