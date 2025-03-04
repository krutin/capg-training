# file  = open('sample.txt','r')
# content = file.read()
# print(content)
# file.close()

# file = open("example.txt", "w")
# file.write("Hello, World!")
# file.close()

# file = open('example.txt', 'a')
# file.write("This will add this line")
# file.close()

# # creating file exclusively ,x mode
# try:
#     file = open("newfile.txt", "x")
#     file.write("exclusive file creation.\n")
#     file.close()
# except FileExistsError:
#     print("file alredy exists")

#     # with method

# with open("sample.txt","w") as file:
#     file.write("line 1\nline 1\nline 3 \n")

# with open('sample.txt',"r") as file:
#     content = file.read()
#     print(content)


# with open('sample.txt',"r") as file:
#     print(file.readline())


with open('sample.txt',"r") as file:
    lines = file.readlines()
    print(lines)


with open('sample.txt',"w") as file:
    file.write("hello, Python!\n")






