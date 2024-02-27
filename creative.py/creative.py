def add_name(names, new_name):
    if new_name not in names:
        names.append(new_name)
        print(f"{new_name} added successfully!")
    else:
        print(f"{new_name} already exists!")

def remove_name(names, name):
    if name in names:
        names.remove(name)
        print(f"{name} removed successfully!")
    else:
        print(f"{name} doesn't exist in the list!")

def main():
    names = []

    while True:
        print("\nCurrent Names:", names)
        print("1. Add a name")
        print("2. Remove a name")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_name = input("Enter the name you want to add: ")
            add_name(names, new_name)
        elif choice == '2':
            name = input("Enter the name you want to remove: ")
            remove_name(names, name)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
