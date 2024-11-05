#variables

#se usa snake case

my_variable = "variable str"
print(my_variable)

my_int_var = 9
print(my_int_var)

my_int_to_str_var = str(my_int_var)
print("my_int_var:", my_int_var)
print("my_int_var type:", type(my_int_var))

print("my_int_to_str_var:", my_int_to_str_var)
print("my_int_to_str_var type:", type(my_int_to_str_var))



my_float_var = 1.6
print(my_float_var)


print(my_variable,":",my_float_var) #print con multiples inputs

print(len(my_variable)) # len entrega el largo de una cadena

#varibles en una sola linea

name, surname, age, work = "Juan", "Muñoz", 42, True
print(surname,",",name, "| Edad:",age,"| Has Work:", work)  #agrega espacios despues de cada variable

#ingreso de datos por el usuario

name = input("Nombre?")
age = input("Edad?")

print( name, "tiene", age,"años de edad.")

#cambio de tipo de dato
name = 43
age = False

print(name)
print(age)


#explicitamos tipo de dato que se quiere en la variable, pero igual puede cambiar su tipo

apellido:str="Lopez"
print(apellido)
apellido=True
print(apellido)

