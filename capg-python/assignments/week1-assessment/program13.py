
def pal(st):
    return st == st[::-1]


inp = ''
while(inp != 'q'):
    inp = input("enter a string to check palindrome and q to quit: ")
    print(pal(inp))

