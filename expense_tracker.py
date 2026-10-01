
expenses =[]
while True:
    print("=== Expense Tracker ===")
    print(" 1.Add Expense")
    print(" 2.View Expense")
    print(" 3.Show Total")
    print(" 4.Exit")


    choice = input("Choose an option: ")

    if choice == "1":
      print("Add Expense Selected")
      category = input("Enter Category: ")
      amount = int(input("Enter Amount:"))
      expenses.append({"category": category , "amount": amount})
    elif choice == "2":
     print("View Expense Selected")
     for expense in expenses:
      print(expense["category"],":" ,expense["amount"])
    elif choice =="3":
     print("Show Total Selected")
     total=0

     for expense in expenses:
       total += expense["amount"]
     print(" Total:",total)
    elif choice =="4":
     print("Goodbye!")
     break
    else: 
     print("Invalid Choice")

    
    
    