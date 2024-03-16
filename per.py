def calculate_percentage(part, whole):
    percentage = (part / whole) * 100
    return percentage

def main():
    try:
        part = float(input("Enter the part: "))
        whole = float(input("Enter the whole: "))
        
        if whole == 0:
            print("Error: Cannot divide by zero. Please enter a non-zero value for the whole.")
            return
        
        percentage = calculate_percentage(part, whole)
        print("The percentage is:", percentage, "%")
    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    main()
