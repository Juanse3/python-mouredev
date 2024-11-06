### Operadores ###

print(3+4) # suma
print(3-5) # resta
print(3*4) # multiplicacion
print(3/5) # division

print(4%2)  # modulo
print(10%3) # modulo
print(11 // 3) # redondeo de la división (parte entera)
print(11 / 3) # redondeo de la división (parte entera)
print(2 ** 3) # exponente

print("hola" + "mundo") # concatenado
print("hola" + str(5)) # convierte el 5 en string y luego se concatena con hola
print("hola "*5) # repite el string 5 veces. Tiene qye ser entero el valor numerico

my_val= 5.0

print ("HOLA "*int(my_val)) # el int() convierte el valor en entero

print("Comparacion de enteros")
print (3 > 4)
print (3 < 4)
print (3 >= 4)
print (3 <= 4)
print (3 == 4)
print (3 != 4)

#FUENTE FIRACODE PARA MEJOR VISUALIZACION DE SIMBOLOGIA
print("Comparacion de strings")
#Comprueba la ordenación alfabetica por ASCII, no el len de los str
print ("Hola" > "Python")
print ("Hola" < "Python")
print ("Hola" >="Python")
print ("Hola" <="Python")
print ("Hola" =="Python")
print ("Hola" !="Python")

print("aaa" >= "aba") # false
print("aba" >= "aaa") # true
print("aaa" >= "AAA") # true porque toma el valor de caracter en lugar de un numerico


# Operadores logicos

print(3 > 4 and "Hola" > "Python") 
print(3 > 4 or "Hola" > "Python") 
print(3 < 4 and "Hola" > "Python") 
print(3 < 4 or "Hola" > "Python") 
print(3 < 4 and "Hola" > "Python" and 4==4) 
print(3 > 4)
print(not(3 > 4))

