sum_row, sum_col = [-1,1,0,0], [0,0,-1,1]
mul_row, mul_col = [-1, -1, 1, 1], [-1, 1, -1, 1]

def plus_direction(flies, row, col):
    tmp_sum = flies[row][col]
    for i in range(1, M):
        for j in range(4):
            neighboring_row = row + (sum_row[j] * i)
            neighboring_col = col + (sum_col[j] * i)
            if 0 <= neighboring_row < N and 0 <= neighboring_col < N:
                tmp_sum += flies[neighboring_row][neighboring_col]

    return tmp_sum

def multiple_direction(flies, row, col):
    tmp_sum = flies[row][col]
    for i in range(1, M):
        for j in range(4):
            neighboring_row = row + (mul_row[j] * i)
            neighboring_col = col + (mul_col[j] * i)
            if 0 <= neighboring_row < N and 0 <= neighboring_col < N:
                tmp_sum += flies[neighboring_row][neighboring_col]
    return tmp_sum

T = int(input())

for test_count in range(1, T+1):
    N, M = map(int, input().split())

    flies = list()
    for i in range(N):
        numbers = list(map(int, input().split()))
        flies.append(numbers)

    max_hit = 0
    sum_hit = 0
    for row_index in range(N):
        for col_index in range(N):
            plus_sum = plus_direction(flies,row_index, col_index)
            mul_sum = multiple_direction(flies, row_index, col_index)
            sum_hit = max(plus_sum, mul_sum)

            if max_hit < sum_hit:
                max_hit = sum_hit

    print(f'#{test_count} {max_hit}')