from mvcSistema.controller.estudianteController import EstudianteController
from mvcSistema.controller.profesoresController import ProfesoresController
from mvcSistema.controller.cursoController import CursosController

estudiantes = EstudianteController()
profesores = ProfesoresController()
cursos = CursosController(profesores)

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1. Gestion de Estudiantes")
    print("2. Gestion de Profesores")
    print("3. Gestion de Cursos")
    print("4. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":
        print("\n1. Registrar\n2. Listar\n3. Buscar\n4. Actualizar\n5. Eliminar\n6. Volver")
        sub = input("Opción: ")

        if sub == "1":
            datos = (
                input("Nombre: "), input("Apellidos: "), input("Edad: "),
                input("Teléfono: "), input("Dirección: "),
                input("Fecha nacimiento: "), input("Grado: "),
                input("Correo: ")
            )
            estudiantes.registrar(datos)

        elif sub == "2":
            estudiantes.listar()

        elif sub == "3":
            nombre = input("Nombre: ")
            est = estudiantes.buscarPorNombre(nombre)
            print(est.mostrarDatos() if est else "No encontrado")

        elif sub == "4":
            estudiantes.actualizar(input("Nombre: "), input("Nuevo grado: "))

        elif sub == "5":
            estudiantes.eliminar(input("Nombre: "))

    elif opcion == "2":
        print("\n1. Registrar\n2. Listar\n3. Eliminar\n4. Volver")
        sub = input("Opción: ")

        if sub == "1":
            datos = (
                input("Nombre: "), input("Apellidos: "),
                input("Especialidad: "), input("Correo: "),
                input("Teléfono: "), input("Dirección: "),
                input("Fecha nacimiento: ")
            )
            profesores.registrar(datos)

        elif sub == "2":
            profesores.listar()

        elif sub == "3":
            profesores.eliminar(input("Nombre: "))

    elif opcion == "3":
        print("\n1. Crear curso\n2. Listar cursos\n3. Eliminar curso\n4. Volver")
        sub = input("Opción: ")

        if sub == "1":
            cursos.crear(input("Nombre curso: "), input("Código: "), input("Profesor: "))

        elif sub == "2":
            cursos.listar()

        elif sub == "3":
            cursos.eliminar(input("Código: "))

    elif opcion == "4":
        print("Saliendo del sistema...")
        break