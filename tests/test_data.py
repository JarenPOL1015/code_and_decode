# Datos de prueba compartidos

PRUEBAS = [
    {
        "nombre": "Codificacion Basica",
        "tipo": "codificar",
        "datos": [1, 2, 3, 4, 5],
        "clave": 15,
        "esperado": [14, 13, 12, 11, 10]
    },
    {
        "nombre": "Codificacion con Cero",
        "tipo": "codificar",
        "datos": [0],
        "clave": 15,
        "esperado": [15]
    },
    {
        "nombre": "Codificacion Clave Personalizada",
        "tipo": "codificar",
        "datos": [1, 2, 3],
        "clave": 7,
        "esperado": [6, 5, 4]
    },
    {
        "nombre": "Decodificacion Basica",
        "tipo": "decodificar",
        "datos": [1, 2, 3, 4, 5],
        "clave": 15
    },
    {
        "nombre": "Decodificacion Numeros Grandes",
        "tipo": "decodificar",
        "datos": [255, 256, 1000, 5000],
        "clave": 15
    },
    {
        "nombre": "Reversibilidad Multiple",
        "tipo": "reversibilidad",
        "datos": [7, 14, 21, 28],
        "clave": 15
    },
    {
        "nombre": "Propiedad Inversa Completa",
        "tipo": "inversa",
        "datos": [1, 2, 3, 4, 5, 10, 100],
        "clave": 15
    }
]


def ejecutar_xor_paso_a_paso(datos, clave):
    """Aplica XOR a cada elemento."""
    return [(num, num ^ clave) for num in datos]


def verificar_codificacion(datos, clave, esperado):
    """Verifica codificacion correcta."""
    resultado = [num ^ clave for num in datos]
    return resultado, resultado == esperado


def verificar_reversibilidad(datos, clave, codificar_fn, decodificar_fn):
    """Verifica ciclo completo de codificacion/decodificacion."""
    paso1 = codificar_fn(datos, clave)
    paso2 = codificar_fn(paso1, clave)
    paso3 = decodificar_fn(paso2, clave)
    paso4 = decodificar_fn(paso3, clave)
    return [paso1, paso2, paso3, paso4], datos == paso4
