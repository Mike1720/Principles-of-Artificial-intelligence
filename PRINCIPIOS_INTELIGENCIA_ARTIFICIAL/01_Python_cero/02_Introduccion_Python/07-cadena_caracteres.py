# Strings o cadenas de caracteres
string_comillas_simples = "Hola, soy una cadena con comillas simples"
string_comillas_dobles = "Hola soy una cadena con comillas dobles"
string_triple_comillas_simples = """Este texto es 
multilinea"""
string_triple_comillas_dobles = """Este texto tambien 
es multilinea"""

# ----------------------------------------

#      0123456789012345678901234567890
txt = "Seguimos trabajando con strings"

# ----------------------------------------
# Slicing: Extraer una parte de la cadena de caracteres
# ----------------------------------------

# Sintaxis: str[start:end] sin incluir el end
print(txt[0:8])  # output: Seguimos
print(txt[:8])  # output: Seguimos
print(txt[9:19])  # output: trabajando
print(txt[24:])  # output: strings
print(txt[-11:])  # output: con strings
print(txt[-11:-1])  # output: con string

# ----------------------------------------
# Lower, Upper, Capitalize, Title, Center, Count, Endswith, Startswith, Find
# ----------------------------------------

# Sintaxis: str.lower(), str.upper(), str.capitalize(), str.title(), str.center(width), str.count(substring), str.endswith(substring), str.startswith(substring), str.find(substring)
txt_Mayus = "CUANDO ESCRIBO EN MAYUSCULAS TODO EL MUNDO PIENSA QUE ESTOY GRITANDO"
txt_Minus = "cuando escribo en minusculas todo el mundo piensa que estoy susurrando"
txt_to_Capitalize = "texto en minusculas"
txt_Title = "titulo del texto"
txt_Center = "texto centrado" # Sintaxis: str.center(width)
txt_Count = "cuantas veces aparece la letra a en esta cadena"
txt_Endswith = "Esta cadena termina con una palabra"
txt_Find = "En que posicion se encuentra la palabra posicion en esta cadena"

print(txt_Mayus.lower())
print(txt_Minus.upper())
print(txt_to_Capitalize.capitalize())
print(txt_Title.title())
print(txt_Center.center(50))
print(txt_Count.count("a"))
print(txt_Endswith.endswith("palabra"))
print(txt_Find.find("posicion"))


# ----------------------------------------
# Spaces
# ----------------------------------------

# Sintaxis: str.strip()
txt4 = "    texto con espacios al inicio y al final    "
print(txt4)
print(txt4.strip())

# ----------------------------------------
# Concatenacion
# ----------------------------------------

# Sintaxis: str1 + str2
txt5 = "Hola"
txt6 = "mundo"
txt7 = txt5 + " " + txt6
print(txt7)

newText0 = "El contenido de este curso es de: "
hours = 10

# concatenacion_incorrecta = text + horas
# print(concatenacion_incorrecta) # Error

concatenacion_correcta = newText0 + str(hours) + " horas"
print(concatenacion_correcta)

newHours = 30
numberClasses = 10
newText = "El contenido de este curso es de: {} horas"
newText2 = "El contenido de este curso es de: {} horas y tendrá {} clases"
newText3 = "El contenido de este curso es de: {1} horas y tendrá {0} clases"

print(newText.format(newHours))  # Output: El contenido de este curso es de: 30 horas
print(
    newText2.format(newHours, numberClasses)
)  # Output: El contenido de este curso es de: 30 horas y tendrá 10 clases
print(
    newText3.format(numberClasses, newHours)
)  # Output: El contenido de este curso es de: 30 horas y tendrá 10 clases
print(
    newText3.format(newHours, newHours)
)  # Output: El contenido de este curso es de: 30 horas y tendrá 30 clases

# ----------------------------------------
# Character scape
# ----------------------------------------

# Sintaxis: \n, \t, \b, \r, \f, \', \", \\

string_comillas = 'La mejor serie de la historia es "Game of Thrones"'
string_comillas2 = "La mejor serie de la historia es 'Game of Thrones'"
str_scape1 = 'La mejor serie de la historia es "Game of Thrones"'  # Output: La mejor serie de la historia es "Game of Thrones"
str_scape2 = "La carpeta se encuentra en C:\\Users\\User\\Documents"  # Output: La carpeta se encuentra en C:\Users\User\Documents
str_scape3 = "Texto con salto de linea \n y tabulacion \t"
str_scape4 = "Texto con \bbackspace"

print(string_comillas)
print(string_comillas2)
print(str_scape1)
print(str_scape2)
print(str_scape3)
print(str_scape4)
