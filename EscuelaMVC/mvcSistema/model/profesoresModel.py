class Profesor:

    contadorId = 1

    def __init__(self, nombre, apellidos, especialidad, correo,
                 telefono, direccion, fechanacimiento):

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.id = Profesor.contadorId
        Profesor.contadorId += 1

        self.nombre = nombre
        self.apellidos = apellidos
        self.especialidad = especialidad
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.fechanacimiento = fechanacimiento

    def mostrarDatos(self):
        return f"ID:{self.id} {self.nombre} {self.apellidos} | {self.especialidad}"
    ##cambiado