from mvcSistema.model.estudianteModel import Estudiante
from mvcSistema.view.estudianteView import EstudianteView

class EstudianteController:

    def __init__(self):
        self.estudiantes = []
        self.vista = EstudianteView()

    def registrar(self, datos):
        estudiante = Estudiante(*datos)
        self.estudiantes.append(estudiante)
        print("Estudiante registrado correctamente.")

    def listar(self):
        self.vista.mostrar_lista(self.estudiantes)

    def buscar(self, nombre):
        for est in self.estudiantes:
            if est.nombre.lower() == nombre.lower():
                self.vista.mostrar_estudiante(est)
                return est
        print("Estudiante no encontrado.")
        return None

    def eliminar(self, nombre):
        estudiante = self.buscar(nombre)
        if estudiante:
            self.estudiantes.remove(estudiante)
            print("Estudiante eliminado.")