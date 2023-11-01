def Limpiar_pantalla():
    from os import system
    system("cls")

def menu():
    print("Bienvenidos a nuestra plataforma.\n¿Qué desea realizar?: ")
    print("1- Buscar libro")
    print("2- Salir")

    option_str = input("Ingrese la opción deseada: ")
    option = int(option_str)

    if option == 1:
        print("Vamos a buscar el libro.\nDesea buscarlo por: ")
        print("1- Título")
        print("2- Autor")
        print("3- Categoría")

        search_option_str = input("Ingrese la opción de búsqueda: ")
        search_option = int(search_option_str)

        if search_option == 1:
            titulo = input("Ingrese el título del libro: ")
            print("Ha ingresado el título:", titulo)

        elif search_option == 2:
            autor = input("Ingrese el autor del libro: ")
            print("Ha ingresado el autor:", autor)
            
        elif search_option == 3:
            categoria = input("Ingrese la categoría del libro: ")
            print("Ha ingresado la categoría:", categoria)
        else:
            print("Opción de búsqueda no válida")
    elif option == 2:
        print("Hasta luego")
    else:
        print("Esa no es una opción válida")

menu()

