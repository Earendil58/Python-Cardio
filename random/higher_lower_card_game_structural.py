import random

#CONSTANTES DE LAS CARTAS
PALOS_CARTAS = ['Espadas', 'Corazones', 'Tréboles', 'Diamantes']
VALORES_CARTAS = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina', 'Rey']

CANT_CARTAS_AL_AZAR = 8

def obtener_carta(baraja):
    carta = baraja.pop()
    return carta

def mezclar(baraja):
    baraja_mezclada = baraja.copy()
    random.shuffle(baraja_mezclada)
    return baraja_mezclada


#CODIGO_PRINCIPAL
print('Bienvenido al juego "ALTO O BAJO"')
print('Vas a tener que elegir si la siguiente carta es más ALTA o BAJA que la carta mostrada')
print('Si acertás obtenes 20 puntos, si perdés se te restan 15 y si la carta es igual se muestra "INCORRECTO"')
print('Te damos 50 puntos al comienzo del juego')
print()

baraja_inicial = []

for palo in PALOS_CARTAS:
    for valor_numerico,  valor in enumerate(VALORES_CARTAS):
        carta = {'valor': valor, 'palo': palo, 'numero': valor_numerico + 1}
        baraja_inicial.append(carta)
        print(f'Esta es la carta del for in: {carta}')

puntaje = 50

while True: #Jugar multiples partidas
    print()
    baraja_juego = mezclar(baraja_inicial)
    carta_actual = obtener_carta(baraja_juego)
    valor_actual = carta_actual['valor']
    numero_actual = carta_actual['numero']
    palo_actual = carta_actual['palo']
    print(f'La carta inicial es: {valor_actual} de {palo_actual}')
    print()

    for numero_de_carta in range(0, CANT_CARTAS_AL_AZAR):
        respuesta = input(f'La próxima carta será más alta o más baja que el {valor_actual} de {palo_actual}? (escribe "a" para alta o "b" para baja): ')
        respuesta = respuesta.lower()
        siguiente_carta = obtener_carta(baraja_juego)
        valor_siguiente = siguiente_carta['valor']
        palo_siguiente = siguiente_carta['palo']
        numero_siguiente = siguiente_carta['numero']
        print(f'La siguiente carta es: {valor_siguiente} de {palo_siguiente}')

        if respuesta == 'a':
            if numero_siguiente > numero_actual:
                puntaje += 20
            else:
                puntaje -= 15
                print('Lo siento, no era más alta')

        elif respuesta == 'b':
            if numero_siguiente < numero_actual:
                puntaje += 20
            else:
                puntaje -=15
                print('Lo siento, no era más baja')

        print(f'Tu puntaje es: {puntaje}')
        print()
        valor_actual = valor_siguiente
        numero_actual = numero_siguiente
        palo_actual = palo_siguiente

    jugar_de_nuevo = input('Para jugar de nuevo, presiona ENTER, o escribe "q" para salir: ')
    if jugar_de_nuevo == 'q':
        break

print('Adios, gracias por jugar')




