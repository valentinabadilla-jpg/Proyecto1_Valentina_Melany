from mvcSistema.model.profesorModel import Profesor
from mvcSistema.view.profesorView import ProfesorView

class ProfesorController:

    def __init__(self):
        self.profesores = []
        self.vista = ProfesorView()

    def registrar(self, datos):
        try:
            profesor = Profesor(*datos)
            self.profesores.append(profesor)
            print("Profesor registrado.")
        except ValueError as error:
            print(error)

    def listar(self):
        self.vista.mostrar_lista(self.profesores)

    def obtener_profesor(self, nombre):
        for prof in self.profesores:
            if prof.nombre.lower() == nombre.lower():
                return prof
        return None