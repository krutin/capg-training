

def password_checker():
    s = input("Enter a password to check")

    if(len(s)<8):
        return "password too short, try again"

    u = l = d = spe = False
    for char in s:
        if(char.isupper()):
            u  = True
        elif(char.islower()):
            l = True
        elif(char.isnumeric()):
            d = True
        else:
            spe = True
    if(not u):
        return "password must contain lower letters, try again"
    if(not l):
        return "password must contain upper letters, try again"
    if(not d):
        return "password must contain numbers, try again"
    if(not spe):
        return "password must contain special characters, try again"
    
    return "strong password."
print(password_checker())