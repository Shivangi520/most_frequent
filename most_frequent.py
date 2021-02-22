def most_frequent(s):
    s=s.lower()
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    print(sorted(dic.items(),key=lambda x: (-x[1],x[0])))

s=input("Enter the string:")
most_frequent(s)
