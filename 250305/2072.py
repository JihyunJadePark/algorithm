t = int(input())


for testcase in range(1, t+1):
    numbers = list(map(int, input().split()))

    sum = 0

    for i in numbers:
        if i % 2 == 1:
            sum += i

    answer = sum

    print(f'#{testcase} {answer}')