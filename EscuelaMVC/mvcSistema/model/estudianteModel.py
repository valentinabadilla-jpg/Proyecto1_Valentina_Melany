class Estudiante:

    contadorId = 1

    def __init__(self, nombre, apellidos, edad, telefono, direccion,
                 fechanacimiento, grado, correo):
        self.id = Estudiante.contadorId
        Estudiante.contadorId += 1

        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion
        self.fechanacimiento = fechanacimiento
        self.grado = grado
        self.correo = correo

    def mostrarDatos(self):
        return f"ID:{self.id} {self.nombre} {self.apellidos} | Grado:{self.grado} | Correo:{self.correo}"
    ##cambiado