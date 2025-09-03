# Registro de Temperaturas Diarias con Matriz 3D
# Autor: Naydelin Jiménez Layedra 

# Lista de ciudades
ciudades = ["Ciudad A", "Ciudad B"]

# Número de semanas y días
num_semanas = 2
num_dias = 7

# Matriz 3D con temperaturas de ejemplo
# Estructura: temperaturas[ciudad][semana][dia]
temperaturas = [
    [   # Ciudad A
        [25, 26, 27, 28, 29, 30, 31],  # Semana 1
        [24, 25, 26, 28, 27, 29, 30]   # Semana 2
    ],
    [   # Ciudad B
        [18, 19, 20, 21, 22, 23, 24],  # Semana 1
        [20, 21, 19, 22, 23, 21, 20]   # Semana 2
    ]
]

# Calcular y mostrar los promedios
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedios de temperaturas para {ciudad}:")
    for semana in range(num_semanas):
        suma = 0
        for dia in range(num_dias):
            suma += temperaturas[i][semana][dia]
        promedio = suma / num_dias
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")