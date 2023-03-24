import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master
        self.var = tk.StringVar(value="")  # inicializamos la variable de control con una cadena vacía

        # creamos los RadioButton y los añadimos a un Frame
        opciones = ["Opción 1", "Opción 2", "Opción 3"]
        self.frame_opciones = tk.Frame(master)
        for opcion in opciones:
            rb = tk.Radiobutton(self.frame_opciones, text=opcion, variable=self.var, value=opcion,
                                command=self.mostrar_seleccion)
            rb.pack(side="left")

        # creamos el botón para reiniciar la selección
        self.btn_reset = tk.Button(master, text="Reset", command=self.reset_seleccion)

        # mostramos los widgets
        self.frame_opciones.pack()
        self.btn_reset.pack()

    def mostrar_seleccion(self):
        seleccion = self.var.get()
        print(f"Has seleccionado: {seleccion}")

    def reset_seleccion(self):
        self.var.set("")  # establecemos la variable de control a una cadena vacía
        print("Selección reiniciada")


root = tk.Tk()
app = App(root)
root.mainloop()

