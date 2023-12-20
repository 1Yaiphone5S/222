with open('17_7038 (1).txt') as f:
    s = [int(x) for x in f]
    n = []
    a = []
    all = []
    for i in range(len(s)-1):
        if (abs(s[i])%10==1 and abs(s[i+1])%10!=1) or (abs(s[i])%10!=1 and abs(s[i+1])%10==1):
            n.append((s[i]+s[i+1])//2)
    for z in range(len(s)-1):
        if ((abs(s[z])%10==1 and abs(s[z+1])%10!=1) or (abs(s[z])%10!=1 and abs(s[z+1])%10==1)) and (s[z]<max(n) and s[z+1]<max(n)):
            a.append(s[z])
            a.append(s[z+1])
    all.append(min(a))




print(len(a)//2, a[a.index(min(a))+1])