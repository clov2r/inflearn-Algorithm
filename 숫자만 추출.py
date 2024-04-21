import re
X=input() #문자열 입력
num=re.sub(r'[^0-9]', '', X) #문자와 숫자가 섞여진 문자열이 주어졌을 때 숫자만 추출할 수 있도록 만들어줌
num=int(num) # 자연수 만들어주기
cnt=0 #약수의 개수 카운팅하는 변수
for i in range(1, num+1): # 약수의 개수를 세기 위해 반복문 생성
    if(num%i==0):
        cnt+=1
print(num)
print(cnt)
