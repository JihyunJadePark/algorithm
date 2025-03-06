t = int(input())

for testcase in range(1, t+1):
    arr = list(map(int, input().split()))

    sumofthenumbers = sum(arr)
    average = sumofthenumbers / 10
    answer = round(average)

    print(f'#{testcase} {answer}')