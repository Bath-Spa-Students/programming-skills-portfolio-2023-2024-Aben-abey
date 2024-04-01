# Describe the quantity of money that she has in her possession.
money = 50

# 
price_per_usb = 6

# Calculate the number of USB sticks That she can buy.
num_usb = money // price_per_usb

# Calculate the remaining money
remaining_money = money % price_per_usb

# Print the results
print(f"The Girl can buy {num_usb} USB sticks.")
print(f"He will have {remaining_money} pounds left.")