name_1=input("enter your first name   : " ).strip().lower()
n_1=[a for a in name_1 if a!=' ']
name_2=input("enter your second name  : " ).strip().lower()
n_2=[b for b in name_2 if b!=' ']
t=len(n_1)+len(n_2)
for i in range(0,len(n_1)):
    for j in  range(0,len(n_2)):
        if n_1[i]!='*' and n_1[i]==n_2[j]:
            t=t-2
            n_1[i],n_2[j]='*','*'
r=['Friendship','Love','Affection','Married','Enemy','Sister and Br0ther ']
while len(r)>=2:
    a=t%len(r)-1
    if a<0:
        ri=r[:a]
        r=ri
    else:
        ri=r[a+1:]
        le=r[:a]
        r=ri+le
print(name_1 ,'and ',name_2, r[0])
