# Trata erros de entrada e imprime uma mensagem que diz se o código é válido ou não

def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    
    for i in range(0, len(isbn)):
        if not isbn[i] in "0123456789":
            if i == len(isbn)-1 and isbn[i].lower() == "x":
                continue
            print("Invalid character was found.")
            return
    
    given_check_digit = isbn[length-1]
    main_digits_list = [int(digit) for digit in isbn[:length-1]]
    
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    
    result = 11 - digits_sum % 11
    
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    
    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    
    result = 10 - digits_sum % 10
    
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def main():
    try:
        user_input = input('Enter ISBN and length: ')
        values = user_input.split(',')
        isbn = values[0]
        length = int(values[1])
        if length == 10 or length == 13:
            validate_isbn(isbn, length)
        else:
            print('Length should be 10 or 13.')
    except IndexError:
        print("Enter comma-separated values.")
        return
    except ValueError:
        print("Length must be a number.")
        return

main()
