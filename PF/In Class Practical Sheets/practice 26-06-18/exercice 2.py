# Q2 - Aircraft engine temperature monitoring

i = 1
safe = 0
maintain = 0

while i <= 4:
    input_text = "Engine " + str(i) + " - Temperature (ºC): "
    eng_temp = float(input(input_text))
    if eng_temp >= 200 and eng_temp <= 800:
        print("Engine ", str(i), ": Safe")
        safe = safe + 1
    else:
        print("Engine ", str(i), ": Maintainance Required")
        maintain = maintain + 1
    i = i + 1

print("Safe Engines = ", str(safe))
print("Maintainance Required Engines = ", str(maintain))