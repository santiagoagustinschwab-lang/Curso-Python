#1
nombre, apellido = "santiago", "schwab"
print(len(nombre), len(apellido))

#2
print(nombre ,""+ apellido)

#3
ciudad = "mg"
print(f"{nombre} \n{ciudad}")

#4
name, surname, age = "santiago", "schwab", 17
print("mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"mi nombre es {name} {surname} y mi edad es {age}")

#5
programacion = "programacion"
print(programacion[:4])

#6
print(programacion[5:])

#7
print(programacion[::-1])

#8
print(f"{name}".upper(), f"{name}".lower())

#9
print(f"{name} {surname}".count(name[0]))

#10
print(f"{name}".startswith("s"))