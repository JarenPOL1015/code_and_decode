from config import MAX_NUMBERS

def parse_comma_separated_input(datos_str):
    # Separar por comas y quitar espacios
    items = [x.strip() for x in datos_str.split(',') if x.strip() != '']
    if len(items) > MAX_NUMBERS:
        raise ValueError(f"Se permiten como máximo {MAX_NUMBERS} números (usted ingresó {len(items)}).")
    try:
        numeros = [int(x) for x in items]
    except ValueError:
        raise ValueError("La cadena contiene elementos que no son números enteros.")
    return numeros
