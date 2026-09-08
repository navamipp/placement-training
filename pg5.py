integers=list(map(int,input().split()))

if len(integers)==1:
    str1=""
    n=integers[0]
    count=1
    coo=1
    while(n>1):
        str1+=str(n)
        if n%2==0:
            if count%2!=0:
                str1+="//"
                count+=1
            elif count%2==0:
                str1+="*"
                count+=1
        if n%2!=0:
            if count%2!=0:
                str1+="-"
                coo+=1
            elif count%2==0:
                str1+="+"
                coo+=1
        n=n-1
    str1+=str(n)
    print(str1)
    print(eval(str1))
elif len(integers)==2:
    f=integers[0]
    l=integers[1]
    ev=1
    od=1
    str2=""
    while(f>l):
        str2+=str(f)
        if f%2==0:
            if ev%2!=0:
                str2+="//"
                ev+=1
            elif ev%2==0:
                str2+="*"
                ev+=1
        if f%2!=0:
            if ev%2!=0:
                str2+="-"
                od+=1
            elif ev%2==0:
                str2+="+"
                od+=1
        f=f-1
    str2+=str(f)
    print(str2)
    print(eval(str2))
        
    
            
            
        
