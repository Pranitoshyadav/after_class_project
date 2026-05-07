age_input = input("Enter your age: ")

if age_input.isdigit():
    age = int(age_input)
    
    if 0 <= age <= 120:
        print(f"Your age is {age}.")
        
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")
    else:
        print("Error: Age entered is not realistic. Please enter a value between 0 and 120.")
else:
    print("Error: Invalid input. Please enter a numeric value for age.")
