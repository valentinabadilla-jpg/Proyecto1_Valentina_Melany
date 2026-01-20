class EstudianteView:

    def mostrar_estudiante(self, estudiante):
        print(f"{estudiante.nombre} {estudiante.apellidos} | Grado: {estudiante.grado} | Correo: {estudiante.correo}")

    def mostrar_lista(self, estudiantes):
        if not estudiantes:
            print("No hay estudiantes registrados.")
        for est in estudiantes:
            self.mostrar_estudiante(est)