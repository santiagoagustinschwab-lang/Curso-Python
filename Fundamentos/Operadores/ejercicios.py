#1
numero_1 = 1
numero_2 = 2

print(numero_1 + numero_2)
print(numero_1 - numero_2)
print(numero_1 * numero_2)
print(numero_1 / numero_2)

#2
numero = 10
print(numero % 2 == 0)

#3
veces = 50 // 7
resto = 50 % 7
print("el numero 7 entra aproximadamente", veces, "en 50, y su resto es", resto)

#4
lado = 2
area_de_un_cuadrado = lado ** 2
print("el area del cuadrado de lado 2 es ",area_de_un_cuadrado)

#5
print("santiago " + "schwab")

#6
print("python " * 17)

#7
edad_1 = 10
edad_2 = 20
print(edad_1 > edad_2)
print(edad_1 < edad_2)
print(edad_1 == edad_2)

#8
verdadero = True
falso = False

print(verdadero and falso)
print(verdadero or falso)
print(not(verdadero))

#9 
# no lo supe hacer

#10, este resultado se da porque al comparar dos str se toman en cuenta la cantidad de caracteres, en este caso, el mensaje aa tiene mas caracteres que el mensaje a, osea, la comparacion es verdadera
print("mensaje aa" > "mensaje ab")