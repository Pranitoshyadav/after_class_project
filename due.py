a = int(input("enter the ammount you owe : "))
b = int(input("enter hoe much did you pay : "))

if a > b:
    print("You still need to pay Rs.",a - b)
elif b > a:
    print("The person needs to return you RS.",b - a)
else:
    print("You paid the exact amount")