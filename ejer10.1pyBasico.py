import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master

        # creamos la lista de elementos seleccionables
        elementos = ["Elemento 1", "Elemento 2", "Elemento 3"]
        self.listbox = tk.Listbox(master, selectmode="single")
        for elemento in elementos:
            self.listbox.insert("end", elemento)

        # creamos el label con un texto inicial
        self.label = tk.Label(master, text="Selecciona un elemento")

        # asociamos el evento <<ListboxSelect>> a la función mostrar_seleccion
        self.listbox.bind("<<ListboxSelect>>", self.mostrar_seleccion)

        # mostramos los widgets
        self.listbox.pack()
        self.label.pack()

    def mostrar_seleccion(self, event):
        # obtenemos el elemento seleccionado y actualizamos el texto del label
        seleccion = self.listbox.get(self.listbox.curselection())
        self.label.configure(text=f"Has seleccionado: {seleccion}")


root = tk.Tk()
app = App(root)
root.mainloop()
