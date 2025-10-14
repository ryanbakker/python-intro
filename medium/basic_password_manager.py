from cryptography.fernet import Fernet

# Create key file and input generated fernet key
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


# Open the file, read the key, close the file, return key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    # open as f - file
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            # Strip off \n from return
            data = (line.rstrip())
            # We can pass user, passw as the list has 2 elements (user, pass), thus auto assigned the 0 and 1 index
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    # Using "with" will auto close the file after opening it, simply using open won't close the file when finished using it
    # Open receives the file name, then (a: append - add something to end of file or create if it doesn't exist), (w: write/override), (r: read)
    with open("passwords.txt", "a") as f:
        # Add line break after username / password
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (add/view)? or press Q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
