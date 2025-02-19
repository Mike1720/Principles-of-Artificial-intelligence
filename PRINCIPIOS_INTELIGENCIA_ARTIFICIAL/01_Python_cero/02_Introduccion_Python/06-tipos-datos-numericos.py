import random

x = 1  # int
y = 3.14  # float
z = 1j  # complex

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

# Casteo int -> float
flotante = float(x)
print(flotante)  # output: 1.0
print(type(flotante))  # output: <class 'float'>

# Casteo float -> int
entero = int(y)
print(entero)  # output: 3
print(type(entero))  # output: <class 'int'>


# ----------------------------
# Números aleatorios
# ----------------------------

# randrange -> Genera un número aleatorio entre un rango sin incluir el último número
aleatorio = random.randrange(1, 10) 
print(aleatorio)

# random() -> Genera un número aleatorio entre 0 y 1
aleatorio_0_1 = random.random()
print(aleatorio_0_1)

# randint -> Genera un número aleatorio entre un rango incluyendo el último número
aleatorio_2 = random.randint(1, 10)
print(aleatorio_2)