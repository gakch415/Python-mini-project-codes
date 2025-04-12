# Restaurent project
print(" Welcome to Gani's Restaurent")
print(" Today's Menu:")
print("1. Burger: 100 (small) / 150 (large)")
print("2. Pizza: 200 (small) / 300 (large)")
print("3. Sandwich: 80 (regular) / 120 (grilled)")

total_bill= 0

while True:

    choice = int(input(" Enter your choice (1 for burger, 2 for pizza, 3 for sandwich):"))
    price = 0

    if choice == 1:
        size= int(input("Choose the Burger size (1-small, 2-large):"))
        if size == 1:
            price = 100
        elif size == 2:
            price = 150
        else:
            print(" Invalid Burger size.")  
            continue  

    elif choice ==2:
        size= int(input("Choose the pizza size (1-small, 2-large):")) 
        if size == 1:
            price = 200
        elif size == 2:
            price = 300
        else:
            print(" Invalid Pizza size.")
            continue    

    elif choice ==3:
        size=int(input("Choose type of sandwich  (1-regular, 2-grilled):")) 
        if size == 1:
            price = 80
        elif size == 2:
            price = 120 
        else:
            print("Invalid sandwich type.")
            continue    

    else:
        print("Select Invalid and Try again.")
        continue

    quantity = int(input("Enter quantity:"))
    item_total = price*quantity
    print(f"item total: ₹{item_total}")
    total_bill += item_total


    another = input("Do you want to order another item? (yes/no):").lower()
    if another == "no":
        break

print(f" Your final bill is: ₹{total_bill}")
print(f" thank you for dining with Gani's Restaurent!")

    



