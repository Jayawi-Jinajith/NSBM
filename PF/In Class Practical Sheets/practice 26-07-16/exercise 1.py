product_id = []
name = []
price = []

i = 1
while i <= 1:
    pid = input(f"Product {i} - product id:    ")
    product_id.append(pid)

    p_name = input(f"{" "*12}product Name:  ")
    name.append(p_name)
    
    p_price = float(input(f"{" "*12}product Price: "))
    price.append(p_price)

    print()
    i += 1

j = 0
while j < 10:
    print(f"{product_id[j]:5} - {name[j]:12} ---------- Rs {price[j]:10,.2f}")
    j += 1

