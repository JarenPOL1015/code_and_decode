from algorithms.decodificacion import decodificar
from algorithms.codificacion import codificar
from functions.comma_parser import parse_comma_separated_input
from functions.file_parser import read_numbers_from_file
from config import MAX_NUMBERS

# Menú interactivo
def menu():
    datos = []
    while True:
        print("\nMenú:")
        print("1. Cargar Datos")
        print("2. Codificar")
        print("3. Decodificar")
        print("4. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print('Por favor ingrese un número válido (1-4).')
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
                    except ValueError as e:
                        print(f'Error: {e}')
                        continue
                    datos = numeros
                    print(f'Datos cargados: {datos}')
                    break

                if metodo == '2':
                    file_path = input('Ingrese el nombre del archivo .txt: ').strip()
                    try:
                        numeros = read_numbers_from_file(file_path)
                    except FileNotFoundError as e:
                        print(f'Error: {e}')
                        continue
                    except ValueError as e:
                        print(f'Error: {e}')
                        continue
                    datos = numeros
                    print(f'Datos cargados desde archivo: {datos}')
                    break
        
        elif opcion == 2:  # Codificar
            if not datos:
                print("No hay datos cargados.")
            else:
                print(f"Datos antes de codificar: {datos}")
                datos_codificados = codificar(datos)
                datos = datos_codificados  # Actualizar datos con los codificados
                print(f"Datos codificados: {datos_codificados}")                              
        
        elif opcion == 3:  # Decodificar
            if not datos:
                print("No hay datos cargados.")
            else:
                # Aquí usamos los datos codificados para decodificarlos correctamente
                # datos_codificados = codificar(datos)  # Codificar primero para simular el caso
                print(f"Datos codificados: {datos}")
                datos_decodificados = decodificar(datos)  # Decodificar
                datos = datos_decodificados  # Actualizar datos con los decodificados                
                print(f"Datos decodificados: {datos_decodificados}")        
        elif opcion == 4:  # Salir
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
