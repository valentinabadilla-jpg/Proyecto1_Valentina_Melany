class CursoView:

    def mostrar_curso(self, curso):
        profesor = curso.profesor.nombre if curso.profesor else "Sin asignar"
        print(f"{curso.codigo} - {curso.nombre} | Profesor: {profesor}")

    def mostrar_lista(self, cursos):
        if not cursos:
            print("No hay cursos creados.")
        for curso in cursos:
            self.mostrar_curso(curso)