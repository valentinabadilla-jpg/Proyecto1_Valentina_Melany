from mvcSistema.controller.estudianteController import EstudianteController
from mvcSistema.controller.profesorController import ProfesorController
from mvcSistema.controller.cursoController import CursoController

estudiantes = EstudianteController()
profesores = ProfesorController()
cursos = CursoController(profesores)

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestión Estudiantes")
        print("2. Gestión Profesores")
        print("3. Gestión Cursos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estudiantes.listar()
        elif opcion == "2":
            profesores.listar()
        elif opcion == "3":
            cursos.listar()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

menu()