def mostrarMensaje(mensaje):
    print(mensaje)

def mostrarLista(profesores):
    print("\n--- LISTA DE PROFESORES ---")
    if not profesores:
        print("No hay profesores registrados")
    else:
        for prof in profesores:
            print(prof.mostrarDatos())
    print("---------------------------")
    ##cambiado