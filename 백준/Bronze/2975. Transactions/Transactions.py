transactions = []
while True:
    line = input().strip()
    if line == "0 W 0":
        break
    transactions.append(line)

for transaction in transactions:
    balance, operation, amount = transaction.split()
    balance = int(balance)
    amount = int(amount)
    if operation == "W":
        if balance - amount < -200:
            print("Not allowed")
        else:
            balance -= amount
            print(balance)
    elif operation == "D":
        balance += amount
        print(balance)



