# Función para decodificar utilizando XOR con la misma clave
def decodificar(datos_codificados, clave=15):
    datos_decodificados = []
    for numero in datos_codificados:
        datos_decodificados.append(numero ^ clave)  # Operación XOR
    return datos_decodificados