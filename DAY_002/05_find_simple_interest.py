print("Welcome To Simple Interest Calculator")
principal_amount = float(input("Please enter principal amount. $"))
rate_of_interest = float(input("Please enter rate of interest."))
year = int(input("Please enter number of years. "))
simple_interest = (principal_amount * rate_of_interest * year) / 100
print(f"Your simple interest is: {round(simple_interest, 2)}")
