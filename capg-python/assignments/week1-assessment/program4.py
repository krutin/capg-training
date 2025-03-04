def grading():
    name = input("enter students name:")
    print("Enter marks acoording to subject asked out of 100")
    eng = int(input("Enter marks for english:"))
    san = int(input("Enter marks for sanshrith:"))
    mat = int(input("Enter marks for Math:"))
    phy = int(input("Enter marks for physics:"))
    che = int(input("Enter marks for chemestry:"))

    total = eng+san+mat+phy+che
    per = total/5
    if(per>=85):
        grade = 'A'
        print("Student name:",name,"\nTotal:", total, "\nPercentage:",per,"\nGrade:",grade)
    elif(per>=75 and per<85):
        grade = 'B'
        print("Student name:",name,"\nTotal:", total, "\nPercentage:",per,"\nGrade:",grade)
    elif(per>=65 and per<75):
        grade = 'C'
        print("Student name:",name,"\nTotal:", total, "\nPercentage:",per,"\nGrade:",grade)
    elif(per>=55 and per<65):
        grade = 'D'        
        print("Student name:",name,"\nTotal:", total, "\nPercentage:",per,"\nGrade:",grade)
    elif(per<55):
        print("Try again next semester, student",name,"failed")
    
grading()