"""
Very small flight travel planner
"""

# List of available cities
valid_cities = ["Johannesburg", "Cape Town", "Durban"]

# Assign values to the cities using dictionary
# This makes it adaptable in a real world scenario (easily changable if new cities are added or rates change)
city_hotel_price = { # Each city will have different rates
    "Johannesburg" : 50,
    "Cape Town" : 60,
    "Durban" : 70}

city_flight_rate = {
    "Johannesburg" : 1000,
    "Cape Town" : 1200,
    "Durban" : 1400}

car_rent_rate = 10

print("Welcome to Starter Travel Agency!\nWe currently offer flights to:", ", ".join(valid_cities)) # Show user available flgihts

while True: # Take into account when user enters invalid city
    city_flight = input("Please select your destination city from the above list:\n")
    if city_flight in valid_cities:
        print("\nYou have booked a flight to", city_flight + ".\n")
        break
    else:
        print("We unfortunately do not offer flights to that city. Please choose from the following:\n", ", ".join(valid_cities))


# num_night: Num of nights at the hotel
# Prevent invalid values from being entered
num_night = input("Please enter how many nights you will be staying at the hotel:\n")
while True:
    try:
        num_night = float(num_night)
        if num_night > 0 and num_night.is_integer():
            num_night = int(num_night)
            print(f"\nYou have booked {num_night} night(s) at the hotel.\n")
            break
        else:
            print("Please enter a valid integer.")
            num_night = input("Please enter how many nights you will be staying at the hotel:\n")
    except ValueError:
        print("Please enter a valid integer.")
        num_night = input("Please enter how many nights you will be staying at the hotel:\n")

# rental_days: Num of days they will be hiring the car
rental_days = input("Please enter how many days you will be hiring the car:\n")
while True:
    try:
        rental_days = float(rental_days)
        if rental_days > 0 and rental_days.is_integer():
            rental_days = int(rental_days)
            print(f"\nYou have booked to use the rental car for {rental_days} day(s).\n")
            break
        else:
            print("Please enter a valid integer.")
            rental_days = input("Please enter how many days you will be hiring the car:\n")
    except ValueError:
        print("Please enter a valid integer.")
        rental_days = input("Please enter how many days you will be hiring the car:\n")


# Next, create functions for:
    # hotel_cost: Function will take the num_nights as argument and return cost for the hotel stay 
def hotel_cost(city_flight, num_nights):
    hotel_price = city_hotel_price[city_flight]
    total_hotel_cost = num_nights * hotel_price
    return total_hotel_cost

# store the function for easier readability
total_hotel_cost = hotel_cost(city_flight, num_night)

# plane_cost: Will take city_flight as argument and return cost for the flight 
def plane_cost(city_flight):
    plane_price = city_flight_rate[city_flight]
    total_plane_cost = plane_price
    return total_plane_cost

# store the function for easier readability
total_plane_cost = plane_cost(city_flight)

# car_rental: Take rental_days as argument and return total cost of car rental
def car_rental(rental_days):
    total_rental_cost = rental_days * car_rent_rate
    return total_rental_cost

# store the function for easier readability
total_rental_cost = car_rental(rental_days)

# holiday_cost: Take the three arguments. Call all three and return total cost for your holiday
def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_holiday_cost = hotel_cost + plane_cost + car_rental
    return total_holiday_cost

# store the function for easier readability
total_holiday_cost = holiday_cost(total_hotel_cost, total_plane_cost, total_rental_cost)

# Print out details in a readable way
print("\nYour total holiday cost breakdown:")
print("Total hotel cost:", total_hotel_cost)
print("Plane cost:", total_plane_cost)
print("Total rental cost:", total_rental_cost)
print("Total holiday cost:", total_holiday_cost)

