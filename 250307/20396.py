# 20396. 돌 뒤집기 게임1
# 15:33~39
# 16:06~15
# 16:44~59


# 펜, 연습지 지참

'''
문제
i번째부터 j개의 돌을
i번째 돌의 색으로 바꿔놓는다
가능한 돌에 대해서만 진행
'''

# 자연어 n번째
# 첫 줄에 게임의 개수 T
# 다음 줄부터 게임별로
    # 첫 줄에 N, M
    # 다음 줄에 N개 돌의 초기상태
# 이후 M개의 줄에 걸쳐 i, j...?
    # 이거 어케하죠
    # m개 줄이니까 반복...

t = int(input())

for games in (1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    for i, j in range(m):
        i, j = map(int(input().split()))

    # i번째: i-1 위치
    # i-1 찾고 i-1의 값을 i+j-1까지 넣기
    # 근데 그 과정을 m번 반복
    # 인덱스 범위 설정

    if i+j-1 < n-1:
        


