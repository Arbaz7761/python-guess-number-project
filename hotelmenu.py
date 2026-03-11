menu = {"pizza" : 40,
        "burger" : 50,
        "pasta" : 60,
        "salad" : 20,
        "coffe" : 80

}

print("welcome to PYTHON Restaurant")
print("pizza: Rs40\nburger: Rs50\npasta: Rs60\nsalad: Rs20\ncoffe: Rs80")

order_total = 0

item = input("enter your items what you want to order = ")
if item in menu:
    order_total += menu[item]
    print(f"your item {item} has been added to your order")
else:
    print(f"order item {item} is not available yet!")    

another_order = input("do you want add another item (yes/no) ")
if another_order == "yes":
    item2 =  input("enter the name of second item = ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"item {item2} has been added to order")
    else:
        print(f"ordered item {item2} is not available!")
print(f"The total amount of itmes to is {order_total}")        






