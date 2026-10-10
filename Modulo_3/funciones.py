#1. El calculador de envíos (Scope y globales)
#Declarar nuestra variable global (Accesible desde cualquier parte)

TARIFA_BASE = 50 #Variable Global

def calcular_envio(peso):
    costo = (peso * 10) + TARIFA_BASE
    print(TARIFA_BASE)
    return costo

precio_final = calcular_envio(10)
print(TARIFA_BASE)
print(f'El costo del envío es: {precio_final}')

#Intento de error
# print(costo)

#2. Generador de reportes

def generar_titulo(texto, simbolo):
    """Imprime un texto centrado y rodeado por un símbolo decorativo.

    :text str: El título o mensaje principal.
    :simbolo str: El carácter que se usará para decorar.
    """

    #Multiplica un string que repite el carácter.
    decoracion = simbolo * 10
    print(f'{decoracion} {texto} {decoracion}')

# #Llamada usando help() para ver nuestra documentación (docString)
help(generar_titulo)

generar_titulo("ANÁLISIS FINAL", "*")
generar_titulo("ADVERTENCIA", "!")

#3. Conversor de Moneda Flexible
#Uso de parámetros obligatorios y opcionales

#Tasa de cambio tiene un valor default de 18.41
def convertir_a_pesos(cantidad, tasa_cambio=18.41):
    total = cantidad * tasa_cambio
    return round(total, 2)

#Caso 1: Usando el valor por defector (Dólares)
print(f'100 USD son: {convertir_a_pesos(100)} MXN (Tasa Default)')

#Caso 2: Sobreescribiendo el valor por defecto (Euros)
pesos_euros = convertir_a_pesos(100, 20.63)
print(f'100 Euros son: {pesos_euros} MXN (Tasa específica)')