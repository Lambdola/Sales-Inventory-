KEY = True
MAIN_LIST = []
TOTAL_AMOUNT = []
MINI_SEPARATION = "*" * 24
SEPARATION = MINI_SEPARATION * 3
CONFIRMATION = "\n    Do you want to add more items: "

def Style(n):
    print(SEPARATION )
    print( f"●●● {n} ●●●".center(63, " "))
    print(SEPARATION )    
Style("OLA VENTURES")

i = 0
items_prices = {}
while KEY:
   
    i += 1
    item = input(f"Enter item #{i} name: ").capitalize()
    price = input(f"Enter item #{i} price: ")
    price = float(price.replace(" ",""))
    
    items_prices[item] = price
    MAIN_LIST.append(items_prices)
    TOTAL_AMOUNT.append(price)
    
    print(CONFIRMATION)
    
    option = " "
    while len(option) != 0:
        option = input("(yes/no): ").lower()
        if (option.startswith('y')):
            print("\n")
            break
        elif (option.startswith('n')):
            print("\nTotal Cart = ",MAIN_LIST)
            print("\nTotal_Amount = ", sum(TOTAL_AMOUNT))
            Style("THANKS FOR COMING")
            KEY = False
            break
