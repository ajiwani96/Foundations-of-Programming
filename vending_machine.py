import math as m
Toonies = 5
Loonies = 5
Quarters = 20
Dimes = 30
Nickels = 40
def display_welcome_menu():
 print("Welcome to the COMP 202 Vending Machine.\n Here are your options: \n 1. Candy bar $2.95 \n 2. Cookies $3.90 \n 3. Soda $4.00 \n 4. Chips $3.90 \n 5. No snacks for me today!")
 
def get_snack_price(which_snack):
    if (which_snack == 1):
        return("295")
    elif (which_snack == 2):
        return("390")
    elif (which_snack == 3):
        return("400")
    elif (which_snack == 4):
        return("390")
    else:
        return("0")

def get_num_of_coins(money_needed, coin_value, number_in_machine):
    x = money_needed/coin_value 
    y = x - number_in_machine
    if (y <= 0):
        rounded_number_of_coins = m.floor(x) #cant have a fraction of a coin so we must round down for the maximum number of whole coins
        return(rounded_number_of_coins)
    else:
        return(number_in_machine)

def compute_and_display_change(change):
    num_toonies = change//200 ##maximum number of toonies that can "fit" inside the change
    num_loonies = (change%200)//100 ##given that the maximum number of toonies has been taken out of the change, we divide the remaining amount of change by the next biggest coin value, loonies, to get the maximum amount of loonies. we repat this process until no money is left.
    num_quarters = ((change%200)%100)//25
    num_dimes = (((change%200)%100)%25)//10
    num_nickels = ((((change%200)%100)%25)%10)//5
    if ((num_toonies <= 5) and (num_loonies <= 5) and (num_quarters <= 20) and (num_dimes <= 30) and (num_nickels <= 40)):
       print("Here is your change: \n Toonies x", num_toonies, "\n Loonies x", num_loonies, "\n Quarters x", num_quarters, "\n Dimes x", num_dimes, "\n Nickels x", num_nickels)
       return(True)
    else:
        return(False)


def operate_machine():
    display_welcome_menu()
    which_snack = int(input(""))
    get_snack_price(which_snack)
    if (get_snack_price(which_snack) == "0"):
        print("Goodbye!")
    else:
        print(get_snack_price(which_snack))
        cash = float(input(""))
        rounded_cash = round(cash, 2)
        cash_in_cents = int(rounded_cash*100)
        print(cash_in_cents)
        if (cash_in_cents % 5 != 0): #if the remainder of cash in cents when didvided by 5 is not zero, then the number is not a multiple of 5 and cannot be fully made up of toonies, loonies, quarters, dimes and cents.
            print("The machine does not accept pennies")
        else:
            if(((which_snack == 1) and cash_in_cents < 290) or ((which_snack == 2) and cash_in_cents < 390) or ((which_snack == 3) and cash_in_cents < 400) or ((which_snack == 4) and cash_in_cents < 390)):
                print("insufficent funds") #testing to see if the amount of money given to the machine is greater than or equal to the cost of the chosen item 
            else:
                snack_price = get_snack_price(which_snack)
                change = cash_in_cents - int(snack_price) #calculating the amount of change needed
                print(change)
            
            if (compute_and_display_change(change) == True): #testing to see if the machine has enough coins to give to the
                return( None )
            else:
                print("The machine does not have enough coins")
             
            
                
            
            
        
            
    
    
                      



        