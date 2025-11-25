import art
print(art.logo)

# 2. CORE LOGIC FUNCTION (The workhorse)
def caesar_shift(input_text, effective_shift_value):
    # This function contains the loop and the modulo arithmetic.
    # It doesn't care if 'effective_shift_value' is positive or negative.
    # It just applies: (position + effective_shift_value) % 26
    ...
    result = ''
    for char in input_text:
        if 'a' <= char <= 'z':  # Check for lowercase letters
            start_ord = ord('a')
            new_ord = (ord(char) - start_ord + effective_shift_value) % 26 + start_ord
            result += chr(new_ord)

        elif 'A' <= char <= 'Z':  # Check for uppercase letters
            start_ord = ord('A')
            new_ord = (ord(char) - start_ord + effective_shift_value) % 26 + start_ord
            result += chr(new_ord)

        else:
            # Keep spaces and other characters (numbers, punctuation) as they are
            result += char
    return result


# 3. MAIN PROGRAM FLOW (The controller)
def run_cipher():
    # Loop to keep the program running until the user quits
    running_cipher = True
    while running_cipher:
        # 1. Get user 'encode' or 'decode' choice
        choice = input("What you want: type (encode/decode)?  ")
        message = input("What do you want to cipher: ")
        # print(text)
        shift_number = int(input("What number of shift you want for cipher: "))

        # 2. Get the message and the shift_number

        # 3. Determine the final shift value to pass:
        if choice == 'decode':
            final_shift = -shift_number
        elif choice == 'encode':  # 'encode'
            final_shift = shift_number
        else:
            print("You have invalid choice.")
            continue

        # 4. Call the unified core function
        output = caesar_shift(message, final_shift)
        print(output)

        # 5. Display output and ask to continue
        continue_selection = input("Do you want to continue? Type 'yes' or 'no': ").lower()
        if continue_selection == 'no':
            running_cipher = False
            print("Cipher program terminated. Goodbye!")

run_cipher()
