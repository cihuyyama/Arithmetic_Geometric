a=eval(input("Input the first number :"))
r=eval(input("Input the Ratio :"))
n=int(input("Input number of iteraion :"))
arr=[a]
for i in range(n):
    rat=r
    rat=rat**(i+1)
    geometric=a*rat
    arr.append(geometric)

sum=0

for i in range (n):
    if(i<n-1):
        print(arr[i],",", end="")
        sum=sum+arr[i]
    else:
        print(arr[i])
        sum=sum+arr[i]

print("Total : ",sum)

