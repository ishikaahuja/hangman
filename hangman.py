word='scientist'
disp=[]
count=0
cha=9
ip=list(word)
n=len(ip)
for i in range(0,len(ip)):
    disp.append('_')
    count=count+1
while(count>0 and cha>0):
    r=input()
    flag=0
    for i in range(0,len(ip)):
        if(ip[i]==r):
            count=count-1
            #print(count)
            disp[i]=r
            flag=1
    if(flag==0):
        cha=cha-1
    print(disp)
if(count==0):
    print("success")
        
