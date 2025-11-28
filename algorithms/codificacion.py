def codificar(datos, clave=15):
    """Codifica una lista de numeros usando XOR con la clave especificada."""
    return [numero ^ clave for numero in datos]