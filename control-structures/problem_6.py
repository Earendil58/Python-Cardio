

# Make a program that calculates the minimum breakdown in bills and coins of an exact amount of euros.
# There are bills of 500, 200, 100, 50, 50, 20, 10 and 5; coins of 2 and 1 euro.

amount_of_money = int(input('Enter your amount of money, please: '))

bill_500 = 0
bill_200 = 0
bill_100 = 0
bill_50 = 0
bill_20 = 0
bill_10 = 0
bill_5 = 0
coin_2 = 0
coin_1 = 0


if amount_of_money >= 500:
    bill_500 = amount_of_money // 500
    amount_of_money = amount_of_money % 500
    
if amount_of_money >= 200:
    bill_200 = amount_of_money // 200
    amount_of_money = amount_of_money % 200

if amount_of_money >= 100:
    bill_100 = amount_of_money // 100
    amount_of_money = amount_of_money % 100

if amount_of_money >= 50:
    bill_50 = amount_of_money // 50
    amount_of_money = amount_of_money % 50
    
if amount_of_money >= 20:
    bill_20 = amount_of_money // 20
    amount_of_money = amount_of_money % 20
    
if amount_of_money >= 10:
    bill_10 = amount_of_money // 10
    amount_of_money = amount_of_money % 10
    
if amount_of_money >= 5:
    bill_5 = amount_of_money // 5
    amount_of_money = amount_of_money % 5

    
if amount_of_money >= 2:
    coin_2 = amount_of_money // 2
    amount_of_money = amount_of_money % 2

if amount_of_money >= 1:
    coin_1 = amount_of_money // 1
    
print(f'The amount of 500 bills is: {bill_500}')
print(f'The amount of 200 bills is: {bill_200}')
print(f'The amount of 100 bills is: {bill_100}')
print(f'The amount of 50 bills is: {bill_50}')
print(f'The amount of 20 bills is: {bill_20}')
print(f'The amount of 10 bills is: {bill_10}')
print(f'The amount of 5 bills is: {bill_5}')
print(f'The amount of 2 coins is: {coin_2}')
print(f'The amount of 1 coins is: {coin_1}')



