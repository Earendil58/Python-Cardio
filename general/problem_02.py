# You want to know the price of a medium distance bus ticket. 
# In order to calculate it, you must consider the base amount (which is always charged), 
# plus an extra value calculated on the basis of the number of kilometers to be traveled: 
# For each kilometer to be traveled, an additional $0.30 is charged.

base_amount = float(input('Enter the base amount of the bus ride: '))
number_of_km = float(input('Enter the amount of Km to travel: '))

EXTRA_VALUE = 0.30

total_price = base_amount + (number_of_km * EXTRA_VALUE)

print(f'The total price you have to pay is: ${total_price}')

