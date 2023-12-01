# Develop a program that, knowing the departure and arrival times of a flight (hour and minutes), determines its duration in minutes. 
# If the traveler then needs 45 minutes more to get from the airport to the hotel he has booked, what time will he arrive at the hotel?


departure = input('Enter the departure time hh/mm: ')
arrival = input('Enter the arrival time hh/mm: ')

TAXI_TIME = 45

minutes_departure_time = (departure[3])+(departure[4])
minutes_departure_time_integer = int(minutes_departure_time)

hours_departure_time = departure[0] + departure[1]
hours_departure_time_integer = int(hours_departure_time)

total_minutes_departure = minutes_departure_time_integer + (hours_departure_time_integer * 60)

minutes_arrival_time = (arrival[3])+(departure[4])
minutes_arrival_time_integer = int(minutes_arrival_time) 

hours_arrival_time = arrival[0] + arrival [1]
hours_arrival_time_integer = int(hours_arrival_time)

total_minutes_arrival = minutes_arrival_time_integer + (hours_arrival_time_integer * 60)


total_time_traveled_minutes = total_minutes_arrival - total_minutes_departure

hotel_arrival_hours = (total_time_traveled_minutes + TAXI_TIME) // 60
hotel_arrival_minutes = (total_time_traveled_minutes + TAXI_TIME) % 60





print(f'The hour of arrival to the hotel is : {hotel_arrival_hours}, minutes: {hotel_arrival_minutes}')


