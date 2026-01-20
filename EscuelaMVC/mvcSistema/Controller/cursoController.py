from mvcSistema.model.cursosModel import Curso
import mvcSistema.view.cursosView as vista

class CursosController:

    def __init__(self, profesoresController):
        self.listaCursos = []
        self.profesoresController = profesoresController

    def crear(self, nombre, codigo, nombreProfesor):
        profesor = self.profesoresController.obtenerProfesorPorNombre(nombreProfesor)
        curso = Curso(nombre, codigo, profesor)
        self.listaCursos.append(curso)
        vista.mostrarMensaje("Curso creado correctamente")

    def listar(self):
        vista.mostrarLista(self.listaCursos)

    def eliminar(self, codigo):
        for curso in self.listaCursos:
            if curso.codigo == codigo:
                self.listaCursos.remove(curso)
                vista.mostrarMensaje("Curso eliminado")
                return
        vista.mostrarMensaje("Curso no encontrado")
        ##cambiado