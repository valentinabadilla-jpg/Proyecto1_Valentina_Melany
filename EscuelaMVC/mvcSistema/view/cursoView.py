def mostrarMensaje(mensaje):
    print(mensaje)

def mostrarLista(cursos):
    print("\n--- LISTA DE CURSOS ---")
    if not cursos:
        print("No hay cursos registrados")
    else:
        for curso in cursos:
            print(curso.mostrarDatos())
    print("-----------------------")
    ##cambiado