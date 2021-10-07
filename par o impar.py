#Par o impar
#Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000

#Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje con el resultado.

#Ejemplo:

#Mensaje que se muestra: ¿En qué número estás pensando?
#Entrada: 25
#Salida: ¡Es un número impar! ¿Puedes añadir otro?


while True:
    
        
    num=int(input("piensa un número entre 1 y mil, despues teclealo: "))
    if num==0:
        print("no funciona asi, lo siento")
    elif num%2==0:
        print(num," es par")
    
    else:
        print(num, " es impar")
    print("vamos trata de engañar al sistema, no escribas cero")        

