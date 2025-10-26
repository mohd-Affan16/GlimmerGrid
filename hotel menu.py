from datetime import datetime
food_item=[ {'id':'1.','name':'Biryani','price':150 },
               {'id':'2.','name':'Paneer Butter Masala','price':180},
               {'id':'3.','name':'Masala Dosa','price':80},
               {'id':'4.','name':'Chole Bhature','price':100},
               {'id':'5.','name':'Rogan Josh','price':250}]
order_list=[]
def menu():
    print('-'*40)
    print("Name:".ljust(34)+"Price")
    print('-'*40)
    for food in food_item:
        print(f"{food ['id']} {food ['name'].ljust(30)} ₹{food ['price']}")
    print('-'*40)
def get_order():
    while True:
         order_name=input('enter your order or type quit to complete your order:').strip()
         
         if order_name.lower() == 'quit':
            print('your order is successfully place')
            break
         food_found=False
         for food in food_item:
             if food['name'].lower() == order_name.lower() or food['id'].strip('.') == order_name:
                 food_found=True
                 quantity=int(input('Enter the quantity you want:'))
                 order_list.append({'name':order_name,'quantity':quantity})
                 print('what else do you want to order:')
                 break
         if not food_found:
                print('sorry we do not have that ')
    return 
def generating_bill():
    current_time=datetime.now()
    total_bill = 0
    print('='*80)
    print('The Azure Haven Hotel'.rjust(55))  
    print(current_time.strftime("Date: %d-%m-%Y at %I:%M %p"))
    print('='*80)
    print('Name'.ljust(25)+'quanatity'.ljust(20)+'price'.ljust(20)+'amount')
    print('-'*80)
    for order in order_list:
        for food in food_item:
               if food['name']==order['name']:
                 food_price=food['price']
                 total_price=food_price*order['quantity']
                 print(f"{order['name'].ljust(28)} {str(order['quantity']).ljust(15)} ₹{str(food_price).ljust(18)} ₹{total_price}")
                 total_bill += total_price
    print('-'*80)
    print(f"{'Amount'.ljust(64)} ₹{total_bill}")
    print('-'*80)

menu()
get_order()
generating_bill()
