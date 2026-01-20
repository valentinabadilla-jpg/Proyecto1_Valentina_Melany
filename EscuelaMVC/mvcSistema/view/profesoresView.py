class ProfesorView:

    def mostrar_profesor(self, profesor):
        print(f"{profesor.nombre} {profesor.apellidos} | {profesor.especialidad} | {profesor.correo}")

    def mostrar_lista(self, profesores):
        if not profesores:
            print("No hay profesores registrados.")
        for prof in profesores:
            self.mostrar_profesor(prof)