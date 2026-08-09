# Strings
mi_string = "mi string"
mi_otro_string = "mi otro string"

print(len(mi_string))
print(len(mi_otro_string))

print(mi_string + " " + mi_otro_string)

# salto de linea
mi_nuevo_string_linea = "este es un string  \ncon salto de linea"
print(mi_nuevo_string_linea)

# tabulacion
mi_nuevo_string_tabulado = "\teste es un string tabulado"
print(mi_nuevo_string_tabulado)

# Se pueden convinar
mi_string_convinado = "\teste es un string \ncomvinado"
print(mi_string_convinado)

# Se puede cancelar poniendo otra \ al principio, ej \\n \\t

# Formateo

name, apellido, edad = "santiago", "schwab", 17
# primer metodo format
print("mi nombre es {} {} y mi edad es {}".format(name, apellido, edad))
#segundo metodo %, %s para str, %d para int
print("mi nombre es %s %s y mi edad es %d" %(name, apellido, edad))

# Inferencia de datos, mejor
print(f"mi nomnbre es {name} {apellido} y mi edad es {edad}")

# Desempaquetado de caracteres
languaje = "python"
a, b, c, d, e, f = languaje
print(a)
print(b)

# Division
# agarra caracter 1 y 3
languaje_slice = languaje[1:3]
print("1",languaje_slice)

#elimina los primeros 2 caractreres
languaje_slice = languaje[2:]
print("2",languaje_slice)

#agarra los primero 2 caracteres
languaje_slice = languaje[:2]
print("3", languaje_slice)

#agarra en anteultiomo caracter
languaje_slice = languaje[-2]
print("4", languaje_slice)

# agara el carater n0, 6 y 2
languaje_slice = languaje[0:6:2]
print("5", languaje_slice)

# Reversa
reverse_lenguaje = languaje[::-1]
print(reverse_lenguaje)

# Funciones
# Capitalize, mayuscula el la primera letra
print(languaje.capitalize())
# Upper, todo mayusucla
print(languaje.upper())
# count, cuenta cuantos caracteres x hay
print(languaje.count("t"))
# isnumeric, dice si es un numero o no
print(languaje.isnumeric())
# sirve para str tmb, si hay numero es true
print("1".isnumeric())
# Lower, todo minuscula
print(languaje.lower())
# Se pueden conbinar, primero convierte python en mayuscula y luego lo comprueba, es verdadero
print(languaje.upper().isupper())
# Startswith, comprueba si la variable x epieza con "y"
print(languaje.startswith("py"))