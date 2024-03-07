
user_details = {}

def add_user():
  
    name = input("Enter your name: ")
    age = input("Enter your age: ")

  
    user_details[name] = {'age': age}
    print(f"{name}'s details have been added.")

def remove_user():
  
    name_to_remove = input("Enter the name to remove: ")

  
    if name_to_remove in user_details:
        del user_details[name_to_remove]
        print(f"{name_to_remove}'s details have been removed.")
    else:
        print(f"{name_to_remove} not found in the user details.")

def display_user_details():
  
    print("\nUser Details:")
    for name, details in user_details.items():
        print(f"Name: {name}, Age: {details['age']}")

while True:
    print("\nOptions:")
    print("1. Add User")
    print("2. Remove User")
    print("3. Display User Details")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_user()
    elif choice == '2':
        remove_user()
    elif choice == '3':
        display_user_details()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
