def fizbuz():
    for i in range(1,101):
        if(i %3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif(i % 5 == 0):
            print("Bizz")
        elif(i % 3 == 0):
            print("Fuzz")
        else:
            print(i)
fizbuz()


