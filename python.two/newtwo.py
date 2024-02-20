#number to Alphabet


def print_number_in_alphabet(number):
    number_to_alphabet = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 
        5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
    }
    
    number_str = str(number)
    
    for digit in number_str:
        if digit.isdigit():
            print(number_to_alphabet[int(digit)], end=' ')


number = int(input("Enter a number: "))
print("Number in alphabet:")
print_number_in_alphabet(number)
