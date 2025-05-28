"""
Título de práctica: Mascotas2

Autor: Isaac Alfonso Rodriguez
<Ialfonsor@academia.usbbog.edu.co>
Fecha: 2025-04-27
"""

from datetime import datetime


class Mascota:
    """Clase base para una mascota."""
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre.capitalize()
        self.edad = edad
        self.raza = raza.capitalize()
        self.fecha_ingreso = datetime.now().isoformat()


class Visualizador:
    """Clase para mostrar un resumen de mascotas."""

    def resumen(self, lista_mascotas):
        print("> Resumen:")
        print("|Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
        for mascota in lista_mascotas:
            clase = mascota.__class__.__name__
            print(f"|{clase:<6}|{mascota.nombre:<9}|{mascota.edad} años|{mascota.raza:<13}|{mascota.fecha_ingreso:<25}|" )


class Perro(Mascota, Visualizador):
    """Clase Perro, hereda de Mascota y Visualizador."""
    pass


class Gato(Mascota, Visualizador):
    """Clase Gato, hereda de Mascota y Visualizador."""
    pass


def ingresar_mascota(num):
    tipo = input(f"> Mascota {num}, ¿qué clase es (P)erro o (G)ato?\n< ").strip().lower()
    while tipo not in ['p', 'perro', 'g', 'gato']:
        print("> Opción no válida. Ingrese 'perro' o 'gato'")
        tipo = input(f"< ").strip().lower()

    nombre = input(f"> ¿Cuál es el nombre del {'Perro' if tipo.startswith('p') else 'Gato'}?\n< ").strip()
    edad = int(input(f"> ¿Qué edad tiene '{nombre}'?\n< "))
    raza = input(f"> ¿De qué raza es '{nombre}'?\n< ").strip()

    if tipo.startswith('p'):
        return Perro(nombre, edad, raza)
    else:
        return Gato(nombre, edad, raza)


def main():
    mascotas = []

    cantidad = int(input("> ¿Cuántas mascotas va a ingresar?\n< "))
    for i in range(1, cantidad + 1):
        mascota = ingresar_mascota(i)
        mascotas.append(mascota)

    # Llamamos a resumen desde Visualizador
    visualizador = Visualizador()
    visualizador.resumen(mascotas)


if __name__ == "__main__":
    main()
