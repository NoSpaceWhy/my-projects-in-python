from cryptography.fernet import Fernet

'''
def write_eye():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb").read()
    file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split('|')
            print("Username: " + user + "| Password: " + password,
                fer.decrypt(password.encode()).decode())
            
def add():
    name = input("Account Name: ")
    pwd = input("Enter your Password: ")
    
    with open('password.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + "\n")
        
    
while True:
    mode = input("What mode do you want to use(view/Add) Q/q to quit?: ").lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode")
        continue