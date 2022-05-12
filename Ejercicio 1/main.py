from Menu import Menu

if __name__ == '__main__':
    print("0:Exit\n1. Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.\n2.  Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.")
    op = int(input("Ingrese un numero de opcion:"))
    while op != 0:
        menu = Menu(op)
        menu.menuop()
        op = int(input("Ingrese un numero de opcion:"))
