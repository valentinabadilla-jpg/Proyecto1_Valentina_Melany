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
        return (
            f"ID: {self.id} | "
            f"Nombre: {self.nombre} {self.apellidos} | "
            f"Especialidad: {self.especialidad} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono} | "
            f"Dirección: {self.direccion} | "
            f"Fecha Nac.: {self.fechanacimiento}"
        )