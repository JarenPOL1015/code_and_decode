# Codificación y Decodificación de Números

## Descripción

Aplicación para codificar y decodificar cadenas numéricas usando la operación XOR bitwise. Incluye interfaz gráfica, menú en consola y pruebas unitarias.

## Requisitos

Instala las siguientes dependencias:

```bash
pip install pillow
```

Python 3.7 o superior (incluye tkinter por defecto en Windows).

## Cómo Ejecutar

### Interfaz Gráfica (Recomendado)

```bash
python gui_menu.py
```

Abre una ventana gráfica con interfaz minimalista que permite:
- Cargar datos desde consola o archivo
- Codificar datos con XOR
- Decodificar datos
- Ver y ejecutar pruebas unitarias
- Guardar automáticamente los datos decodificados en archivo

### Menú en Consola

```bash
python menu.py
```

Ejecuta el programa en la terminal con menú interactivo basado en texto.

## Codificación y Decodificación

### Codificación (XOR)

Transforma números aplicando la operación XOR bitwise con clave 15 (por defecto).

```python
from algorithms.codificacion import codificar

datos = [1, 2, 3, 4, 5]
codificados = codificar(datos)
# Resultado: [14, 13, 12, 11, 10]
```

Cada número se codifica de manera independiente: `número XOR 15`

### Decodificación (XOR Inverso)

Recupera los datos originales aplicando XOR nuevamente con la misma clave.

```python
from algorithms.decodificacion import decodificar

codificados = [14, 13, 12, 11, 10]
originales = decodificar(codificados)
# Resultado: [1, 2, 3, 4, 5]
```

La operación XOR es autoinversa: `(a XOR k) XOR k = a`

### Guardado Automático

Los archivos se guardan automáticamente en la carpeta `files/` con la siguiente estructura:

```
files/
├── original/       - Archivos de datos originales cargados
├── encoded/        - Archivos de datos codificados
└── decoded/        - Archivos de datos decodificados
```

Cada archivo tiene el formato: `{tipo}_YYYYMMDD_HHMMSS.txt`

Ejemplos:
- `original_20250101_143022.txt` - Datos originales
- `encoded_20250101_143023.txt` - Datos codificados
- `decoded_20250101_143024.txt` - Datos decodificados

El contenido es una línea con números separados por comas.

## Pruebas Unitarias

### Ejecutar Pruebas desde GUI

Abre `gui_menu.py` y haz clic en el botón "Pruebas" para ver todos los resultados.

### Ejecutar Pruebas desde Terminal

```bash
python -m unittest test.py -v
```

### Pruebas Incluidas

- **Codificación básica**: Verifica que la codificación funciona correctamente
- **Codificación lista vacía**: Maneja listas sin datos
- **Codificación un elemento**: Prueba con un solo número
- **Codificación cero**: Prueba valor especial 0
- **Codificación clave personalizada**: Usa clave diferente a 15
- **Decodificación básica**: Verifica que decodificar(codificar(x)) = x
- **Decodificación lista vacía**: Maneja listas sin datos
- **Decodificación un elemento**: Prueba con un solo número
- **Decodificación clave personalizada**: Usa clave diferente a 15
- **Propiedad inversa**: Verifica reversibilidad con múltiples valores
- **Números grandes**: Verifica funcionamiento con valores > 1000
- **Reversibilidad múltiple**: Codifica/decodifica múltiples veces

Cada prueba muestra:
- Datos de entrada
- Datos intermedios (si aplica)
- Datos finales
- Resultado esperado

## Uso

### Interfaz Gráfica

1. Ejecuta `python gui_menu.py`
2. Haz clic en "Cargar Datos"
3. Elige método (consola o archivo)
4. Ingresa o carga números (máximo 10)
5. Haz clic en "Codificar" o "Decodificar"
6. Los datos se muestran en pantalla
7. Al decodificar, se genera automáticamente el archivo de salida

### Menú en Consola

1. Ejecuta `python menu.py`
2. Selecciona opción 1 para cargar datos
3. Elige método de entrada
4. Ingresa números
5. Elige codificar (opción 2) o decodificar (opción 3)
6. Los resultados se muestran en consola
7. Al decodificar, se genera automáticamente el archivo de salida

## Notas

- La clave de codificación por defecto es 15
- Máximo 10 números por entrada (configurable en config.py)
- Los archivos de salida se generan en el directorio actual
- La operación XOR es reversible y no pierde información
