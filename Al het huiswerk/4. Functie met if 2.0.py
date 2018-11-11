def new_password(oldpassword, newpassword):
    if len(newpassword) <6:
        print(True)


newpassword = input("What will be your new password?")
oldpassword = input("what was your old password? ")
new_password(oldpassword,newpassword)