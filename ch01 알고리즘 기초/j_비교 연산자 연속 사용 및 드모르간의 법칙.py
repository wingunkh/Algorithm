# 2자리 양수 (10~99) 입력 받기

print("2자리 양수를 입력하세요.: ")

while True:
    no = int(input("값을 입력하세요.: "))
    # if(10 <= no <= 99): # 연속으로 사용한 비교 연산자는 and 결합으로 취급한다.
    if not(no < 10 or no > 99): # 드모르간의 법칙 적용
        break

print(f"입력받은 양수는 {no}입니다.")
