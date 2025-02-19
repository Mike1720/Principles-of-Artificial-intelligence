# CASTEO
# Casteo es la conversión de un tipo de dato a otro.

# Texto (string)
text1 = "Texto"
text2 = "123"
text3 = "Texto123"

# Números (int, float, complex)
num1 = 123
num2 = 123.456
num3 = 1j

# list
list1 = ["manzana", "banana", "cereza"]

# tuple
tuple1 = ("manzana", "banana", "cereza")

# *Casteo str -> num
casteo_Str_Num1 = int(text2)
print(casteo_Str_Num1)
print(type(casteo_Str_Num1))

# *Casteo num -> str
casteo_Num_Str1 = str(num1)
print(casteo_Num_Str1)
print(type(casteo_Num_Str1))

# *Casteo list -> tuple
casteo_List_Tuple1 = list(tuple1)
print(casteo_List_Tuple1)
print(type(casteo_List_Tuple1))

# *Casteo tuple -> list
casteo_Tuple_List1 = tuple(list1)
print(casteo_Tuple_List1)
print(type(casteo_Tuple_List1))