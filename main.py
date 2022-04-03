import re

def main():
    acabar=False
    while acabar==False:
        ver=input("¿Quieres ver el ejercicio?: ")
        if ver=="si" or ver=="Si" or ver=="SI":
            ejecutar=True
            i=0 #utilizaremos la i para definir un numero maximo de intentos para introducir el correo

            while ejecutar==True:
                if i<5:
                    correo=input(str("introduzca su direccion de correo electronico: "))
                    if re.search(".+@.+..+", correo)!=None:
                        lista=re.split("@", correo)
                        print("Direccion de correo electronico correcta, bienvenido")
                        ejecutar=False
                    else:
                        print("La direccion de correo electronico introdcida no existe o no es valida")
                else:
                    print("Lo sentimos, usted ha sobrepasado el numero maximo de intentos, intentelo mas tarde")
                ejecutar=False
                i=i+1
        else:
            acabar=True
if __name__=='__main__':
    main()