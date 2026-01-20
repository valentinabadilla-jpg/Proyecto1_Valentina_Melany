def mostrarMensaje(mensaje):
    print(mensaje)

def mostrarLista(estudiantes):
    print("\n--- LISTA DE ESTUDIANTES ---")
    if not estudiantes:
        print("No hay estudiantes registrados")
    else:
        for est in estudiantes:
            print(est.mostrarDatos())
    print("----------------------------")
    ##cambiado