from Menu import Menu

if __name__ == '__main__':
    user = input("Ingrese el tipo de usuario que es (general/tesorero/director) finalice con 'Nadie':")
    menu = Menu()
    while user != "Nadie":
        password = str(input("Ingrese una contraseña:"))
        if user.lower() == "tesorero" and password == "uTesoreso/ag@74ck":
            menu.tesorero()
        elif user.lower() == "director" and password == "uDirector/ufC77#!1":
            menu.director()
        elif user.lower() == "general":
            menu.op()
        else:
            print("Usuario o contraseña no valida")
        user = input("Ingrese el tipo de usuario que es (tesorero/director) finalice con 'Nadie':")
