N=int(input())
X=[list(map(int, input().split())) for _ in range(N)]
m_num=-2147000000 #최댓값
for i in range(N):
    sum1=sum2=0
    for j in range(N):
        sum1+=X[i][j]
        sum2+=X[j][i]
    if sum1>m_num:
        m_num=sum1
    if sum2>m_num:
        m_num=sum2
sum1=sum2=0
for i in range(N):
    sum1+=X[i][i]
    sum2+=X[i][N-i-1]
    if sum1>m_num:
        m_num=sum1
    if sum2>m_num:
        m_num=sum2
print(m_num)
