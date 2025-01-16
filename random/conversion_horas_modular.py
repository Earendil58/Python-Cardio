segundos_totales_a_convertir = 8421

segundos_en_una_hora = 3600

cant_horas_totales = segundos_totales_a_convertir//segundos_en_una_hora

print(f'Cantidad de horas: {cant_horas_totales}')

segundos_a_minutos = (segundos_totales_a_convertir%segundos_en_una_hora) // 60

print(f'Cantidad de minutos: {segundos_a_minutos}')

segundos_sobrantes_de_minutos = (segundos_totales_a_convertir%segundos_en_una_hora) % (segundos_a_minutos * 60)

print(f'Segundos sobrantes: {segundos_sobrantes_de_minutos}')
