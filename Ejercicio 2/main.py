from Menu import Menu
if __name__ == '__main__':
    print("0:Exit\n1:Registrar un ramo vendido (instancia de la clase ramo), solicitando las flores que lo que se pondrán en el ramo.\n2:Mostrar el nombre de las 5 flores  más pedidas en un ramo, considerando todos los ramos vendidos.\n4:Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos.")
    op = int(input("Ingrese un numero de opcion:"))
    while op != 0:
        menu = Menu(op)
        menu.menuOp()
        print("0:Exit\n1:Registrar un ramo vendido (instancia de la clase ramo), solicitando las flores que lo que se pondrán en el ramo.\n2:Mostrar el nombre de las 5 flores  más pedidas en un ramo, considerando todos los ramos vendidos.\n4:Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos.")
        op = int(input("Ingrese un numero de opcion:"))
