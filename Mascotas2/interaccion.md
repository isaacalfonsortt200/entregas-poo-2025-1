Detecta si el objeto es un Perro o un Gato (usando isinstance), y crea una cadena de texto alineada que muestra:
tipo de animal (Perro o Gato),
nombre,
edad,
raza,
fecha de ingreso.

2. _init_(self, nombre, edad, raza) en Mascota
¿Qué hace?
Inicializa una nueva mascota guardando su:
nombre,
edad,
raza,
fecha de ingreso (usa la fecha actual con datetime.now()).

3. _init_(self, nombre, edad, raza) en Perro
¿Qué hace?
Llama el _init_ de Mascota para no reescribir el mismo código.
Así un Perro guarda nombre, edad, raza, y fecha de ingreso igual que Mascota.

4. _init_(self, nombre, edad, raza) en Gato
¿Qué hace?
Igual que en Perro, llama al _init_ de Mascota.
Un Gato guarda los mismos datos.

5. registrar_mascota()
¿Qué hace?
Es la función principal que:
Pregunta cuántas mascotas quieres ingresar,
Para cada mascota:
Pregunta si es Perro o Gato,
Pide nombre, edad y raza,
Crea un objeto Perro o Gato,
Lo guarda en una lista mascotas
Finalmente imprime un resumen de todas las mascotas usando resumen() de cada una.
Mascota es la clase base: Perro y Gato son subclases (hijas) que heredan de ella.
