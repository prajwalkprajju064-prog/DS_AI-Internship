cart=[]
print("welocome to shopping")
print("type 'done' when you finish shopping")

while True:
    fruit = input("Enter a fruit to add: ")
    
    
    if fruit=="DONE":
        break
    
    cart.append(fruit)
    print(f"{fruit} added  to cart ")
    
print("your shopping cart contains:")
for item in cart:
    print("-",item)