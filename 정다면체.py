from collections import Counter
N, M=map(int, input().split())
X=[] #N의 길이인 리스트
Y=[] #M의 길이인 리스트
Z=[] #N+M의 합을 나타내는 리스트
for i in range(N): #N면체의 주사위 숫자 넣기
    X.append(i+1)
for j in range(M): #M면체의 주사위 숫자 넣기
    Y.append(j+1)
if(M>N):
    for T in range(N):
        for Q in range(M):
            Z.append(X[T]+Y[Q])
else:
    for T in range(M):
        for Q in range(N):
            Z.append(Y[T]+X[Q])
            
frequency = Counter(Z)  # 빈도수 계산
most_common = frequency.most_common()  # 빈도수가 높은 순으로 정렬된 튜플 리스트 생성

# 가장 빈도수가 높은 숫자 출력
max_frequency = most_common[0][1]
most_frequent_numbers = [num for num, freq in most_common if freq == max_frequency]

print(*most_frequent_numbers)
