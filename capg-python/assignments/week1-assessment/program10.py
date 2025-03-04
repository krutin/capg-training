
def bill_splitter():
    bill = int(input("enter bill amount:"))
    members = int(input("enter the number of members to split the bill:"))
    tip = int(input("enter tip percentage of tip to add"))

    tip_amount = (tip / 100 ) * bill

    total = bill + tip_amount
    split = total/members
    print("The amount each person should pay is: ", split)

bill_splitter()