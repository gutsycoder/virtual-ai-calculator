s=input()
s=s.upper()
remove="AWS"
k=s.find(remove)

while k!=-1:
    s=s[:k]+s[k+3:]
    k=s.find(remove)
if s!="":
    print(s)
else:
    print(-1)
