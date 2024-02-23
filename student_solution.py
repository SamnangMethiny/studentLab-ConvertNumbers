def hexToDecimal(hexString):
    hex_digits = "0123456789ABCDEF"
    decimal_value = 0
    # -1 since len() counts from 1 but numbering system start from 16 ** 0
    power = len(hexString) - 1 
    
    # Iterate over each character in the hexString
    for digit in hexString:
        # Convert the character to uppercase
        digit = digit.upper()
        # Calculate decimal value for the current digit
        decimal_value += hex_digits.index(digit) * (16 ** power)
        power -= 1
        
    return decimal_value

def decimalToBinary(decimalValue):
    binary = ""
    while decimalValue != 0:
        # Prepend the remainder of decimalValue divided by 2 (0 or 1) to binary
        binary = str(decimalValue % 2) + binary
        # Divide decimalValue by 2 for the next iteration
        decimalValue //= 2
    return binary




# # Example usage (not necessary for the assignment, just for student testing)
# if __name__ == "__main__":
#     # Hexadecimal to Decimal
#     print("Hexadecimal 'A' to Decimal:", hexToDecimal('A'))
#     print("Hexadecimal '1A' to Decimal:", hexToDecimal('1A'))

#     # Decimal to Binary
#     print("Decimal 2 to Binary:", decimalToBinary(2))
#     print("Decimal 5 to Binary:", decimalToBinary(5))
