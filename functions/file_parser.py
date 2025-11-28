import os
from datetime import datetime

def get_files_directory():
    """Obtiene o crea el directorio files con subcarpetas."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files_dir = os.path.join(base_dir, "files")
    
    for subfolder in ["original", "encoded", "decoded"]:
        subfolder_path = os.path.join(files_dir, subfolder)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path, exist_ok=True)
    
    return files_dir

def _get_full_path(file_path):
    """Resuelve ruta completa del archivo."""
    if not os.path.isabs(file_path) and not os.path.dirname(file_path):
        files_dir = get_files_directory()
        original_dir = os.path.join(files_dir, "original")
        return os.path.join(original_dir, file_path)
    return file_path

def _get_available_files():
    """Obtiene lista de archivos en files/original/."""
    files_dir = get_files_directory()
    original_dir = os.path.join(files_dir, "original")
    if os.path.exists(original_dir):
        return os.listdir(original_dir)
    return []

def _parse_numbers(line):
    """Extrae numeros de una linea de texto."""
    line = line.strip()
    if not line:
        return []
    
    if ',' in line:
        parts = [x.strip() for x in line.split(',') if x.strip() != '']
    else:
        parts = [line]
    
    numeros = []
    for p in parts:
        try:
            numeros.append(int(p))
        except ValueError:
            raise ValueError(f"El archivo contiene un valor no entero: '{p}'")
    return numeros

def read_numbers_from_file(file_path):
    """Lee numeros desde un archivo."""
    full_path = _get_full_path(file_path)
    
    if not os.path.isfile(full_path):
        available_files = _get_available_files()
        error_msg = f"Archivo no encontrado: {full_path}"
        if available_files:
            error_msg += f"\nArchivos disponibles en files/original/:\n" + "\n".join(available_files)
        raise FileNotFoundError(error_msg)
    
    numeros = []
    with open(full_path, 'r', encoding='utf-8') as f:
        for line in f:
            numeros.extend(_parse_numbers(line))
    return numeros

def _write_to_file(file_path, numeros):
    """Escribe numeros en un archivo."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(','.join(str(num) for num in numeros))
        return file_path
    except IOError as e:
        raise IOError(f"Error al escribir en el archivo: {e}")

def save_original_file(numeros):
    """Guarda numeros en files/original/."""
    files_dir = get_files_directory()
    original_dir = os.path.join(files_dir, "original")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(original_dir, f"original_{timestamp}.txt")
    return _write_to_file(output_file, numeros)

def write_numbers_to_file(numeros, operacion="decoded"):
    """Guarda numeros en files/encoded/ o files/decoded/."""
    files_dir = get_files_directory()
    subfolder = "encoded" if operacion.lower() == "encoded" else "decoded"
    output_dir = os.path.join(files_dir, subfolder)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"{subfolder}_{timestamp}.txt")
    return _write_to_file(output_file, numeros)

def cleanup_temporary_files():
    """Elimina todos los archivos excepto nums.txt."""
    files_dir = get_files_directory()
    
    for subfolder in ["encoded", "decoded"]:
        folder_path = os.path.join(files_dir, subfolder)
        if os.path.exists(folder_path):
            try:
                for file in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
            except Exception as e:
                print(f"Error al limpiar {subfolder}: {e}")
    
    original_path = os.path.join(files_dir, "original")
    if os.path.exists(original_path):
        try:
            for file in os.listdir(original_path):
                if file.lower() != "nums.txt":
                    file_path = os.path.join(original_path, file)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
        except Exception as e:
            print(f"Error al limpiar original: {e}")
