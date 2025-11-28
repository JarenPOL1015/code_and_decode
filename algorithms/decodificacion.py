def decodificar(datos_codificados, clave=15):
    """Decodifica una lista de numeros usando XOR con la clave especificada."""
    return [numero ^ clave for numero in datos_codificados]