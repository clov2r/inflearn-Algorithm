T=int(input()) #testcase
for i in range(1, T+1): #testcase만큼 반복
    N, S, E, K=map(int, input().split()) 
    N_list=list(map(int, input().split())) #N개의 숫자 리스트
    N_list2=N_list[S-1:E] #S번째 E번째까지의 숫자
    N_list3=sorted(N_list2) #오름차순으로 정렬
    print('#%d'%i, N_list3[K-1]) #K번째로 나타나는 숫자 출력
