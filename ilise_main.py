# Ilise Hyams

def print_menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')


def encode(password_to_encode):
    encoded_password = ''
    for x in password_to_encode:
        if int(x) <= 6:
            new_val = int(x) + 3
            encoded_password += str(new_val)
        if int(x) == 7:
            new_val = 0
            encoded_password += str(new_val)
        if int(x) == 8:
            new_val = 1
            encoded_password += str(new_val)
        if int(x) == 9:
            new_val = 2
            encoded_password += str(new_val)
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for i in encoded_password:
        i = int(i)
        if i == 0:
            i = 7
        elif i == 1:
            i = 8
        elif i == 2:
            i = 9
        else:
            i -= 3
        i = str(i)
        decoded_password += i
    return decoded_password



if __name__ == '__main__':
    print_menu()
    print('')
    option = int(input('Please enter an option: '))
    while option != 3:
        if option == 1:
            password_to_encode = str(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!')
            print('')
            encoded_password = encode(password_to_encode)
            print_menu()
            option = int(input('Please enter an option: '))
        if option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
            print()
            print_menu()
            option = int(input('Please enter an option: '))
