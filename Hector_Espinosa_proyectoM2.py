print("=======1. Longitud de una frase =======")
# Declarar variable para validar la palabra ingresada
invalida = True

while True:
    # Pedir la palabra al usuario
    palabra = input('Introduce una palabra de 4 a 8 letras: ')
    # Validar si la palabra tiene mínimo 4 letras, de lo contrario vuelve a pedir la palabra
    if len(palabra) < 4:
        print('Hacen falta letras. Solo tiene ' + str(len(palabra)) + ' letras')
    # Validar si la palabra tiene máximo 8 letras, de lo contrario vuelve a pedir la palabra
    elif len(palabra) > 8:
        print('Sobran letras. Tiene ' + str(len(palabra)) + ' letras')
    # Muestra el mensaje de que es correcta la palabra
    else:
        print(f'La palabra: {palabra} es correcta.')
        break

print("=======2. Encuentra el cuadrante =======")

# Definir diccionario con cuadrantes
cuadrantes = {
    '+,+':'Cuadrante I',
    '-,+':'Cuadrante II',
    '-,-':'Cuadrante III',
    '+,-':'Cuadrante IV'
}

# Pedir coordenadas al usuario
while True:
    eje_x = int(input('Introduce el valor del eje X: '))
    if eje_x == 0:
        print("El valor no puede ser igual a 0")
        continue
    else:
        break

while True:
    eje_y = int(input('Introduce el valor del eje Y: '))
    if eje_y == 0:
        print("El valor no puede ser igual a 0")
        continue
    else:
        break

# Definir variable para armar la llave en la que se buscará el cuadrante en el diccionario
coordenada = ''

# Armar llave del cuadrante del eje X
if eje_x < 0:
    coordenada += '-,'
else:
    coordenada += '+,'
# Agregar el valor del eje Y a la llave del cuadrante
if eje_y < 0:
    coordenada += '-'
else:
    coordenada += '+'

# Imprimir el resultado del cuadrante donde se encuentra la coordenada ingresada
print("El punto se encuentra en el " + cuadrantes.get(coordenada))