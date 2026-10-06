import my_calculator_module

print("Hi, this is a calculator program. I can increment and decrement numbers by 1.")
retries = 0
while retries < 3:
    option = input("Please select an option to continue: \n1. Increment a number by 1\n2. Decrement a number by 1\n")

    if option == "1":
        number = int(input("Please enter a number: "))
        result = my_calculator_module.increment_by_one(number)
        print(f"The incremented value is: {result}")
        break
    
    elif option == "2":
        number = int(input("Please enter a number: "))
        result = my_calculator_module.decrement_by_one(number)
        print(f"The decremented value is: {result}")
        break
    
    else:
        if retries == 2:
            print("You have exceeded the maximum number of retries.")
            break
        print("Invalid option. Please try again.")
        retries += 1

print("Thank you for using the calculator program. Goodbye!")