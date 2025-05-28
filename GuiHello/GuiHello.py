
#título de práctica: GUIHello


#Autor: Isaac Alfonso Rodriguez
#<Ialfonsor@academia.usbbog.edu.co>
#Fecha: 2025-05-26



import tkinter as tk
from tkinter import messagebox

class VentanaSaludo:
    def _init_(self, ventana):
        self.ventana = ventana
        ventana.title("Bienvenida")

        # Texto guía
        self.etiqueta_nombre = tk.Label(ventana, text="¿Cuál es tu nombre?")
        self.etiqueta_nombre.grid(row=0, column=0, padx=8, pady=10)

        # Entrada de texto
        self.campo_nombre = tk.Entry(ventana)
        self.campo_nombre.grid(row=0, column=1, padx=8)

        # Botón para saludar
        self.boton_saludar = tk.Button(ventana, text="Mostrar saludo", command=self.mostrar_saludo)
        self.boton_saludar.grid(row=1, column=0, pady=10)

        # Botón para cerrar
        self.boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
        self.boton_cerrar.grid(row=1, column=1)

    def mostrar_saludo(self):
        nombre_usuario = self.campo_nombre.get().strip()
        if nombre_usuario:
            mensaje = f"¡Saludos, {nombre_usuario}!"
        else:
            mensaje = "Por favor escribe tu nombre."
        messagebox.showinfo("Saludo personal", mensaje)

# Punto de entrada del programa
if _name_ == "_main_":
    ventana_principal = tk.Tk()
    interfaz = VentanaSaludo(ventana_principal)
    ventana_principal.mainloop()
