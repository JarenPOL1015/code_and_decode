import tkinter as tk
from ui.components import create_frame, create_button, create_label, UIConfig
from ui.components import show_info_message, show_error_message
from functions.comma_parser import parse_comma_separated_input
from functions.file_parser import read_numbers_from_file, save_original_file, get_files_directory
from config import MAX_NUMBERS
import os


def _create_action_button_pair(frame, btn1_text, btn1_cmd, btn2_text, btn2_cmd):
    """Crea un par de botones de accion."""
    btn1 = create_button(frame, btn1_text, btn1_cmd, UIConfig.COLOR_SECUNDARIO)
    btn1.pack(fill=tk.X, pady=5)
    
    btn2 = create_button(frame, btn2_text, btn2_cmd, UIConfig.COLOR_GRIS)
    btn2.pack(fill=tk.X, pady=5)


def create_data_info_section(parent):
    """Crea la seccion de estado de datos."""
    info_frame = create_frame(parent, bg=UIConfig.COLOR_SECUNDARIO, relief=tk.RAISED, bd=2)
    info_frame.pack(fill=tk.X, pady=(0, 20))
    
    info_label = create_label(
        info_frame,
        "Estado de Datos",
        font=UIConfig.FONT_LABEL,
        bg=UIConfig.COLOR_SECUNDARIO,
        fg=UIConfig.COLOR_TEXTO
    )
    info_label.pack(anchor=tk.W, padx=15, pady=(10, 5))
    
    datos_label = create_label(
        info_frame,
        "No hay datos cargados",
        font=UIConfig.FONT_NORMAL,
        bg=UIConfig.COLOR_SECUNDARIO,
        fg=UIConfig.COLOR_TEXTO,
        wraplength=700,
        justify=tk.LEFT
    )
    datos_label.pack(anchor=tk.W, padx=15, pady=(0, 10))
    
    return datos_label


def create_action_buttons(parent, callbacks):
    """Crea los botones principales del menu."""
    button_frame = create_frame(parent)
    button_frame.pack(fill=tk.BOTH, expand=True)
    
    row1_frame = create_frame(button_frame)
    row1_frame.pack(fill=tk.X, pady=10)
    
    btn_cargar = create_button(
        row1_frame,
        "Cargar Datos",
        callbacks['cargar'],
        UIConfig.COLOR_SECUNDARIO
    )
    btn_cargar.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
    
    btn_codificar = create_button(
        row1_frame,
        "Codificar",
        callbacks['codificar'],
        UIConfig.COLOR_SECUNDARIO
    )
    btn_codificar.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
    
    row2_frame = create_frame(button_frame)
    row2_frame.pack(fill=tk.X, pady=10)
    
    btn_decodificar = create_button(
        row2_frame,
        "Decodificar",
        callbacks['decodificar'],
        UIConfig.COLOR_ACENTO
    )
    btn_decodificar.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
    
    btn_pruebas = create_button(
        row2_frame,
        "Pruebas",
        callbacks['pruebas'],
        UIConfig.COLOR_VERDE
    )
    btn_pruebas.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
    
    row3_frame = create_frame(button_frame)
    row3_frame.pack(fill=tk.X, pady=10)
    
    btn_salir = create_button(
        row3_frame,
        "Salir",
        callbacks['salir'],
        UIConfig.COLOR_GRIS_OSCURO
    )
    btn_salir.pack(fill=tk.X)


def create_header_section(parent):
    """Crea el encabezado de la aplicacion."""
    header_label = create_label(
        parent,
        "Codificacion y Decodificacion de Numeros",
        font=UIConfig.FONT_TITULO,
        bg=UIConfig.COLOR_PRIMARIO,
        fg=UIConfig.COLOR_TEXTO
    )
    header_label.pack(pady=15)
    
    subtitle_label = create_label(
        parent,
        "Usa XOR para codificar y decodificar tus datos",
        font=UIConfig.FONT_SUBTITULO,
        bg=UIConfig.COLOR_PRIMARIO,
        fg=UIConfig.COLOR_SECUNDARIO
    )
    subtitle_label.pack()
    
    # Advertencia sobre eliminacion de archivos
    warning_label = create_label(
        parent,
        "AVISO: TODOS los archivos se eliminan al cerrar (excepto nums.txt)",
        font=("Segoe UI", 10),
        bg=UIConfig.COLOR_PRIMARIO,
        fg="#FFD700"
    )
    warning_label.pack(pady=(10, 0))


def create_load_method_window(parent_root, parent_app):
    """Crea ventana de seleccion de metodo de carga."""
    ventana = tk.Toplevel(parent_root)
    ventana.title("Cargar Datos")
    ventana.geometry("500x300")
    ventana.resizable(False, False)
    ventana.configure(bg=UIConfig.COLOR_FONDO)
    
    frame = create_frame(ventana)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    label = create_label(
        frame,
        "Seleccione metodo de carga:",
        font=UIConfig.FONT_LABEL
    )
    label.pack(pady=10)
    
    btn1 = create_button(
        frame,
        "Ingresar por Consola",
        lambda: load_from_console(parent_root, parent_app, ventana),
        UIConfig.COLOR_SECUNDARIO
    )
    btn1.pack(fill=tk.X, pady=10)
    
    btn2 = create_button(
        frame,
        "Cargar desde Archivo",
        lambda: load_from_file(parent_root, parent_app, ventana),
        UIConfig.COLOR_SECUNDARIO
    )
    btn2.pack(fill=tk.X, pady=10)
    
    btn_cancelar = create_button(
        frame,
        "Cancelar",
        ventana.destroy,
        UIConfig.COLOR_GRIS
    )
    btn_cancelar.pack(fill=tk.X, pady=10)


def load_from_console(parent_root, parent_app, previous_window):
    """Crea ventana para ingresar numeros manualmente."""
    ventana = tk.Toplevel(parent_root)
    ventana.title("Ingresar Numeros")
    ventana.geometry("400x250")
    ventana.resizable(False, False)
    ventana.configure(bg=UIConfig.COLOR_FONDO)
    previous_window.destroy()
    
    frame = create_frame(ventana)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    label = create_label(
        frame,
        f"Ingrese numeros separados por comas (max {MAX_NUMBERS}):",
        font=UIConfig.FONT_NORMAL
    )
    label.pack(pady=10)
    
    entry = tk.Entry(
        frame,
        font=UIConfig.FONT_NORMAL,
        width=40,
        bd=2,
        relief=tk.SOLID
    )
    entry.pack(pady=10)
    entry.focus()
    
    def guardar():
        try:
            numeros = parse_comma_separated_input(entry.get())
            parent_app.datos = numeros
            parent_app.actualizar_estado()
            archivo_original = save_original_file(numeros)
            show_info_message("Exito", f"Datos cargados: {parent_app.datos}\n\nArchivo original guardado: {archivo_original}")
            ventana.destroy()
        except ValueError as e:
            show_error_message("Error", str(e))
    
    _create_action_button_pair(frame, "Guardar", guardar, "Cancelar", ventana.destroy)


def _load_and_save_file(filename, parent_app, ventana):
    """Carga archivo y actualiza estado."""
    try:
        numeros = read_numbers_from_file(filename)
        parent_app.datos = numeros
        parent_app.actualizar_estado()
        archivo_original = save_original_file(numeros)
        show_info_message("Exito", f"Datos cargados: {parent_app.datos}\n\nArchivo original guardado: {archivo_original}")
        ventana.destroy()
    except (FileNotFoundError, ValueError) as e:
        show_error_message("Error", str(e))


def load_from_file(parent_root, parent_app, previous_window):
    """Crea ventana para cargar desde archivo."""
    ventana = tk.Toplevel(parent_root)
    ventana.title("Cargar desde Archivo")
    ventana.geometry("450x400")
    ventana.resizable(False, False)
    ventana.configure(bg=UIConfig.COLOR_FONDO)
    previous_window.destroy()
    
    frame = create_frame(ventana)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    files_dir = get_files_directory()
    original_dir = os.path.join(files_dir, "original")
    available_files = []
    if os.path.exists(original_dir):
        available_files = os.listdir(original_dir)
    
    label = create_label(frame, "Archivos disponibles en files/original/:", font=UIConfig.FONT_LABEL)
    label.pack(pady=(10, 5))
    
    if available_files:
        listbox_frame = tk.Frame(frame, bg=UIConfig.COLOR_FONDO)
        listbox_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        listbox = tk.Listbox(
            listbox_frame,
            yscrollcommand=scrollbar.set,
            font=UIConfig.FONT_NORMAL,
            bg=UIConfig.COLOR_SECUNDARIO,
            fg=UIConfig.COLOR_TEXTO,
            bd=2,
            relief=tk.SOLID
        )
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)
        
        for file in available_files:
            listbox.insert(tk.END, file)
        
        def cargar_seleccionado():
            selection = listbox.curselection()
            if selection:
                filename = listbox.get(selection[0])
                _load_and_save_file(filename, parent_app, ventana)
        
        create_button(frame, "Cargar Seleccionado", cargar_seleccionado, UIConfig.COLOR_SECUNDARIO).pack(fill=tk.X, pady=5)
    else:
        info_label = create_label(frame, "No hay archivos disponibles en files/original/", font=UIConfig.FONT_NORMAL)
        info_label.pack(pady=20)
    
    label_manual = create_label(frame, "O ingrese el nombre del archivo:", font=UIConfig.FONT_NORMAL)
    label_manual.pack(pady=(10, 5))
    
    entry = tk.Entry(frame, font=UIConfig.FONT_NORMAL, width=40, bd=2, relief=tk.SOLID)
    entry.pack(pady=10)
    entry.focus()
    
    def cargar():
        _load_and_save_file(entry.get(), parent_app, ventana)
    
    _create_action_button_pair(frame, "Cargar por Nombre", cargar, "Cancelar", ventana.destroy)
