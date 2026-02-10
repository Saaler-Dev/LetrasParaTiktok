import tkinter as tk
import sys

def vent_mostrar(titulo, frases):
    """
    Crea una secuencia de ventanas emergentes centradas.
    Argumentos:
        titulo (str): El texto que aparecerá como encabezado.
        frases (list): Una lista de strings con las letras que va a mostrar.
    """
    estado = {"corriendo": True}

    def cerrar_todo():
        
        estado["corriendo"] = False
        root.destroy()
        sys.exit() 

    for frase in frases:
        if not estado["corriendo"]:
            break

        ventana = tk.Toplevel()
        ventana.title(titulo)
        ventana.attributes('-toolwindow', True)
        
        ventana.protocol("WM_DELETE_WINDOW", cerrar_todo)
        
        ancho_v, alto_v = 350, 150
        x = (ventana.winfo_screenwidth() // 2) - (ancho_v // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto_v // 2)
        ventana.geometry(f"{ancho_v}x{alto_v}+{x}+{y}")
        
        label = tk.Label(ventana, text=frase, font=("Arial", 11), pady=30)
        label.pack()

        boton = tk.Button(ventana, text="Aceptar",width=10,command=ventana.destroy)
        boton.pack()

        ventana.grab_set()
        try:
            root.wait_window(ventana)
        except tk.TclError:
            break

root = tk.Tk()
root.withdraw()

Letra = [
    "Are you sick of me..? ( ._.)",
    "Would you like to be?",
    "I'm tryin' to tell you somethin'",
    "Somethin' that I already said",
    "You like a pretty boy ._.",
    "with a pretty voice...",
    "Who is tryin' to sell you somethin'",
    "Somethin' that you already have",
    "But if you're too drunk to drive",
    "and the music is right",
    "She might let you stay",
    "but just for the night",
    "And if she grabs for your hand ( o_o)",
    "and drags you along",
    "She might want a kiss",
    "before the end of the song...",
    "Because love can burn like a cigarette...",
    "And leave you with nothing :c",
    "And leave you with nothing...",
]

vent_mostrar("Lovers Rock", Letra)