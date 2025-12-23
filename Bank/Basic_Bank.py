# Creating Basic bank account using file-handling
import os

File_name = "Balance.txt"

# if not os.path.exists(File_name):
if File_name not in os.listdir():
    with open(File_name,"w") as f:
        f.write("0")

def file_write(cm):
    # f = open(File_name,"w+")
    # f.write(str(cm))
    # f.close()
    # print("Updated Successfully")
    with open(File_name,"w") as f:
        f.write(str(cm))
    print("Balance Updated Successfully")

def file_read():
    # f = open(File_name,"r")
    # cm = int(f.read())
    # f.close()
    with open(File_name,"r") as f:
        cm = int(f.read())
    return cm


def deposit():
    cm = file_read()
    dm = int(input("Enter Deposit Money: "))
    if dm < 0:
        print("Invalid Money")
    else:
        cm+=dm
        file_write(cm)
        print("Money deposited successfully")


def withdraw():
    cm = file_read()
    wm = int(input("Enter Withdraw Money: "))
    if wm > cm:
        print("Insufficient Balance")
    else:
        cm-=wm
        file_write(cm)
        print("Money withdrawn successfully")

def display_balance():
    print(f"Total Balance: ",file_read())

while True:
    print("Choose from the following options:")
    print("1. Deposit Money \n2. Withdraw Money \n3. Display Balance \n4. Exit")
    x = int(input("Enter your choice Number: "))
    if x == 1:
        deposit()
    elif x == 2:
        withdraw()
    elif x == 3:
        display_balance()
    elif x == 4:
        break
    else:
        print("Invalid Choice")