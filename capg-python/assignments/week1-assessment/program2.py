def temp_conv():
    temp = int(input("Enter temperature to convert:-"))
    conv = input("Enter type of temperatue \n 'c' for celsius \n 'f' for farenheit \n 'k' for kelvin:")

    if(conv=="c"):
        print("temperature in farenheit is:", (temp*5/9)+32)
        print("temperature in kelvin is :", temp + 273.5)
    elif(conv == "f"):
        print("temp in celsius is:", (temp - 32) * 5/9)
        print("temp in kelvin is:", ((temp - 32) * 5/9) + 273.5)
    elif(conv == "f"):
        print("temp in celsius is:", temp - 273.15)
        print("temp in faranheit is:", ((temp - 273.5) * 9/5) + 32)
    else:
        print("input a correct format for type of temperature")
        temp_conv()
temp_conv()
