N=int(input()) #N으로 입력
for i in range(N): #입력받은 만큼 회전
    X=input().lower() #N번만큼 문자열 데이터를 받음 >대신 대소문자 구분 없음 그래서 lower() 사용
    if(X[::-1]==X): #회문 문자열인지 아닌지 확인하는 조건문
        print('#%d'%(i+1), "YES")
    else:
        print('#%d'%(i+1), "NO")
