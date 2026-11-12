import database_functions as dbf

dbf.initialize_database()

while True:
    print("Welcome to SQL Database program, choose an option to continue:")
    option = input("1. Add user\n" \
                   "2. Show users\n" \
                   "3. Exit\n" \
                   "Choose an option: ")

    if option == "1":
        name = input("Name: ")
        age = int(input("Age: "))

        dbf.add_user(name, age)

    elif option == "2":
        dbf.show_users()

    elif option == "3":
        break

print("Thank you for using the SQL Database program. Goodbye!")
