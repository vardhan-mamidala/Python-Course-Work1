sales = int(input("Enter the sales: "))

if sales>1000:
    print("Best Seller")


    eli_acc = eval(input("Eligible Accout: "))
    ver_sub = eval(input("Meta Verified subscription: "))

    if eli_acc and ver_sub:
        print("Verified badges Granted")
        

rain_status = eval(input("Enter the rain status: "))
if rain_status:
    print("Extra Rain Charges Applied")


username = input("username: ")
password = input("password: ")