bank_balance = int(input("Enter Bank Balance : "))
user_pin  = int(input("Enter Pin No : "))

print("Deposite : 1")
print("Withdraw : 2")

option = int(input("Enter Choice: "))

user_pin_2 = int(input("Enter Pin Again for process : "))

if user_pin == user_pin_2:
    amount = int(input("Enter Amount : "))
    if option==2:
        bank_balance = bank_balance - amount
        print("you withdraw: ", amount)
        print("your Bank Balance is Now: ", bank_balance)
    else:
        bank_balance = bank_balance + amount
        print("Succefully added in your account")
        print("Your bank balance is Now: ", bank_balance)
else:
    print("Your Pin is Incorrect")