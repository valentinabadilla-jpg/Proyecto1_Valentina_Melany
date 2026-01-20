from mvcSistema.model.cursoModel import Curso
from mvcSistema.view.cursoView import CursoView

class CursoController:

    def __init__(self, profesor_controller):
        self.cursos = []
        self.profesor_controller = profesor_controller
        self.vista = CursoView()

    def crear(self, nombre, codigo, nombre_profesor):
        profesor = self.profesor_controller.obtener_profesor(nombre_profesor)
        curso = Curso(nombre, codigo, profesor)
        self.cursos.append(curso)
        print("Curso creado.")

    def listar(self):
        self.vista.mostrar_lista(self.cursos)