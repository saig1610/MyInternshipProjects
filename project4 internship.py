import random

#TITLE OF THE PROJECT
print("PYTHON PROGRAMMING PROJECT - 4\n")
print("PROJECT TITLE : PASSWORD GENERATOR\n") 
print("GENERATES PASSWORDS WITH A MIX OF UPPERCASE/LOWERCASE/SPECIAL CHARACTERS \n")

# Define character sets for different types of characters
def generate_password(length=12):
    
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQSTUVWXYZ'
    digits = '0123456789'
    special_characters = '!@#$%^&*()_-+=<>?/[]{}|'

    # Combine all character sets into one
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure that at least one character from each set is included
    password = random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(digits) + random.choice(special_characters)

    # Generate the rest of the password with the specified length
    password += ''.join(random.choice(all_characters) for _ in range(length - 4))
    
    # Shuffle the password characters for added security
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def generate_passwords(num_passwords=1, length=12):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length)
        passwords.append(password)
    return passwords

if __name__ == "__main__":
    print("Welcome to the Strong Password Generator!")
    
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))

    generated_passwords = generate_passwords(num_passwords, password_length)

    print("\nGenerated Passwords:")
    for i, password in enumerate(generated_passwords, 1):
        print(f"Password {i}: {password}")

    print("\nPlease save these passwords in a secure place and do not share them.")
