n = int(input())

# def fibb(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     return fibb(n-1) + fibb(n-2)

# print(fibb(n))

## 위 코드는 시간 초과가 남

r = 0
fibb = [0,1]
for i in range(2, n+1):
    fibb.append(fibb[-1]+fibb[-2])

print(fibb[-1])