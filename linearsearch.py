lst = []
num = int(input("enter the size of the list:"))
for i in range(num):
    number = int(input("Enter the numbers to the list :"))
    lst.append(number)

x = int(input("Enter the number to search :"))

found = False

for i in range(len(lst)):
    if lst[i]==x:
        found=True
        print("\n %d found at position %d\n"%(x,i))
        break
if not found:
    print(" %d not found" % x)
    
