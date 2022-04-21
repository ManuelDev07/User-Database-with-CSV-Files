import csv
import email

#Realizando el REGISTRO DEL USUARIO y subiendolo al CSV:
def registrarUsuario():

    with open("usuarios.csv", mode="a", newline="") as fichero:
        registrar = csv.writer(fichero, delimiter=",")
        print("Para Registrarte, por favor ingresa tu información:")
        email = input("Correo Electrónico: ")
        contraseña = input("Contraseña: ")
        contraseña2 = input("Verificar Contraseña: ")

        if contraseña == contraseña2:
            registrar.writerow([email, contraseña])
            print("Te haz Registrado Correctamente!")
        else:
            print("Contraseñas Inválidas. Intente de nuevo.")

#Realizando el INGRESO DEL USUARIO a la base de datos:
def ingresarUsuario():
    print("Para ingresar por favor ingrese su información:")
    email = input("Correo Electrónico: ")
    contraseña = input("Contraseña: ")

    with open("usuarios.csv", mode="r") as fichero:
        leer = csv.reader(fichero, delimiter = ",")
        
        for i in leer:
            if i == [email, contraseña]:
                print("Haz Ingresado Correctamente!")
                return True
            else:
                print("Los datos no concuerdan. Intente de nuevo.")
                return False


#Cuerpo Principal del programa donde el usuario eligirá si registrarse o ingresar a la base de datos.
logeado = False

while True:
    if logeado == True:
        print("""Menú:
        1.- (Cerrar) para Cerrar Sesión en la base de datos.
        2.- (Salir) para Salir del Programa.""")
    else:
        print("""Menú:
        1.- (Ingresar) para Ingresar a la bas de datos.
        2.- (Registrar) para Registrarme a la base de datos.
        3.- (Salir) para Salir del Programa.""")
    
    opcion = input("Que desea realizar? ").upper()

    if opcion == 'REGISTRAR' and logeado == False:
        registrarUsuario()
    elif opcion == "INGRESAR" and logeado == False:
        logeado = ingresarUsuario()
    elif opcion == 'SALIR':
        print("Hasta Pronto! :D")
        break
    elif opcion == "CERRAR" and logeado == True:
        logeado = False
        print("Se ha Cerrado Sesión")
    else:
        print("ERROR! Intente de nuevo...")