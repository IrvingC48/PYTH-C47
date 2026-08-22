# #Variable integer (enteros)
# chocolate_caliente = 50

# #Variable float (decimal)
# PI = 3.141516

# #Variable boolean
# is_active = True

# #Variable string/char (texto)
# saludo = 'Hola, Mundo!'

# #f-string
# print(f'Variables simples: {chocolate_caliente}, {PI}, {is_active}, {saludo}')

# #------
# #Variable list
# #[index0, index1, index2, ...]
# fruits = ['apple', 50, 'cherry', [1,2,3], True]
# #fruits[0] -- 'apple'

# #Variable Tuple
# #(value1, value2, ...)
# coordinates = (10.0, 20.0)
# #coordinates[0] --10.0

# #Variable Dictionary
# #{key : value}
# person = {
#     'name' : 'Juan',
#     'age' : 30,
#     'city' : 'Madrid',
#     'hobbies' : ['football', 'read', 'trips'],
#     'is_active' : True
# }

# print(f'Variables complejas: {fruits}, {coordinates}, {person}')

#---------------

#Ejemplo de conversión de tipos
numero_str = "100"

#a + b a y b deben ser del mismo tipo (decimal, enteros)
#No podemos sumar/concatenar un string con un entero directamente
print(f'{numero_str}50') #Output "10050"

numero_int = int(numero_str) + 50 #Conversión de string a entero y sumar 50
print(numero_int)

fruits_str = ["10", "20", "30"]
print(fruits_str) #Output ['10','20','30']
# fruits_int = list(map(int,fruits_str))
# print(fruits_int)

flotante = 25.657
entero = int(flotante) #Conversión de float a entero
print(entero) #Output 25
print(round(flotante,0)) #Output 26

flotante_nuevo = float(numero_str) #Conversión de entero a float
print(flotante_nuevo) #Output 100.0
print(entero + flotante_nuevo) #Output 125.0

#Ejemplo de conversión a boleano
is_boolean = True
is_boolean_str = str(is_boolean) #Convertir boolean a str
print(is_boolean_str) #Output "True"
is_boolean_int = int(is_boolean)
print(is_boolean_int) #Output 1
is_boolean_float = float(is_boolean)
print(is_boolean_float) #Output 1.0
boolean_float = bool(is_boolean_float)
print(boolean_float) #Output True

fruta = 'platano'
fruta_int = int(fruta) #ValueError: invalid literal for int() with base 10: 'platano'
# fruta_int = int(float(fruta)) #ValueError: could not convert string to float: 'platano'
print(fruta_int)

#--------------------------------------------------------------------