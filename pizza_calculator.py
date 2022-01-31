import math as m

def display_welcome_menu():
    print("Welcome to the COMP 202 fair pizza calculator! \n Please choose one of the following modes: \n A. \"Quantity Mode\" \n B. \"Price Mode\" ")
    
def get_fair_quantity(diameter_1, diameter_2):
    area_of_pizza_1 = m.pi*((diameter_1 / 2) ** 2)
    area_of_pizza_2 = m.pi*((diameter_2 / 2) ** 2)
    if(area_of_pizza_1 < area_of_pizza_2): #case 1, pizza 1 is smaller than pizza 2
        if((area_of_pizza_2 % area_of_pizza_1) == 0): #if there is no remainder when the area of pizza 2 is divided by pizza 1 then the two areas are multiples of each other and so fair number of pizzas is exactly pizza 2/pizza 1
            return( int(area_of_pizza_2//area_of_pizza_1))
        else: #as they are not exact multiples, you have to add an extra pizza as you cannot have a fgraction of a pizza
            return(int((area_of_pizza_2//area_of_pizza_1) +1))
    else: #case 2, pizza 1 is bigger than pizza 2
        if((area_of_pizza_1 % area_of_pizza_2) == 0):
            return( int(area_of_pizza_1//area_of_pizza_2))
        else:
            return(int((area_of_pizza_1//area_of_pizza_2) +1))
        

def get_fair_price(diameter_large, price_large, diameter_small, num_small):
    area_large = m.pi*((diameter_large / 2) ** 2)
    area_small = m.pi*((diameter_small / 2) ** 2)
    pizza_per_dollar = price_large / area_large
    total_fair_price = pizza_per_dollar * area_small * num_small #the price of all the small pizzas if they were priced at the same rate as the large pizzas
    rounded_fair_price = round(total_fair_price, 2) #rounding to 2dp
    return(rounded_fair_price)
    
def run_pizza_calculator():
    display_welcome_menu()
    choice = input("")
    if(choice == "A"):
        diameter_1 = int(input(""))
        diameter_2 = int(input(""))
        print(get_fair_quantity(diameter_1, diameter_2)) #using the get_fair_quantity function
    elif(choice == "B"):
        diameter_large = int(input(""))
        price_large = float(input(""))
        diameter_small = int(input(""))
        num_small = int(input(""))
        print(get_fair_price(diameter_large, price_large, diameter_small, num_small)) #using the get_fair_price function
    else:
        print("This mode is not supported") #for all other inputs except "A" and "B" this message should be shown.
    
    
    
    