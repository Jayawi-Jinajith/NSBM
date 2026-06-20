# Q6 - Online Shopping Checkout System

# 1 - status > logged in
# 2 - cart value > Rs.1000.00
# 3 - payment must be successful

login_valid = input("Are you logged in? (Yes/No): ")
if login_valid[0].upper() == "Y":
    cart_value = float(input("Enter Cart Value: Rs."))
    if cart_value > 1000:
        print("Please proceed with the Payment")
        payment_valid = input("Payment Successful (Yea/No): ")
        if payment_valid[0].upper() == "Y":
            print("Payment confirmed. Order is Successful")
        else:
            print("Payment not successful. Cannot proceed the Order")
    else:
        print("Cart value is lower than minimum Checkout Value")
        print("Cart value must excced Rs.1000.00")
else:
    print("Cannot proceed the checkout")
    print("Must log in before checkout")
