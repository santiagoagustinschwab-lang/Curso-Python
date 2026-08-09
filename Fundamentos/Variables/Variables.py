# Variables

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Con comas, print imprime todo
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)


# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea
name, surname, alias, edad = "Santiago", "Schwab", "Santi", 35
print("Me llamo:" ,name, "mi apellido es:" ,surname, "my alias es:" ,alias, "y tengo:" ,edad)

# Funcion input
"""""
first_name = input("Cual es tu nombre?")
age = input("Cuantos años tenes?")

print(first_name)
print(age)
"""

#Cambie el tipo
name = 35
age = "Santiago"
print(name)
print(age)

#Forze el tipo
address: str = "mi direccion"
print(type(address))