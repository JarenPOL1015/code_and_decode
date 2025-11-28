from algorithms.decodificacion import decodificar
from algorithms.codificacion import codificar
from functions.comma_parser import parse_comma_separated_input
from functions.file_parser import read_numbers_from_file, write_numbers_to_file, save_original_file, get_files_directory, cleanup_temporary_files
from tests.console_tests import ejecutar_pruebas_consola
from config import MAX_NUMBERS
import os


def _load_and_save_numbers(numeros):
    """Carga y guarda numeros."""
    try:
        archivo_original = save_original_file(numeros)
        print(f'Datos cargados: {numeros}')
        print(f'Archivo original guardado: {archivo_original}')
        return numeros
    except IOError as e:
        print(f'Error al guardar archivo original: {e}')
        return None


def _show_available_files():
    """Muestra archivos disponibles."""
    files_dir = get_files_directory()
    original_dir = os.path.join(files_dir, "original")
    available_files = []
    
    if os.path.exists(original_dir):
        available_files = os.listdir(original_dir)
    
    if available_files:
        print('\nArchivos disponibles en files/original/:')
        for i, file in enumerate(available_files, 1):
            print(f'  {i}. {file}')
        print(f'  {len(available_files) + 1}. Otro archivo (ingrese nombre manualmente)')
    
    return available_files


def _get_file_choice(available_files):
    """Obtiene seleccion de archivo del usuario."""
    try:
        choice = input('Seleccione archivo (número): ').strip()
        if choice.isdigit():
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(available_files):
                return available_files[choice_idx]
        return choice
    except ValueError:
        return input('Ingrese el nombre del archivo .txt: ').strip()

def menu():
    datos = []
    
    # Advertencia inicial
    print("\n" + "=" * 60)
    print("  ADVERTENCIA")
    print("=" * 60)
    print("  TODOS los archivos seran ELIMINADOS al cerrar:")
    print("    - Archivos subidos/cargados")
    print("    - Archivos codificados")
    print("    - Archivos decodificados")
    print("  Solo se conserva: nums.txt (archivo de prueba)")
    print("=" * 60)
    
    while True:
        print("\nMenu:")
        print("1. Cargar Datos")
        print("2. Codificar")
        print("3. Decodificar")
        print("4. Ejecutar Pruebas")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print('Por favor ingrese un numero valido (1-5).')
            continue
        
        if opcion == 1:  # Cargar datos
            # Ask the user whether they want to enter a comma-separated string or a text file
            while True:
                print('\nCargar datos:')
                print(f'1. Ingresar cadena de números separados por comas (máx {MAX_NUMBERS})')
                print(f'2. Cargar desde archivo .txt con números separados línea a línea o por comas')
                metodo = input('Seleccione método (1 o 2) o presione ENTER para cancelar: ').strip()
                if metodo == '':
                    print('Carga de datos cancelada.')
                    break
                if metodo not in ('1', '2'):
                    print('Opción no válida. Intente de nuevo.')
                    continue

                if metodo == '1':
                    datos_str = input(f'Ingrese una cadena de números separados por comas (máx {MAX_NUMBERS}): ').strip()
                    try:
                        numeros = parse_comma_separated_input(datos_str)
                        datos = _load_and_save_numbers(numeros)
                        if datos:
                            break
                    except ValueError as e:
                        print(f'Error: {e}')
                        continue

                if metodo == '2':
                    available_files = _show_available_files()
                    file_path = _get_file_choice(available_files) if available_files else input('Ingrese el nombre del archivo .txt: ').strip()
                    
                    try:
                        numeros = read_numbers_from_file(file_path)
                        datos = _load_and_save_numbers(numeros)
                        if datos:
                            break
                    except (FileNotFoundError, ValueError) as e:
                        print(f'Error: {e}')
                        continue
        
        elif opcion == 2:  # Codificar
            if not datos:
                print("No hay datos cargados.")
            else:
                print(f"Datos antes de codificar: {datos}")
                datos_codificados = codificar(datos)
                datos = datos_codificados  # Actualizar datos con los codificados
                print(f"Datos codificados: {datos_codificados}")
                
                try:
                    archivo = write_numbers_to_file(datos_codificados, "encoded")
                    print(f"Archivo guardado: {archivo}")
                except IOError as e:
                    print(f"Error al guardar: {e}")                              
        
        elif opcion == 3:  # Decodificar
            if not datos:
                print("No hay datos cargados.")
            else:
                print(f"Datos codificados: {datos}")
                datos_decodificados = decodificar(datos)  # Decodificar
                datos = datos_decodificados  # Actualizar datos con los decodificados                
                print(f"Datos decodificados: {datos_decodificados}")
                
                try:
                    archivo = write_numbers_to_file(datos_decodificados, "decoded")
                    print(f"Archivo guardado: {archivo}")
                except IOError as e:
                    print(f"Error al guardar: {e}")
        
        elif opcion == 4:  # Ejecutar Pruebas
            print("\nIniciando pruebas con pasos intermedios...")
            ejecutar_pruebas_consola()
        
        elif opcion == 5:  # Salir
            print("\nLimpiando archivos...")
            cleanup_temporary_files()
            print("\n" + "=" * 60)
            print("  AVISO: Todos los archivos han sido eliminados:")
            print("    - Archivos subidos/cargados")
            print("    - Archivos codificados")
            print("    - Archivos decodificados")
            print("  Solo se conserva: nums.txt")
            print("=" * 60)
            print("\nSaliendo del programa.")
            break
        
        else:
            print("Opcion no valida, intente de nuevo.")

if __name__ == "__main__":
    menu()
