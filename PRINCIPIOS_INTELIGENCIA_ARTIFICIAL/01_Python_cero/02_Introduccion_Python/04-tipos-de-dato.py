# TIPOS DE DATOS EN PYTHON

#---------------------------------------------------
# Texto
#---------------------------------------------------

# str -> string -> cadena de texto
texto = "cadena de caracteres"

#---------------------------------------------------
# Números
#---------------------------------------------------

# int -> integer -> número entero
numero_entero = 10

# float -> número decimal
numero_decimal = 10.5

# complex -> número complejo
numero_complejo = 10 + 5j

#---------------------------------------------------
# Secuencias
#---------------------------------------------------

# list -> lista -> colección ordenada y modificable
lista = [1, 2, 3, 4, 5]

# tuple -> tupla -> colección ordenada e inmodificable
tupla = (1, 2, 3, 4, 5)

# range -> rango -> secuencia de números inmodificable
rango = range(5)

#---------------------------------------------------
# Mapeo o diccionarios
#---------------------------------------------------

# dict -> diccionario -> colección no ordenada de pares clave-valor
diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Ciudad de México"
}

#---------------------------------------------------
# Conjuntos o sets
#---------------------------------------------------

# set -> conjunto -> colección no ordenada, mutable y sin elementos duplicados
conjunto = {1, 2, 3, 4, 5}

# frozenset -> conjunto inmutable
conjunto_inmutable = frozenset({1, 2, 3, 4, 5})

#---------------------------------------------------
# Booleanos
#---------------------------------------------------

# bool -> booleano -> True o False
booleano = True
booleano2 = False

#---------------------------------------------------
# Binarios
#---------------------------------------------------

# bytes -> secuencia de bytes inmutable
bytes = b"cadena de bytes"

# bytearray -> secuencia de bytes mutable
bytearray = bytearray(5)

# memoryview -> secuencia de bytes que permite acceder a la memoria
memoryview = memoryview(bytes)