import re

ejecutar=True
i=5 #utilizaremos la i para definir un numero maximo de intentos para introducir el correo

while ejecutar==True:
    if i<5:
        correo=input(str("introduzca su direccion de correo electronico: "))
        if re.search(".+@.+..+", correo)!=None:
            lista=re.split("@", correo)
            print("Direccion de correo electronico correcta, bienvenido")
            ejecutar=False
        else: 
            print("La direccion de correo electronico introducida no existe o no es valida")
    else:
        print("L o sentimos, usted ha sobrepasado el numero de intentos permitidos, intentelo mas tarde")

    
