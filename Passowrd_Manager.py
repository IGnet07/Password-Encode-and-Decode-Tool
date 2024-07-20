from cryptography.fernet import Fernet

# Function to load the encryption key from a file
def load_key():
    """
    Load the encryption key from the 'key.key' file.
    
    Returns:
        bytes: The encryption key read from the file.
    """
    with open("key.key", "rb") as file:
        key = file.read()
    return key

# Prompt user to enter the master password
master_password = input("Please Enter the Master Password: ")

# Load the encryption key and combine it with the master password
key = load_key() + master_password.encode()
fer = Fernet(key)

# Function to add a new account name and password
def add():
    """
    Add a new account name and password to the 'user_passwords.txt' file.
    Encrypts the password before storing it.
    """
    name = input("Account Name: ")
    pswd = input("Enter Password: ")
    encrypted_password = fer.encrypt(pswd.encode()).decode()
    
    # Append the encrypted password to the file
    with open('user_passwords.txt', 'a') as f:
        f.write(name + '|' + encrypted_password + '\n')

# Function to view existing passwords from the 'user_passwords.txt' file
def view():
    """
    Read and decrypt passwords from the 'user_passwords.txt' file.
    Displays the account name and corresponding decrypted password.
    """
    with open('user_passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, encrypted_password = data.split("|")
            decrypted_password = fer.decrypt(encrypted_password.encode()).decode()
            print("User : " + user + "\n" + "Passwd:  " + decrypted_password)

# Main loop for user interaction
while True:
    operation = input("Enter the operation you want to perform - Add (New Password) or View (Existing Password). Choose one (Add/View) or 'q' to quit: ").lower()
    
    if operation == "q":
        break
    elif operation == 'add':
        add()
    elif operation == 'view':
        view()
    else:
        print("Invalid Operation\n")
