dict1={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
val=input()

arr1=[""]
str1=""
if val=="":
    arr1=[]
    print(arr1)
else:
    i=0
    while i<len(val):
        str1=dict1[val[i]]
        arr1=[x+y for x in arr1 for y in str1]
        i+=1
    print(arr1)
