# excepciones-en-poo

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/excepciones-en-poo.git)

Hemos realizado un ejercicio que simula una pagina en la que ya estamos registrados, y nos pide nuestro correo electronico para poder iniciar sesion, asi mismo nos pide definir los diferentes casos de errores que puede cometer el usuario

### Ejercicio de excepciones en POO

El codigo que hemps usado para resolver el ejercicio es el siguiente:

```
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
        print("Lo sentimos, usted ha sobrepasado el numero de intentos permitidos, intentelo mas tarde")
    ejecutar=False
    i=i+1
```
 ### Nota: al haber resuelto el ejercicio sin el uso de clases, el codigo del main es el mismo que el del ejercicio.
