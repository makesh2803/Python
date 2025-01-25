goods = {"Milk (drinks)" : 4,
         "Bread (bakery)" : 2,
         "Apple (fruits)" : 3,
         "Egg (dairy and protein)" : 5,
         "Cheese (dairy)" : 6,
         "Sausage (meat)" : 8         
         }
bought_products = {}
while True:
    for i, j in goods.items():
        print(f"- {i} : {j} TMT")
    product = input("Enter the product you want to buy or type 'done' to finish: ").capitalize()
    if product == 'Done':
        break
    
    matched_product = None 
    for haryt in goods:
        if product == haryt.split()[0]:
            matched_product = haryt
            break
    if matched_product:
        quantity = int(input(f"Enter the quantity of {matched_product}: "))
        if matched_product in bought_products:
            bought_products[matched_product] += quantity
        else:
            bought_products[matched_product] = quantity
        print(f"Added {quantity} x {matched_product} to your cart")
    else:
        print("Sorry, that product is not available. Please choose another.")

total_bill = 0
if bought_products:
    print("You bought the following products: ")
    for product, quantity in bought_products.items():
        price = goods[product]
        total = price * quantity
        total_bill += total
        print(f"- {product}: {quantity} * {price} TMT = {total} TMT")
else:
    print("You didn't buy anything")
    
print(f"""Your total bill is:
{total_bill} TMT""")
print("Thank you for shopping!")