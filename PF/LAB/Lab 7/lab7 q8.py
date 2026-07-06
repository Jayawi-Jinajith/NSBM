# Q8 - Bus Ticket Booking

available = 40
booked = 0
success = 0

while True:
	seats = int(input("Number of seats: "))
	if seats == 0:
		break
	if seats > available:
		print("Not Enough Available Seats")
		print(available)
		continue
	else:
		available -= seats
		booked += seats
		success += 1
print(f"Total seats booked = {booked}")
print(f"Remaining seats = {available}")
print(f"Number of Successful Bookings = {success}")