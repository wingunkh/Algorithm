# 가로, 세로의 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기

area = int(input("직사각형의 넓이를 입력하세요.: "))

for i in range(1, area+1):
    if i*i > area: break # i가 가장 긴변의 길이가 되면 반복문 종료
    if area % i : continue # area가 i로 나누어 떨어지지 않으면 다음 반복문으로 이동 
    print(f"{i} * {area // i}")
