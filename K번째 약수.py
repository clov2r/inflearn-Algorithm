# K번째 약수
N, K =map(int, input().split()) #N, K 입력 받음
X=[] # X 리스트 생성 > 약수를 한 곳으로 모으기 위함
for i in range(1, N+1): #입력받은 숫자만큼 반복
    if(N%i==0): #약수 생성기
        X.append(i) # 빈 리스트에 값 쑤셔 넣기
    X2=sorted(X) #문제에서 K번째로 작은 수 출력이라고 해서 sorted로 X 값들을 정리
if(len(X2)<K): #N의 약수의 개수가 K보다 적어서 K번째 약수가 존재하지 않을 경우도 생각
    print(-1)
else:
    print(X2[K-1])
