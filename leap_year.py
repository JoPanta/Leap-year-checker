# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


# is it divisible by 4with no remainder?
if year % 4 == 0:
    # is it divisible by 100 with no remainder?
    if year % 100 == 0:
        # is it divisible by 400 with no remainder?
        if year % 400 == 0:
            print("Leap year.")
            # if not:
        else:
            print("Not leap year.")
            # if not:
    else:
        print("Leap year.")
# if no:
else:
    print("Not leap year.")
