from datetime import datetime,timedelta
id=input("Enter the id :").lower()

pres_rdg=int(input('Enter pres rdg :'))
prev_rdg=int(input('Enter prev rdg :'))
def time():
    current_time = datetime.now()
    print("-"*35)
    print(current_time.strftime("Reading Date:  %d-%m-%Y"))
    print(current_time.strftime("Issued Date:   %d-%m-%Y at %I:%M %p"))

def data_base():
    customer_list=[{ "uid":'586g291b7h',"name":"xyz","address":"xyz" },{"uid":"9eaigc31j4","name":"xyz","address":"xyz"}]
    found=False
    for customer in customer_list:
     if id==customer["uid"]:
        print('-'*10+'Customer Detail'+'-'*10)
        print(f"Name:{customer['name'].rjust(19)}")                  
        print(f"Address:{customer['address'].rjust(16)}")
        print('------------------------------------')     
        found=True                                                
        break
     else:
        found=False

def calculation_one():
   consumed=pres_rdg-prev_rdg
   print(f"Pres Rdg:{str(pres_rdg).rjust(15)}")
   print(f"Prev Rdg:{str(prev_rdg).rjust(15)}")
   print(f"Consumed units: {str(consumed).rjust(8)}")
   print('-'*35)

def calculation_two():
    consumed=pres_rdg-prev_rdg
    amt=consumed*5.90
    atm=consumed*0.48
    tax=amt*0.09
    tatalamt=720+amt+atm+tax
    print("Bill For Consumed Units")
    print("\nFixed Charges(Unit,Rate,Amt)")
    print("\t6.00\t120.00\t720")
    print("\nEnergy Charges(Unit,Rate,Amt)")
    print(f"\t{consumed}\t5.90\t{amt}")
    print('FPPCA (Unit,Rate,Amt)')
    print(f"\t{consumed}\t0.48\t{atm}")
    print(f"Tax(9%){str(tax).rjust(22)}")
    print("-"*35)
    print(f"Net Payable:{f'{round(tatalamt, 2):.2f}'.rjust(10)}")
    
def due_date():
   current_date = datetime.now()
   day_due_date=15
   due_date=current_date + timedelta(days=day_due_date)
   print(f"Due Date:{due_date.strftime('%d-%m-%Y').rjust(16)}")
   print("-"*35)



time()   
data_base()
calculation_one()
calculation_two()
due_date()