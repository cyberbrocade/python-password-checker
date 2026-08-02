print("Welcome to Password the Password Checker, test and see if a password valid")

def is_valid(password):
    if len(password) < 12:
        print("Password must be at least 12 characters")
        return False
    if password == "":
        print("Password can't be empty")
        return False
    if " " in password:
        print("Password must not contain spaces")
        return False
    if not any(char.isdigit() for char in password):
        print("Password must contain at least 1 digit")
        return False
    if password.isalnum():
        print("Password must contain at least 1 special character")
        return False
    return True


for x in range(1000):
    password = input("Enter your password: ")
    while  not is_valid(password):
        password = input("Enter your password: ")

    print("Well done! This is a fine password.")

    again = input("Do you wanna try another password? (y/n): ").strip().lower()
    if again != ("y" or "yes"):
        break
