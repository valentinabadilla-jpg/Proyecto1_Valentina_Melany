from mvcSistema.model.estudianteModel import Estudiante
import mvcSistema.view.estudianteView as vista

class EstudianteController:

    def __init__(self):
        self.listaEstudiantes = []

    def registrar(self, datos):
        estudiante = Estudiante(*datos)
        self.listaEstudiantes.append(estudiante)
        vista.mostrarMensaje("Estudiante registrado correctamente")

    def listar(self):
        vista.mostrarLista(self.listaEstudiantes)

    def buscarPorNombre(self, nombre):
        for est in self.listaEstudiantes:
            if est.nombre.lower() == nombre.lower():
                return est
        return None

    def actualizar(self, nombre, nuevoGrado):
        estudiante = self.buscarPorNombre(nombre)
        if estudiante:
            estudiante.grado = nuevoGrado
            vista.mostrarMensaje("Estudiante actualizado")
        else:
            vista.mostrarMensaje("Estudiante no encontrado")

    def eliminar(self, nombre):
        estudiante = self.buscarPorNombre(nombre)
        if estudiante:
            self.listaEstudiantes.remove(estudiante)
            vista.mostrarMensaje("Estudiante eliminado")
        else:
            vista.mostrarMensaje("Estudiante no encontrado")
            ##cambiado