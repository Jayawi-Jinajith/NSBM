# Q7 - Hotel Reservation & Check-in System

# 1 - room: must be available
# 2 - customer: must provide a valid ID
# 3 - customer: must pay advance payment
# 4 - customer: must stay for at least 1 night

rooms = input("Rooms available (yes/no): ")
if rooms[0].upper() == "Y":
    customer_id = input("Do you have a valid ID (yes/no): ")
    if customer_id[0].upper() == "Y":
        adv_payment = input("Advance Payment Completed (yes/no): ")
        if adv_payment[0].upper() == "Y":
            nights = int(input("How many nights you want to stay: "))
            if nights >= 1:
                print("Customer can check into the hotel")
            else:
                print("Cannot check-in. Customer must stay for at least 1 night")
        else:
            print("Cannot proceed. Customer must pay advance payment before check-in")
    else:
        print("Cannot proceed. Customer doesn't has a valid ID")
else:
    print("No Rooms Available at the moment")
