N=int(input())
X=list(map(int, input().split()))
avg=sum(X)/len(X) # 성적 리스트의 평균값
T=[]
for i in range(N):
    if(X[i]>=avg):
        T.append(X[i])
T2=sorted(T)
print(round(avg), X.index(T2[0])+1)
# 굳이 이렇게 어렵게 짠 이유가 뭘까........
