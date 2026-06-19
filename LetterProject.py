import tkinter as tk
import sys
import os

def vent_mostrar(titulo, frases):
    estado = {"corriendo": True}

    def cerrar_todo():
        estado["corriendo"] = False
        root.destroy()
        sys.exit() 

    ruta_imagen = "imagen2.png"
    imagen_cargada = None
    if os.path.exists(ruta_imagen):
        try:
            imagen_original = tk.PhotoImage(file=ruta_imagen)
            imagen_cargada = imagen_original.subsample(10, 10)
        except Exception as e:
            print(f"Error cargando imagen: {e}")

    for frase in frases:
        if not estado["corriendo"]:
            break

        ventana = tk.Toplevel()
        ventana.title(titulo)
        ventana.attributes('-toolwindow', True)
        
        ventana.protocol("WM_DELETE_WINDOW", cerrar_todo)
        
        ancho_v, alto_v = 380, 160 
        x = (ventana.winfo_screenwidth() // 2) - (ancho_v // 2)
        y = (ventana.winfo_screenheight() // 3) - (alto_v // 3)
        ventana.geometry(f"{ancho_v}x{alto_v}+{x}+{y}")
        
        frame_principal = tk.Frame(ventana)
        frame_principal.pack(fill="both", expand=True, pady=10)

        if imagen_cargada:
            label_imagen = tk.Label(frame_principal, image=imagen_cargada)
            label_imagen.pack(side="left", padx=(10, 15))

        frame_derecho = tk.Frame(frame_principal)
        frame_derecho.pack(side="left", expand=True, fill="both")

        label_texto = tk.Label(frame_derecho, text=frase, font=("Arial", 12), wraplength=200)
        label_texto.pack(expand=True, pady=(15, 5))

        boton = tk.Button(frame_derecho, text="Aceptar", width=10, command=ventana.destroy)
        boton.pack(pady=(0, 15))

        ventana.lift()
        ventana.focus_force()

        ventana.grab_set()
        try:
            root.wait_window(ventana)
        except tk.TclError:
            break

root = tk.Tk()
root.withdraw()

Letra2 = [
    "Is it true?",
    "You've been feelin' sort of low these days",
    "Just don't have a place to go these days",
    "Must be bringin' you down",
    "If it's so",
    "Then come on, give this loverboy a try",
    "I'll put the sparkle right back in your eyes",
    "What could you lose?"
]

vent_mostrar("Blue Hair - TV Girl", Letra2)