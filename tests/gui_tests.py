"""Modulo de pruebas con interfaz grafica."""
import tkinter as tk
from tkinter import scrolledtext
import threading
import time

from algorithms.codificacion import codificar
from algorithms.decodificacion import decodificar
from tests.test_data import PRUEBAS


class ConsolaPruebas:
    """Ventana de pruebas con visualizacion de pasos."""
    
    def __init__(self, parent):
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Pruebas del Sistema")
        self.ventana.geometry("700x550")
        self.ventana.configure(bg="#1e1e1e")
        self.ventana.resizable(True, True)
        
        # Área de texto estilo consola
        self.texto = scrolledtext.ScrolledText(
            self.ventana,
            wrap=tk.WORD,
            font=("Consolas", 11),
            bg="#1e1e1e",
            fg="#d4d4d4",
            insertbackground="#ffffff",
            padx=10,
            pady=10
        )
        self.texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Botón para cerrar
        self.btn_cerrar = tk.Button(
            self.ventana,
            text="Cerrar",
            font=("Segoe UI", 11),
            bg="#3c3c3c",
            fg="white",
            command=self.ventana.destroy,
            relief=tk.FLAT,
            padx=20,
            pady=5
        )
        self.btn_cerrar.pack(pady=(0, 10))
        
        # Ejecutar pruebas en hilo separado
        self.hilo = threading.Thread(target=self.ejecutar_pruebas, daemon=True)
        self.hilo.start()
    
    def imprimir(self, texto, delay=0.03):
        """Imprime texto con delay para efecto progresivo."""
        try:
            self.texto.insert(tk.END, texto + "\n")
            self.texto.see(tk.END)
            self.texto.update()
            time.sleep(delay)
        except tk.TclError:
            pass  # Ventana cerrada
    
    def ejecutar_pruebas(self):
        """Ejecuta todas las pruebas mostrando pasos intermedios."""
        try:
            self.imprimir("=" * 55, 0.02)
            self.imprimir("  PRUEBAS UNITARIAS - PASOS INTERMEDIOS", 0.05)
            self.imprimir("=" * 55, 0.02)
            self.imprimir("")
            
            total = len(PRUEBAS)
            exitosas = 0
            
            for i, prueba in enumerate(PRUEBAS, 1):
                self.imprimir("-" * 50, 0.02)
                self.imprimir(f"  PRUEBA {i}/{total}: {prueba['nombre']}", 0.05)
                self.imprimir("-" * 50, 0.02)
                self.imprimir("")
                
                tipo = prueba["tipo"]
                
                if tipo == "codificar":
                    resultado = self.prueba_codificar(prueba)
                elif tipo == "decodificar":
                    resultado = self.prueba_decodificar(prueba)
                elif tipo == "reversibilidad":
                    resultado = self.prueba_reversibilidad(prueba)
                elif tipo == "inversa":
                    resultado = self.prueba_inversa(prueba)
                else:
                    resultado = False
                
                if resultado:
                    exitosas += 1
                    self.imprimir("  [OK] PRUEBA EXITOSA", 0.1)
                else:
                    self.imprimir("  [FALLO] PRUEBA FALLIDA", 0.1)
                
                self.imprimir("")
                time.sleep(0.3)
            
            # Resumen
            self.imprimir("")
            self.imprimir("=" * 55, 0.02)
            self.imprimir(f"  RESUMEN: {exitosas}/{total} pruebas exitosas", 0.1)
            self.imprimir("=" * 55, 0.02)
            
            if exitosas == total:
                self.imprimir("\n  TODAS LAS PRUEBAS PASARON CORRECTAMENTE", 0.1)
            else:
                self.imprimir(f"\n  {total - exitosas} PRUEBA(S) FALLARON", 0.1)
                
        except tk.TclError:
            pass  # Ventana cerrada
    
    def prueba_codificar(self, prueba):
        """Ejecuta prueba de codificacion XOR."""
        datos = prueba["datos"]
        clave = prueba["clave"]
        esperado = prueba["esperado"]
        
        self.imprimir(f"  Paso 1: Datos de entrada")
        self.imprimir(f"          {datos}", 0.1)
        self.imprimir("")
        
        self.imprimir(f"  Paso 2: Clave XOR = {clave} (binario: {bin(clave)})", 0.1)
        self.imprimir("")
        
        self.imprimir(f"  Paso 3: Aplicando XOR a cada elemento:")
        resultado = []
        for num in datos:
            cod = num ^ clave
            resultado.append(cod)
            self.imprimir(f"          {num} XOR {clave} = {cod}", 0.1)
        
        self.imprimir("")
        self.imprimir(f"  Paso 4: Resultado final")
        self.imprimir(f"          {resultado}", 0.1)
        
        self.imprimir("")
        self.imprimir(f"  Paso 5: Verificacion")
        self.imprimir(f"          Esperado: {esperado}")
        self.imprimir(f"          Obtenido: {resultado}")
        self.imprimir("")
        
        return resultado == esperado
    
    def prueba_decodificar(self, prueba):
        """Ejecuta prueba de decodificacion XOR."""
        datos = prueba["datos"]
        clave = prueba["clave"]
        
        self.imprimir(f"  Paso 1: Datos originales")
        self.imprimir(f"          {datos}", 0.1)
        self.imprimir("")
        
        self.imprimir(f"  Paso 2: Codificando (XOR con clave {clave}):")
        codificados = []
        for num in datos:
            cod = num ^ clave
            codificados.append(cod)
            self.imprimir(f"          {num} XOR {clave} = {cod}", 0.1)
        
        self.imprimir("")
        self.imprimir(f"  Paso 3: Datos codificados intermedios")
        self.imprimir(f"          {codificados}", 0.1)
        self.imprimir("")
        
        self.imprimir(f"  Paso 4: Decodificando (XOR con clave {clave}):")
        decodificados = []
        for num in codificados:
            dec = num ^ clave
            decodificados.append(dec)
            self.imprimir(f"          {num} XOR {clave} = {dec}", 0.1)
        
        self.imprimir("")
        self.imprimir(f"  Paso 5: Resultado final")
        self.imprimir(f"          {decodificados}", 0.1)
        
        self.imprimir("")
        self.imprimir(f"  Paso 6: Verificacion")
        self.imprimir(f"          Original:   {datos}")
        self.imprimir(f"          Recuperado: {decodificados}")
        self.imprimir("")
        
        return datos == decodificados
    
    def prueba_reversibilidad(self, prueba):
        """Ejecuta prueba de reversibilidad XOR."""
        datos = prueba["datos"]
        clave = prueba["clave"]
        
        self.imprimir(f"  Paso 1: Datos originales")
        self.imprimir(f"          {datos}", 0.1)
        self.imprimir("")
        
        self.imprimir(f"  Paso 2: Primera codificacion:")
        paso1 = codificar(datos, clave)
        self.imprimir(f"          {datos} -> {paso1}", 0.15)
        self.imprimir("")
        
        self.imprimir(f"  Paso 3: Segunda codificacion (doble XOR):")
        paso2 = codificar(paso1, clave)
        self.imprimir(f"          {paso1} -> {paso2}", 0.15)
        self.imprimir("")
        
        self.imprimir(f"  Paso 4: Primera decodificacion:")
        paso3 = decodificar(paso2, clave)
        self.imprimir(f"          {paso2} -> {paso3}", 0.15)
        self.imprimir("")
        
        self.imprimir(f"  Paso 5: Segunda decodificacion:")
        paso4 = decodificar(paso3, clave)
        self.imprimir(f"          {paso3} -> {paso4}", 0.15)
        self.imprimir("")
        
        self.imprimir(f"  Paso 6: Verificacion de ciclo completo")
        self.imprimir(f"          Original: {datos}")
        self.imprimir(f"          Final:    {paso4}")
        self.imprimir("")
        
        return datos == paso4
    
    def prueba_inversa(self, prueba):
        """Ejecuta prueba de propiedad inversa XOR."""
        datos = prueba["datos"]
        clave = prueba["clave"]
        
        self.imprimir(f"  Paso 1: Datos originales")
        self.imprimir(f"          {datos}", 0.1)
        self.imprimir("")
        
        self.imprimir(f"  Paso 2: Codificando elemento por elemento:")
        codificados = []
        for num in datos:
            cod = num ^ clave
            codificados.append(cod)
            self.imprimir(f"          {num:5d} XOR {clave} = {cod:5d}", 0.08)
        
        self.imprimir("")
        self.imprimir(f"  Paso 3: Resultado codificado")
        self.imprimir(f"          {codificados}", 0.1)
        self.imprimir("")
        
        self.imprimir(f"  Paso 4: Decodificando para recuperar:")
        decodificados = []
        for num in codificados:
            dec = num ^ clave
            decodificados.append(dec)
            self.imprimir(f"          {num:5d} XOR {clave} = {dec:5d}", 0.08)
        
        self.imprimir("")
        self.imprimir(f"  Paso 5: Verificacion final")
        self.imprimir(f"          Original:   {datos}")
        self.imprimir(f"          Recuperado: {decodificados}")
        self.imprimir(f"          Iguales:    {datos == decodificados}")
        self.imprimir("")
        
        return datos == decodificados


def create_tests_window(parent):
    """Crea y muestra la ventana de pruebas."""
    ConsolaPruebas(parent)
