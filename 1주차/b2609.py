import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))

########유클리드 호제법 사용########

# def gcd(m, n):  #최소공배수
#     if n == 0:
#         return m
#     elif m % n == 0:
#         return n
#     return gcd(n, m%n)

# def lcm(m, n):  #최대공약수
#     return (m * n) // gcd(n, m)

# print(gcd(a,b))
# print(lcm(a,b))

