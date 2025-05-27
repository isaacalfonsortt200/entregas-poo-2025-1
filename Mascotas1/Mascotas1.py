"""
título de práctica: Mascotas1


Autor: Isaac A lfonso R odriguez
<Ialfonsor@academia.usbbog.edu.co>
Fecha: 2025-03-30
"""


from datetime import datetime

class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().isoformat()
    
    def mostrar_info(self):
        clase = "Perro" if isinstance(self, Perro) else "Gato"
        return f"| {clase:<5} | {self.nombre:<8} | {self.edad:<4} años | {self.raza:<12} | {self.fecha_ingreso} |"

class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)

class Gato(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)

def registrar_mascota():
    mascotas = []
    num_mascotas = int(input("Cuantas mascotas va a ingresar?\n> "))
    
    for i in range(1, num_mascotas + 1):
        tipo = input(f"Mascota {i}, que clase es (Perro/Gato)?\n> ").strip().lower()
        
        while tipo not in ['perro', 'gato']:
            print("Opción no válida, intente de nuevo.")
            tipo = input(f"Mascota {i}, que clase es (Perro/Gato)?\n> ").strip().lower()
        
        clase = "Perro" if tipo == "perro" else "Gato"
        nombre = input(f"Cual es el nombre del {clase}?\n> ").strip()
        edad = input(f"Que edad tiene '{nombre}'?\n> ").strip()
        raza = input(f"De que raza es '{nombre}'?\n> ").strip()
        
        mascota = Perro(nombre, edad, raza) if tipo == "perro" else Gato(nombre, edad, raza)
        mascotas.append(mascota)
        print()
    
    print("Resumen:")
    print("| Clase | Nombre   | Edad  | Raza         | Fecha de ingreso          |")
    print("|-------|---------|-------|-------------|--------------------------|")
    for mascota in mascotas:
        print(mascota.mostrar_info())

# Ejecutar la función de registro
registrar_mascota()
