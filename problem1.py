pwd= input()
str1=""
str2=""
cnt0=0
cnt1=0
for i in range(0,len(pwd)):
    if i<2:
        str1 += pwd[i]
    else:
        str2+=pwd[i]

for j in str2:
    if j == "0":
        cnt0+=1
    else:
        cnt1+=1

if str1[0] == str1[1]:
    print(min(cnt0,cnt1))
else:
    print(min(cnt0,cnt1)+1)

