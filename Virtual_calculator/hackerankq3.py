s=["ABC","BCD","EFG","DCB"]
d={}
d1={}
ans=[]
for pat in s:
    key=""
    for i in range(len(pat)-1):
        dif=ord(pat[i+1])-ord(pat[i])
        key+=str(dif)
    if key not in d:
        d[key]=0
    d[key]+=1
    d1[key]=pat
for k in d:
    if d[k]==1:
        print(d1[k])
