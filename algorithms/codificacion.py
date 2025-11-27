# Función para codificar utilizando XOR con una clave por defecto
def codificar(datos, clave=15):
    datos_codificados = []
    for numero in datos:
        datos_codificados.append(numero ^ clave)  # Operación XOR
    return datos_codificados