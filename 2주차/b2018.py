
# N = int(input())

# t_l = [x for x in range(1, N+1)]

# l = [0]
# sumi = 0
# for i in t_l:
#     sumi+=i
#     l.append(sumi)

# cnt = 0
# for i in range(0, N+1):
#     for j in range(0, i):
#         if l[i]-l[j] == N:
#             cnt+=1

# print(cnt)
##### 위에 코드 메모리 초과,, 찾아보니 투포인터 쓰라함

N = int(input())
start, end = 1, 1
cnt = 0
sum = 1

while start < N//2+1:
    if sum < N:
        end += 1
        sum += end
    elif sum > N:
        sum -= start
        start += 1
    else:
        cnt += 1
        end += 1
        sum -= start
        sum += end
        start += 1


print(cnt + 1)