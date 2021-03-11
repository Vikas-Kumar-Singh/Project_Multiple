N=int(input())
A=[]
B=[]
x=int(input())
y=int(input())
A.append(x)
B.append(y)
i=2
while i>0:
    if max(A)>=N:
        break
    else:
        A.append(x*i)
        i+=1
i=2
while i>0:
    if max(B)>=N:
        break
    else:
        B.append(y*i)
        i+=1
print(A)
print(B)
##pairs in list A whosesum is equal to T
t=int(input())
l=0
h=len(B)-1
while l<h:
    if A[l]+B[h]==t:
        print(A[l],B[h])
        l=l+1
        h=h+1
    elif A[l]+B[h]>t:
        h=h-1
    else:
        l=l+1
