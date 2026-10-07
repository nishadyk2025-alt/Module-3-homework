print("----- Due Amount Calculator -----")
bill_amount = float(input("Enter total bill amount: "))
paid_amount = float(input("Enter amount paid by customer: "))
if (paid_amount - bill_amount)>0:
    change = paid_amount - bill_amount
    print("Bill is fully paid")
    print("Change to return:", change)
else:
    due = bill_amount - paid_amount
    print("Bill is not fully paid")
    print("Due amount:", due)
print("---------------------------------------")
print("Total bill:", bill_amount)
print("Amount paid:", paid_amount)
print("Amount due:", bill_amount - paid_amount)
print("Thank you for shopping!")