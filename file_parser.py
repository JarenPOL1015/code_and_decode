import os

def read_numbers_from_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Archivo no encontrado: {file_path}")
    numeros = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Permite separar por comas o linea por linea
            if ',' in line:
                parts = [x.strip() for x in line.split(',') if x.strip() != '']
            else:
                parts = [line]
            for p in parts:
                try:
                    num = int(p)
                except ValueError:
                    raise ValueError(f"El archivo contiene un valor no entero: '{p}'")
                numeros.append(num)
    return numeros
