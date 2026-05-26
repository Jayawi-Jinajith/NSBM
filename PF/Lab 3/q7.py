# Q7 - University Course Fee Calculator

print("University Course Fee Calculator\n")
modules = int(input("Enter the number of modules you enrolled: "))
module_fee1 = float(input("Enter the fee per module: Rs."))
lib_fee = float(input("Enter the library fee: Rs."))
reg_fee = float(input("Enter the registration fee: Rs."))

module_fee = modules * module_fee1
total_fee = module_fee + lib_fee + reg_fee

print("Registration Fee >>> Rs." + str(reg_fee))
print("     Library Fee >>> Rs." + str(lib_fee))
print("      Module Fee >>> Rs." + str(module_fee))
print("\n       Total Fee >>> Rs." + str(total_fee))
