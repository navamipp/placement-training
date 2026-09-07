n1=int(input())
n2=int(input())
arr1=[0]*n1
arr2=[0]*n2
for i in range(n1):
    arr1[i]=int(input())
for i in range(n2):
    arr2[i]=int(input())
new=arr1+arr2
a=set(new)
new=list(a)
p=0
if len(new)%2==0:
    k=len(new)//2
    p=(new[k-1]+new[k])/2
else:
    p=new[len(new)//2]
print(p)
    

    
