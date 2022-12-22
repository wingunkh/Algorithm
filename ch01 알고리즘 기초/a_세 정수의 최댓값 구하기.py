# 세 정수를 입력받아 최댓값 구하기

print("세 정수의 최댓값을 구합니다.")
a = int(input("정수 a의 값을 입력하세요.: ")) # input() 함수는 키보드로 문자열을 입력받아 반환하는 함수이다.
b = int(input("정수 b의 값을 입력하세요.: "))
c = int(input("정수 c의 값을 입력하세요.: "))

maximum = a
if b > maximum: maximum = b # 콜론(:) 이전 부분은 '헤더', 이후 부분은 '스위트'
if c > maximum: maximum = c 

print(f"최댓값은 {maximum}입니다.")
