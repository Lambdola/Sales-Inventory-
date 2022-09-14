n = 0
main_list = []
total_amount = []
print ("       *** OLA VENTURES *** ")
print(">>>All prices are in naira (NGN)<<<\n")


def store_value():

    global n
    n += 1
    print("******************\n")
    
    item = input('Enter item #' + str(n) + ' name: ')
    check1_price= input('Enter item #' + str(n) +  ' price:')
    price = float(check1_price.replace(" ",""))
    
    
    items_prices = {}
    items_prices[item] = price
    main_list.append(items_prices)
    total_amount.append(price)
    
    print("\n    Do you want to add more items: ")
    
    option = ""

    while (option != 'Yes' or option != 'yes') or (option != 'No' or option != 'no'):
        print("     Input either Yes or No: ")
        check1_option = input( )
        option = check1_option.replace(" ","")
        if (option == 'Yes' or option == 'yes'):
            return store_value()
        elif (option == 'No' or option == 'no'):
            print("\n")
            break
       
    for i in range(1):
        for j in range(5):
            j += 1
            print("*"*j)
            if j == 5:
                for x in range(4,0,-1):
                    print("*"*x)
                
            
    print("\ntotal_cart = ",main_list)
    print("\ntotal_amount_to_pay = ",sum(total_amount))
   

store_value()
