# VARIABLES EN PYTHON
'''
-Contenedores que almacenan datos que pueden cambiar durante la ejecución del programa
-Cada variable tiene un nombre único llamado identificador y un valor asociado
-Para asignar un valor a una variable se utiliza el operador de asignación "="
'''

x = 5
nombre = "Juan"
y = str(x)

print(x) # output: 5
print(nombre) # output: Juan
print(y) # output: 5
print(type(y)) # output: <class 'str'>

# Reglas para nombrar variables
# VALIDO: Si comienza con una letra y sin caracteres especiales
apellido = "Perez"

#VALIDO: Si comienza con una letra y con guiones bajos intermedios
nombre_completo = "Juan Perez"

#VALIDO: Si comienza con guiones bajos
_nombre = "Juan"

#VALIDO: Si usa camelCase (la primera letra de la primera palabra en minúscula y la primera letra de las palabras siguientes en mayúscula)
nombreCompleto = "Juan Perez"

#VALIDO: Todo en mayúsculas
NOMBRE = "Juan"

#VALIDO: Si comienza con una letra y con números
nombre1 = "Juan"

#INVALIDO: Si comienza con números
#1nombre = "Juan"

#INVALIDO: Si contiene caracteres especiales como @, #, $, %, espacios, etc.
#nombre@ = "Juan"
#nombre-1 = "Juan"
