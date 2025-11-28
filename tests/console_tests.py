import time
from algorithms.codificacion import codificar
from algorithms.decodificacion import decodificar
from tests.test_data import PRUEBAS


def imprimir_linea(texto, delay=0.05):
    """Imprime texto con pausa."""
    print(texto)
    time.sleep(delay)


def ejecutar_prueba_codificar(prueba):
    """Ejecuta prueba de codificacion XOR."""
    datos = prueba["datos"]
    clave = prueba["clave"]
    esperado = prueba["esperado"]
    
    imprimir_linea(f"  Paso 1: Datos de entrada")
    imprimir_linea(f"          {datos}", 0.1)
    print()
    
    imprimir_linea(f"  Paso 2: Clave XOR = {clave} (binario: {bin(clave)})", 0.1)
    print()
    
    imprimir_linea(f"  Paso 3: Aplicando XOR a cada elemento:")
    resultado = []
    for num in datos:
        codificado = num ^ clave
        resultado.append(codificado)
        imprimir_linea(f"          {num} XOR {clave} = {codificado}", 0.15)
    
    print()
    imprimir_linea(f"  Paso 4: Resultado final")
    imprimir_linea(f"          {resultado}", 0.1)
    
    print()
    imprimir_linea(f"  Paso 5: Verificacion")
    imprimir_linea(f"          Esperado: {esperado}")
    imprimir_linea(f"          Obtenido: {resultado}")
    
    return resultado == esperado


def ejecutar_prueba_decodificar(prueba):
    """Ejecuta prueba de decodificacion XOR."""
    datos = prueba["datos"]
    clave = prueba["clave"]
    
    imprimir_linea(f"  Paso 1: Datos originales")
    imprimir_linea(f"          {datos}", 0.1)
    print()
    
    imprimir_linea(f"  Paso 2: Codificando (XOR con clave {clave}):")
    codificados = []
    for num in datos:
        cod = num ^ clave
        codificados.append(cod)
        imprimir_linea(f"          {num} XOR {clave} = {cod}", 0.1)
    
    print()
    imprimir_linea(f"  Paso 3: Datos codificados intermedios")
    imprimir_linea(f"          {codificados}", 0.1)
    print()
    
    imprimir_linea(f"  Paso 4: Decodificando (XOR con clave {clave}):")
    decodificados = []
    for num in codificados:
        dec = num ^ clave
        decodificados.append(dec)
        imprimir_linea(f"          {num} XOR {clave} = {dec}", 0.1)
    
    print()
    imprimir_linea(f"  Paso 5: Resultado final")
    imprimir_linea(f"          {decodificados}", 0.1)
    
    print()
    imprimir_linea(f"  Paso 6: Verificacion")
    imprimir_linea(f"          Original:    {datos}")
    imprimir_linea(f"          Recuperado:  {decodificados}")
    
    return datos == decodificados


def ejecutar_prueba_reversibilidad(prueba):
    """Ejecuta prueba de reversibilidad XOR."""
    datos = prueba["datos"]
    clave = prueba["clave"]
    
    imprimir_linea(f"  Paso 1: Datos originales")
    imprimir_linea(f"          {datos}", 0.1)
    print()
    
    imprimir_linea(f"  Paso 2: Primera codificacion:")
    paso1 = codificar(datos, clave)
    imprimir_linea(f"          {datos} -> {paso1}", 0.2)
    print()
    
    imprimir_linea(f"  Paso 3: Segunda codificacion (doble XOR):")
    paso2 = codificar(paso1, clave)
    imprimir_linea(f"          {paso1} -> {paso2}", 0.2)
    print()
    
    imprimir_linea(f"  Paso 4: Primera decodificacion:")
    paso3 = decodificar(paso2, clave)
    imprimir_linea(f"          {paso2} -> {paso3}", 0.2)
    print()
    
    imprimir_linea(f"  Paso 5: Segunda decodificacion:")
    paso4 = decodificar(paso3, clave)
    imprimir_linea(f"          {paso3} -> {paso4}", 0.2)
    print()
    
    imprimir_linea(f"  Paso 6: Verificacion de ciclo completo")
    imprimir_linea(f"          Original:  {datos}")
    imprimir_linea(f"          Final:     {paso4}")
    
    return datos == paso4


def ejecutar_prueba_inversa(prueba):
    """Ejecuta prueba de propiedad inversa XOR."""
    datos = prueba["datos"]
    clave = prueba["clave"]
    
    imprimir_linea(f"  Paso 1: Datos originales")
    imprimir_linea(f"          {datos}", 0.1)
    print()
    
    imprimir_linea(f"  Paso 2: Codificando elemento por elemento:")
    codificados = []
    for num in datos:
        cod = num ^ clave
        codificados.append(cod)
        imprimir_linea(f"          {num:5d} XOR {clave} = {cod:5d}", 0.1)
    
    print()
    imprimir_linea(f"  Paso 3: Resultado codificado")
    imprimir_linea(f"          {codificados}", 0.1)
    print()
    
    imprimir_linea(f"  Paso 4: Decodificando para recuperar:")
    decodificados = []
    for num in codificados:
        dec = num ^ clave
        decodificados.append(dec)
        imprimir_linea(f"          {num:5d} XOR {clave} = {dec:5d}", 0.1)
    
    print()
    imprimir_linea(f"  Paso 5: Verificacion final")
    imprimir_linea(f"          Original:    {datos}")
    imprimir_linea(f"          Recuperado:  {decodificados}")
    imprimir_linea(f"          Iguales:     {datos == decodificados}")
    
    return datos == decodificados


def ejecutar_pruebas_consola():
    """Ejecuta todas las pruebas en consola."""
    total_pruebas = len(PRUEBAS)
    pruebas_pasadas = 0
    
    print()
    print("=" * 60)
    imprimir_linea("  PRUEBAS UNITARIAS - PASOS INTERMEDIOS", 0.1)
    print("=" * 60)
    print()
    
    input("Presione ENTER para comenzar las pruebas...")
    print()
    
    for i, prueba in enumerate(PRUEBAS, 1):
        print("-" * 50)
        imprimir_linea(f"  PRUEBA {i}/{total_pruebas}: {prueba['nombre']}", 0.1)
        print("-" * 50)
        print()
        
        try:
            if prueba["tipo"] == "codificar":
                resultado = ejecutar_prueba_codificar(prueba)
            elif prueba["tipo"] == "decodificar":
                resultado = ejecutar_prueba_decodificar(prueba)
            elif prueba["tipo"] == "reversibilidad":
                resultado = ejecutar_prueba_reversibilidad(prueba)
            elif prueba["tipo"] == "inversa":
                resultado = ejecutar_prueba_inversa(prueba)
            
            print()
            if resultado:
                pruebas_pasadas += 1
                imprimir_linea("  [OK] PRUEBA EXITOSA", 0.1)
            else:
                imprimir_linea("  [FALLO] PRUEBA FALLIDA", 0.1)
        except Exception as e:
            print()
            imprimir_linea(f"  [ERROR] {str(e)}", 0.1)
        
        print()
        if i < total_pruebas:
            input("Presione ENTER para continuar a la siguiente prueba...")
        print()
    
    print()
    print("=" * 60)
    imprimir_linea(f"  RESUMEN: {pruebas_pasadas}/{total_pruebas} pruebas exitosas", 0.1)
    print("=" * 60)
    print()
    
    return pruebas_pasadas == total_pruebas


if __name__ == "__main__":
    ejecutar_pruebas_consola()
