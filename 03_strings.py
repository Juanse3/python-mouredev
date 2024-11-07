### Strings ###

#posibilidad de definiciones de strings
my_string1= "Hola"
my_string2='Holas'


print(my_string1)
print(my_string2)

#len da el largo de la cadena
print(len(my_string1))
print(len(my_string2))

#impresion con string dentro del print
print(my_string1 + " | " + my_string2)

# \n para nueva linea
# \t tabulacion
# escapado de caracteres especiales
my_new_string = "\tString con\nsalto de linea y \\nescapado de caracteres"
print(my_new_string)


# Formateo de strings

name, surname, age = "Juan", 'Muñoz', 42


# distintos tiposd e concatenacion de strings y datos
print("Format: mi nombre es {} y mi apellido {}, tengo {} años".format(name,surname,age))
print("porciento: mi nombre es %s y mi apellido %s, tengo %d años" %(name,surname,age))
print("+: mi nombre es " + name + " y mi apellido " + surname + " tengo " + str(age) + " años")

# desempaquetado de carcteres

lenguaje = "PyThoN"

a,b,c,d,e,f = lenguaje

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


