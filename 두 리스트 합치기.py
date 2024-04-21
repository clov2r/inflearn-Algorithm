A=int(input()) #리스트의 크기
A_list=list(map(int, input().split())) #리스트 생성
B=int(input()) #리스트의 크기
B_list=list(map(int, input().split())) #리스트 생성ㅇ
C=A_list+B_list #리스트 합치기
C2=sorted(C) #오름차순
print(*C2) #출력
