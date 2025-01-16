# Solicitar datos de entrada
hora_partida = int(input("Ingrese la hora de partida (0-23): "))
minutos_partida = int(input("Ingrese los minutos de partida (0-59): "))
hora_llegada = int(input("Ingrese la hora de llegada (0-23): "))
minutos_llegada = int(input("Ingrese los minutos de llegada (0-59): "))

# Convertir la hora de partida y llegada a minutos desde la medianoche
minutos_totales_partida = hora_partida * 60 + minutos_partida
minutos_totales_llegada = hora_llegada * 60 + minutos_llegada

# Calcular la duración del vuelo
if minutos_totales_llegada < minutos_totales_partida:
    # Si la llegada ocurre al día siguiente
    minutos_totales_llegada += 24 * 60  # Sumar 24 horas en minutos

duracion_vuelo = minutos_totales_llegada - minutos_totales_partida

# Calcular el tiempo total hasta llegar al hotel
minutos_totales_hotel = minutos_totales_llegada + 45

# Calcular la hora y minutos de llegada al hotel
hora_hotel = (minutos_totales_hotel // 60) % 24  # División entera y módulo para mantener formato de 24 horas
minutos_hotel = minutos_totales_hotel % 60

# Mostrar resultados
print(f"La duración del vuelo es de {duracion_vuelo} minutos.")
print(f"El viajero llegará al hotel a las {hora_hotel:02d}:{minutos_hotel:02d}.")
