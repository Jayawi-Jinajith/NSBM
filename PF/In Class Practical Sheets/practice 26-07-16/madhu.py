Medicine_ID=[]
Medicine_Name=[]
Medicine_Price=[]

index=0

while index<5:

    Medicine_ID.append(input(f"Enter Medicine {index+1} ID: "))
    Medicine_Name.append(input(f"Enter Medicine {index+1} Name: "))
    Medicine_Price.append(input(f"Enter Medicine {index+1} Price: "))

    index+=1

print(f"{'Medicine_ID':<15}{'Medicine_Name':<20}{'Medicine_Price':<15}")

for i in range(5):

    print(f"{Medicine_ID[i]:<15}{Medicine_Name[i]:<20}{Medicine_Price[i]:<15}")




    