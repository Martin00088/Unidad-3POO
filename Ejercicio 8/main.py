from Menu import Menu

if __name__ == '__main__':
    user = input("Ingrese el tipo de usuario que es (general/tesorero/director) finalice con 'Nadie':")
    user.lower()
    menu = Menu()
    while user != "Nadie":
        password = input("Ingrese una contraseña:")
        if user == "tesorero" and password == "uTesoreso/ag@74ck":
            menu.tesorero()
        elif user == "director" and password == "uDirector/ufC77#!1":
            menu.director()
        elif user == "general":
            menu.op()
        else:
            print("Usuario o contraseña no valida")
        user = input("Ingrese el tipo de usuario que es (tesorero/director) finalice con 'Nadie':")
    menu.op()
