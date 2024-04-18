N=int(input()) #참여자
res=[] #상금 리스트
for i in range(N):
    X=list(map(int, input().split()))
    if(X[0]==X[1]==X[2]): #같은 눈 세 개
        res.append(10000+X[0]*1000)
    elif(X[0]!=X[1]!= X[2]): # 모두 다를 때
        res.append(max(X)*100)
    elif(X[0]==X[1]!=X[2]): #같은 눈 두 개
        res.append(1000+X[0]*100)
    elif(X[1]==X[2]!=X[0]): #같은 눈 두 개
        res.append(1000+X[1]*100)
    elif(X[0]==X[2]!=X[1]): #같은 눈 두 개
        res.append(1000+X[0]*100)
print(max(res))
