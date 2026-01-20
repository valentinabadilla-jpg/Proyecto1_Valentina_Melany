class Profesor:
    def __init__(self, nombre, apellidos, especialidad, correo, telefono, direccion, fecha_nacimiento):
        if "@" not in correo:
            raise ValueError("Correo inválido")
        self.nombre = nombre
        self.apellidos = apellidos
        self.especialidad = especialidad
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento