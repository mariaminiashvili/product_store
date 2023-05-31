product = {
    "phone1" : 500,
    "phone2" : 600,
    "phone3" : 700
}

def print_product():
    print("მოგესალმებით!")
    for key, value in product.items():
        print(f"დასახელება:{key},   ფასი:{value}ლარი")
    ask_product()

def ask_product():
    input_product = input("რომელი მოდელი გნებავთ:")
    if product.get(input_product):
       confirm(input_product)
    else:
       print("არ გვაქვს")    
       ask_product()
 
def confirm(choose):
     print(f"პროდუქტის ფასი:{product[choose]}ლარი")
     confirm_purchase = input("ნამდვილად გსურთ შეძენა?")
     if confirm_purchase == "დიახ":
        print("შეკვეთა გაფორმებულია. მადლობა დაინტერესებისთვის, კარგად ბრძანდებოდეთ.")
     else:
         buy_another = input("სხვა რამ ხომ არ გნებავთ?")
         if buy_another == "დიახ":
             print("პროდუქტი ამოიწურა, კარგად ბრძანდებოდეთ.")
         else:
            print("კარგად ბრძანდებოდეთ")
 
print(print_product())
 