# Restaurent project
# step 1: show the menu
print(" Welcome to Gani's Restaurent")
print(" Today's Menu:")
print("1. Burger: ₹100 (small) / ₹150 (large)")
print("2. Pizza: ₹200 (small) / ₹300 (large)")
print("3. Sandwich: ₹80 (regular) / ₹120 (grilled)")


# step 2: ask user for their choice
choice = int(input(" Enter your choice (1 for burger, 2 for pizza, 3 for sandwich):"))

if choice == 1:
    size= int(input("Enter the size of Burger (1 for small, 2 for large):"))
    if size == 1:
        price = 100
    elif size == 2:
        price = 150

elif choice ==2:
    size= int(input("Enter the size of pizza (1 for small, 2 for large):")) 
    if size == 1:
        price = 200
    elif size == 2:
        price = 300

elif choice ==3:
    size=int(input("Enter the size of sandwich  (1 fro regular, 2 for grilled):")) 
    if size == 1:
        price = 80
    elif size == 2:
        price = 120  

else:
    price = 0  # invalid choice for size
    print("Invalid size selected.")
# step 4: if price is valid ask quantity and calculate total

if price>0:
    quantity = int(input("Enter the no.of items do you want:"))
    total =price*quantity
    print(f"Your total bill: Rs.{total}")

else:
    print("Unable to calculate total amount due to invalid input.")    
