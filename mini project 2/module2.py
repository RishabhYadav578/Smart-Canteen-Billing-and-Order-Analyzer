print("========== SMART CANTEEN ==========")
Veg_Sandwich=60
Masala_Dosa=80
Chole_Rice=90
Paneer_Roll=100
Tea=20
print(f"Veg Sandwich-{Veg_Sandwich} \nMasala Dosa-{Masala_Dosa} \nChole_Rice-{Chole_Rice} \nPaneer Roll-{Paneer_Roll} \nTea-{Tea}\n")
subtotal=0
count1=0
count2=0
count3=0
count4=0
count5=0
while(True):
    choose_item=int(input("\nchoose the item "))
    enter_quantity=int(input("enter quantity:"))
    if choose_item==1:
        print(f"Added: Veg Sandwich*{enter_quantity}={Veg_Sandwich*enter_quantity}")
        subtotal = subtotal+Veg_Sandwich*enter_quantity
        count1=count1+enter_quantity

    elif choose_item==2:
        print(f"Added: Masala Dosa*{enter_quantity}={Masala_Dosa*enter_quantity}")
        subtotal = subtotal+ Masala_Dosa*enter_quantity  
        count2=count2+enter_quantity
    elif choose_item==3:
        print(f"Added: Chole Rice*{enter_quantity}={Chole_Rice*enter_quantity}")
        subtotal = subtotal+ Chole_Rice*enter_quantity
        count3=count3+enter_quantity
    elif choose_item==4:
        print(f"Added: Paneer Roll*{enter_quantity}={Paneer_Roll*enter_quantity}")
        subtotal = subtotal+ Paneer_Roll*enter_quantity
        count4=count4+enter_quantity
    elif choose_item==5:
        print(f"Added: Tea*{enter_quantity}={Tea*enter_quantity}")
        subtotal = subtotal+ Tea*enter_quantity
        count5=count5+enter_quantity
    else:
        print("this is not in menu...\n")
    add_item=input("Add another item? (y/n) ")
    if add_item=='y':
        continue
    elif add_item=='n':
        print("thanks for buying")
        break
    else:
        while(True):
            add_item=input("Add another item? (y/n) ")
            if add_item=='n':
                print("thanks for buying...")
                break
            elif add_item=='y':
                break
    if add_item=='n':
        break                  
print("\n========== RECEIPT ==========")
if count1!=0:
    print(f"\nVeg Sandwich * {count1}:Rs{Veg_Sandwich*count1}")
if count2!=0:
    print(f"Masala Dosa * {count2}:Rs{Masala_Dosa*count2}")
if count3!=0:
    print(f"Chole Rice * {count3}:Rs{Chole_Rice*count3}")
if count4!=0:
    print(f"Paneer Roll * {count4}:Rs{Paneer_Roll*count4}")
if count5!=0:
    print(f"Tea * {count5}:Rs{Tea*count5}")
print(f"subtotal:Rs{subtotal}")
if subtotal>=500:
    discount=subtotal*(10/100)
    print(f"discount:Rs{discount}")
elif subtotal>=250 and subtotal<=499:
    discount=subtotal*(5/100)
    print(f"discount:Rs{discount}")
else:
    discount=0
    print(f"discount:Rs{discount}")
final_total=subtotal-discount
print(f"Final total:Rs{final_total}")
print("Thank you!")

     

     

     
     

    
