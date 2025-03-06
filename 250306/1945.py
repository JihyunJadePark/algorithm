# 1945. 간단한 소인수 분해

t = int(input())

for testcase in range(1, 1+t):
    N = int(input())

    # 2, 3, 5, 7, 11로 나누어지는지 각각 확인
    # 안 나눠지면 3으로
    # 안 나눠지면 5로
    # 안 나눠지면...더보기
    # 11까지 하고 종료

    # if N // 2 = 0:
    # 아니지 이건 지수니까 다르지
    # 어케다른데...
    # 2로 계속 나누기 ㅇㅇㅇ
    # 2로 나눈 몫 & 나머지 구하고
    # 나머지에 대해, 다음 숫자로 가서 몫 구하고... 반복
    # 다음 숫자로 가는 걸 어케 구현하지
    # 어케하죠
    # 함수???????

    powerof2 = 0
    powerof3 = 0
    powerof5 = 0
    powerof7 = 0
    powerof11 = 0

    yettocalculate = 0

    powerof2 = N // 2
    if N % 2 != 0:
        yettocalculate = N - (2 * powerof2)
        yettocalculate // 3
            if (N - yettocalculate) % 3 != 0:
            yettocalculate = N - (2 * powerof2) // 3

            if N % 5 != 0:
                powerof5 = N//5
                if N%7 != 0:
                    powerof7 = N//7
                    if N%11 != 0:
                        powerof11 = N//11











    answer =

    print(f'#{testcase} {answer}')