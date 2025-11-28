import tkinter as tk
from algorithms.decodificacion import decodificar
from algorithms.codificacion import codificar
from functions.file_parser import write_numbers_to_file, save_original_file, cleanup_temporary_files
from ui.components import create_frame, UIConfig, show_info_message, show_warning_message, show_error_message
from ui.dialogs import create_data_info_section, create_action_buttons, create_header_section, create_load_method_window
from tests.gui_tests import create_tests_window


class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Codificacion y Decodificacion de Numeros")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        self.root.configure(bg=UIConfig.COLOR_FONDO)
        
        self.datos = []
        self.setup_ui()
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_ui(self):
        main_frame = create_frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        top_frame = create_frame(main_frame, bg=UIConfig.COLOR_PRIMARIO, height=200)
        top_frame.pack(fill=tk.X, side=tk.TOP)
        top_frame.pack_propagate(False)
        
        create_header_section(top_frame)
        
        content_frame = create_frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.datos_label = create_data_info_section(content_frame)
        
        callbacks = {
            'cargar': self.cargar_datos,
            'codificar': self.codificar_datos,
            'decodificar': self.decodificar_datos,
            'pruebas': self.mostrar_pruebas,
            'salir': self.on_closing
        }
        create_action_buttons(content_frame, callbacks)
    
    def actualizar_estado(self):
        if self.datos:
            texto = f"Datos actuales: {self.datos}"
        else:
            texto = "No hay datos cargados"
        self.datos_label.config(text=texto)
    
    def cargar_datos(self):
        create_load_method_window(self.root, self)
    
    def codificar_datos(self):
        if not self.datos:
            show_warning_message("Advertencia", "No hay datos cargados")
            return
        
        datos_codificados = codificar(self.datos)
        self.datos = datos_codificados
        self.actualizar_estado()
        
        try:
            archivo = write_numbers_to_file(datos_codificados, "encoded")
            show_info_message("Codificacion Exitosa", f"Datos codificados:\n{datos_codificados}\n\nArchivo guardado: {archivo}")
        except IOError as e:
            show_error_message("Error al guardar", str(e))
    
    def decodificar_datos(self):
        if not self.datos:
            show_warning_message("Advertencia", "No hay datos cargados")
            return
        
        datos_decodificados = decodificar(self.datos)
        self.datos = datos_decodificados
        self.actualizar_estado()
        
        try:
            archivo = write_numbers_to_file(datos_decodificados, "decoded")
            show_info_message(
                "Decodificacion Exitosa",
                f"Datos decodificados:\n{datos_decodificados}\n\nArchivo guardado: {archivo}"
            )
        except IOError as e:
            show_error_message("Error al guardar", str(e))
    
    def mostrar_pruebas(self):
        """Muestra la ventana de pruebas"""
        create_tests_window(self.root)
    
    def on_closing(self):
        """Limpia archivos y cierra la aplicacion"""
        from tkinter import messagebox
        cleanup_temporary_files()
        messagebox.showinfo(
            "Archivos Eliminados",
            "Todos los archivos han sido eliminados:\n\n"
            "- Archivos subidos/cargados\n"
            "- Archivos codificados\n"
            "- Archivos decodificados\n\n"
            "Solo se conserva: nums.txt"
        )
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()
