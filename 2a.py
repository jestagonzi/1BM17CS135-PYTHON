def lin_search(lis):
    a = int(input("Enter the number to search: "))
    for i in lis:
        if a in lis:
            print("The element is present at: ",lis.index(a)+1)
            break;

        elif i==len(lis)-1 and a not in lis:
            print("The element is not present !")
n=int(input("Enter the number of elements:"))
lis=[]
for i in range(n):
    x = int(input("Enter the numbers: "))
    lis.append(x)
lin_search(lis)
