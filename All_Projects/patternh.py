# h pattern
for i in range(7):
    for j in range(5):
        if (i==3 or j==0 or j==4):
            print("*",end="")
        else:
            print(end=" ")
    print()
