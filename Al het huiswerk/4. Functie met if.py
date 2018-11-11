oldpassword = (input("Enter your current password: "))
newpassword = (input("Enter your new password:"))

def new_password(oldpassword, newpassword):
    if (newpassword != oldpassword) and (len(newpassword) > 6):
        return "New password has been set!"
    return "You can't use this password (It shoud be different than your old password and it must contain of at least 6 characters)"

print(new_password(oldpassword, newpassword))