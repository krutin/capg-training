def string_analyse():
    s = input("Enter a string you want to analyse:\n")
    vowels, cons , num , special = 0,0,0,0
    for cha in s:
        if(cha.lower() in ["a","e","i","o","u"]):
            vowels += 1
        elif(cha.isalpha()):
            cons += 1
        elif(cha.isnumeric()):
            num += 1
        else:
            special += 1
    print("The string contains\n {} vowels, {} consonants, {} numbers and {} special charectors".format(vowels,cons,num,special))


string_analyse()