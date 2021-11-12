import time
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "Nenye" and password == "1010":
    print("welcome to CyberSafe " + username)
    print(" ")
    account_type = input("savings or current? ")
    transaction_type = input("Deposit or withdrawal? ")

if account_type == "savings" and transaction_type == "withdrawal" :
    print("proceed to enter amount")
    
amount = int(input("enter here: "))
if amount <= 15000:
    print("Please hold on your transaction is processing")
    time.sleep(10)
    print("Please take your cash")
    time.sleep(6)
    print("THANK YOU FOR BANKING WITH US, dont get poor!")
elif amount > 15000:
    print("sapa nice one!! insufficient balance")        

elif account_type == "current" or transaction_type == "Deposit" :
    print("oops! seems like an error occured")    
     
 
else:
    print("sorry boss, i dont know you")