from mvcSistema.model.profesoresModel import Profesor
import mvcSistema.view.profesoresView as vista

class ProfesoresController:

    def __init__(self):
        self.listaProfesores = []

    def registrar(self, datos):
        try:
            profesor = Profesor(*datos)
            self.listaProfesores.append(profesor)
            vista.mostrarMensaje("Profesor registrado correctamente")
        except ValueError as error:
            vista.mostrarMensaje(error)

    def listar(self):
        vista.mostrarLista(self.listaProfesores)

    def obtenerProfesorPorNombre(self, nombre):
        for prof in self.listaProfesores:
            if prof.nombre.lower() == nombre.lower():
                return prof
        return None

    def eliminar(self, nombre):
        profesor = self.obtenerProfesorPorNombre(nombre)
        if profesor:
            self.listaProfesores.remove(profesor)
            vista.mostrarMensaje("Profesor eliminado")
        else:
            vista.mostrarMensaje("Profesor no encontrado")
##cambiado