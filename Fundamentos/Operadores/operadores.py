# Operadores Aritmeticos

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)

# Resto, no porcentaje
print(10 % 3)

# Division aproximada, siempre da entero
print(10 // 3)

# Potencia, x elevado a..
print(2 ** 3)

# Concatena
print("Hola" + "Python")

#print("hola" + 5), no se puede porque 5 es un int
print("hola" + str(5)) #si se puede porque se transforma el 5 en un string

# Se puede multiplicar los str
print("hola " * 5)
print("hola " * (2 ** 3))
# Como son textos, no se puede multiplicar por Floats
#print("hola" * 2.5)

numero_con_coma = 2.5 * 2 # = 5, pero 5.0, es un float
print("hola " * int(numero_con_coma)) # transforme el float por un int, de 5.0 a 5

# Operadores Comparativos #

# Van a imprimir booleanos
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)

# Igualdad
print(3 == 4)
# Desigualdad
print(3 != 4)

# Se pueden comvinar
print(3 > 4 > 5)

# Tambien se puede con Strings
print("hola" > "python") # Cuenta caracteres

# En este caso, tiene en cuenta las letras en orden alfabetico
print("Hola" >= "zola")
# En este, cuenta solo caracteres
print(len("aaaa") > len("abaa"))


# Operadores Logicos #

"""""
Logica booleana
False + False = False
False + True = False
False o False = False
"""""
# operador Y
print( 3 > 4 and "hola" > "python" )
print( 4 > 3 and "python" > "hola")

# operador O, con que una de las 2 condiciones se cumpla o sea incorrecta, alcanza
print(3 > 4 or "hola" > "python")
print(3 < 4 or "hola" < "python")

# Se pueden concatenar
print(3 < 4 or "hola" > "a" and 4 == 4)

# operador NO, niega lo que sigue, 4 > 5 es falso, pero not 4 > 5 es verdadero
print(not(3 > 4)) 