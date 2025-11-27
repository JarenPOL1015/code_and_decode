from decodificacion import decodificar
from codificacion import codificar

# Menú interactivo
def menu():
    datos = []
    while True:
        print("\nMenú:")
        print("1. Cargar Datos")
        print("2. Codificar")
        print("3. Decodificar")
        print("4. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:  # Cargar datos
            datos_str = input("Ingrese una cadena de números separados por comas: ")
            datos = [int(x) for x in datos_str.split(',')]
            print(f"Datos cargados: {datos}")
        
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
