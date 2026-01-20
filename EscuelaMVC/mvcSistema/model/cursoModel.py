class Curso:

    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor

    def mostrarDatos(self):
        profe = self.profesor.nombre if self.profesor else "Sin asignar"
        return f"{self.codigo} - {self.nombre} | Profesor: {profe}"
    ##cambiado