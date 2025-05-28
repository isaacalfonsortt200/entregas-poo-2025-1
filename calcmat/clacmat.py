"""
Práctica de clase: MatrizCalc

Este programa realiza operaciones con matrices 2x2.

Autor: Isaac Alfonso Rodriguez
<ialfonsor@academia.usbbog.edu.co>
"""

class Matriz:
    def __init__(self, elementos):
        if len(elementos) != 2 or any(len(fila) != 2 for fila in elementos):
            raise ValueError("La matriz debe ser de tamaño 2x2.")
        self.valores = elementos

    def __add__(self, otra):
        return Matriz([
            [self.valores[i][j] + otra.valores[i][j] for j in range(2)]
            for i in range(2)
        ])

    def __sub__(self, otra):
        return Matriz([
            [self.valores[i][j] - otra.valores[i][j] for j in range(2)]
            for i in range(2)
        ])

    def __mul__(self, otra):
        return Matriz([
            [
                self.valores[i][0] * otra.valores[0][j] + self.valores[i][1] * otra.valores[1][j]
                for j in range(2)
            ]
            for i in range(2)
        ])

    def mostrar(self):
        print(f"| {self.valores[0][0]}  {self.valores[0][1]} |")
        print(f"| {self.valores[1][0]}  {self.valores[1][1]} |")


def ingresar_matriz(numero):
    print(f"\n> Ingrese los valores de la matriz {numero} (2x2):")
    elementos = []
    for i in range(2):
        fila = []
        for j in range(2):
            while True:
                try:
                    valor = int(input(f"  - Elemento [{i+1},{j+1}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("  ! Valor no válido. Ingrese un número entero.")
        elementos.append(fila)
    return Matriz(elementos)


def main():
    print("=== CALCULADORA DE MATRICES 2x2 ===")
    
    matriz1 = ingresar_matriz(1)
    matriz2 = ingresar_matriz(2)

    print("\n> Matriz 1:")
    matriz1.mostrar()
    print("> Matriz 2:")
    matriz2.mostrar()

    print("\n> Seleccione una operación:")
    print("  1. Suma")
    print("  2. Resta")
    print("  3. Multiplicación")

    while True:
        try:
            opcion = int(input("< Opción: "))
            if opcion not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print("  ! Opción inválida. Intente de nuevo.")

    if opcion == 1:
        resultado = matriz1 + matriz2
        print("\n> Resultado de la suma:")
    elif opcion == 2:
        resultado = matriz1 - matriz2
        print("\n> Resultado de la resta:")
    elif opcion == 3:
        resultado = matriz1 * matriz2
        print("\n> Resultado de la multiplicación:")

    resultado.mostrar()


if __name__ == "__main__":
    main()
