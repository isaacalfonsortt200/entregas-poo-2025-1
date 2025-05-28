
#título de práctica: GUIHello


#Autor: Isaac Alfonso Rodriguez
#<Ialfonsor@academia.usbbog.edu.co>
#Fecha: 2025-05-26

import tkinter as tk
from tkinter import messagebox


class AplicacionSaludo:
    """
    Clase principal para la aplicación de saludo.
    Crea una interfaz gráfica con un campo de entrada, botones y etiquetas.
    """

    def __init__(self, master):
        """
        Inicializa la interfaz gráfica.
        :param master: Ventana raíz de Tkinter.
        """
        self.master = master
        master.title("Saludo en GUI")
        master.geometry("300x150")
        master.configure(bg="#f0f0f0")

        # Label: texto para indicar que se ingrese el nombre
        self.label = tk.Label(master, text="¿Cómo te llamas?", font=("Arial", 12), bg="#f0f0f0")
        self.label.pack(pady=10)

        # Entry: campo de texto para ingresar el nombre
        self.entrada_nombre = tk.Entry(master, width=25)
        self.entrada_nombre.pack()

        # Botón para mostrar el saludo
        self.boton_saludo = tk.Button(master, text="Saludar", command=self.mostrar_saludo, bg="#4CAF50", fg="white")
        self.boton_saludo.pack(pady=5)

        # Botón para salir de la aplicación
        self.boton_salir = tk.Button(master, text="Salir", command=master.quit, bg="#f44336", fg="white")
        self.boton_salir.pack()

    def mostrar_saludo(self):
        """
        Toma el nombre ingresado y muestra un saludo con messagebox.
        """
        nombre = self.entrada_nombre.get().strip()
        if nombre:
            mensaje = f"Hola {nombre}!"
            messagebox.showinfo("Saludo", mensaje)
        else:
            messagebox.showwarning("Campo vacío", "Por favor, ingresa tu nombre.")


# Punto de entrada principal del programa
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionSaludo(ventana)
    ventana.mainloop()
