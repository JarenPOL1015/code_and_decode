import tkinter as tk
from tkinter import messagebox


class UIConfig:
    """Configuracion de colores y estilos."""
    
    COLOR_PRIMARIO = "#2C3E50"
    COLOR_SECUNDARIO = "#3498DB"
    COLOR_ACENTO = "#E74C3C"
    COLOR_FONDO = "#ECF0F1"
    COLOR_TEXTO = "#FFFFFF"
    COLOR_GRIS = "#BDC3C7"          
    COLOR_VERDE = "#27AE60"         
    COLOR_GRIS_OSCURO = "#95A5A6"   
    
    FONT_TITULO = ("Arial", 24, "bold")
    FONT_SUBTITULO = ("Arial", 11)
    FONT_LABEL = ("Arial", 12, "bold")
    FONT_NORMAL = ("Arial", 10)
    FONT_BOTON = ("Arial", 12, "bold")
    FONT_CODIGO = ("Courier", 9)


def create_button(parent, text, command, color):
    """Crea un boton con estilo consistente."""
    btn = tk.Button(
        parent,
        text=text,
        command=command,
        font=UIConfig.FONT_BOTON,
        bg=color,
        fg=UIConfig.COLOR_TEXTO,
        activebackground="#34495E",
        activeforeground=UIConfig.COLOR_TEXTO,
        border=0,
        padx=20,
        pady=15,
        cursor="hand2"
    )
    return btn


def create_label(parent, text, font=UIConfig.FONT_NORMAL, bg=None, fg=None, **kwargs):
    """Crea una etiqueta con estilo consistente."""
    if bg is None:
        bg = UIConfig.COLOR_FONDO
    if fg is None:
        fg = UIConfig.COLOR_PRIMARIO
    
    label = tk.Label(
        parent,
        text=text,
        font=font,
        bg=bg,
        fg=fg,
        **kwargs
    )
    return label


def create_entry(parent, width=40, **kwargs):
    """Crea un campo de entrada con estilo consistente."""
    entry = tk.Entry(
        parent,
        font=UIConfig.FONT_NORMAL,
        width=width,
        bd=2,
        relief=tk.SOLID,
        **kwargs
    )
    return entry


def create_frame(parent, bg=None, **kwargs):
    """Crea un frame con estilo consistente."""
    if bg is None:
        bg = UIConfig.COLOR_FONDO
    
    frame = tk.Frame(parent, bg=bg, **kwargs)
    return frame


def show_info_message(title, message):
    """Muestra un mensaje de informacion."""
    messagebox.showinfo(title, message)


def show_error_message(title, message):
    """Muestra un mensaje de error."""
    messagebox.showerror(title, message)


def show_warning_message(title, message):
    """Muestra un mensaje de advertencia."""
    messagebox.showwarning(title, message)
