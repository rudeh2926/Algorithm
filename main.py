# import random
#
# x = 4
# y = 4
#
# c = [a for a in range(1, x*y+1)]
# random.shuffle(c)
#
# for i in range(y):
#     for j in range(x):
#         d = c.pop(0)
#         if len(str(d)) == 1:
#             print("0" + str(d), end="  ")
#         else:
#             print(str(d), end="  ")
#     print("")

# from collections import deque
# import sys
#
# n = int(sys.stdin.readline().strip())
# b = deque()
#
# for i in range(n):
#     a = sys.stdin.readline().strip().split()
#     c = lambda x: print(x)
#     if a[0] == 'push':
#         b.append(a[1])
#     elif a[0] == 'pop':
#         c(b.popleft() if b else -1)
#     elif a[0] == 'size':
#         c(len(b))
#     elif a[0] == 'empty':
#         c(1 if not b else 0)
#     elif a[0] == 'front':
#         c(b[0] if b else -1)
#     elif a[0] == 'back':
#         c(b[-1] if b else -1)


# a, b = map(int, input().split())
# c = [i for i in range(1, a + 1)]
#
# d = []
# e = 0
#
# for t in range(a):
#     e += b - 1
#     if e >= len(c):
#         e = e % len(c)
#
#     d.append(str(c.pop(e)))
# print("<", ", ".join(d)[:], ">", sep='')

# from collections import deque
#
# a = int(input())
# b = deque([i for i in range(1, a + 1)])
#
# while (len(b) > 1):
#     b.popleft()
#     c = b.popleft()
#     b.append(c)
#
# print(b[0])

# import heapq
# a = []
# heapq.heappush(a,5)
# heapq.heappush(a,9)
# heapq.heappush(a,3)
# print(a)
# print(heapq.heappop(a))
# print(a)
# print(heapq.heappop(a))

# def solution(participant, completion):
#     a = 0
#     b = {}
#
#     for c in participant:
#         a += hash(c)
#         b[hash(a)] = a
#         if c in b: # 동명이인이 있다면 +1 함
#             b[c] += 1
#         else: # 아니면 그냥 1 추가
#             b[c] = 1
#
#     for c in completion:
#         a -= hash(c)
#         b[c] -= 1
#
#     for c, count in b.items():
#         if count == 1:
#             return c
#
#     return None


# def solution(participant, completion):
#     a = {}
#     b = 0
#     for i in participant:
#         a[hash(i)] = i
#         b += hash(i)
#
#     for j in completion:
#         b -= hash(j)
#
#     return a[b]


# def solution(nums):
#     z = ''
#     a = len(nums)//2
#     b = {}
#     c = list(b)
#     d = len(c)
#
#     if a < d:
#         z = a
#     else:
#         z = d
#     return z

# def solution(nums):
#     answer = 0
#     a = {}
#     for n in nums:
#         a[n] = 1
#     if len(nums) // 2 <= len(a):
#         return len(nums) // 2
#     return len(a)


# def solution(phone_book):
#     a = {}
#     for b in phone_book:
#         a[b] = 1
#
#     for b in phone_book:
#         c = ""
#         for num in b:
#             c += num
#
#             if c in a and c != b:
#                 return False
#
#     return True

# a, b = map(int, input().split())
# m = []
# for i in range(a):
#     m.append(int(input()))
# m = sorted(m, reverse=True)
#
# c = 0
# for i in m:
#     if b==0:
#       break
#     c += b//i
#     b %= i
#
# print(c)

# a = int(input())
# b = list(map(int, input().split()))
#
# b.sort()
# c = 0
#
# for i in range(1, a+1):
#     c += sum(b[0:i])
# print(c)

# a = int(input())
# b = []
# for i in range(a):
#     c, d = map(int, input().split())
#     b.append((c, d))
# b.sort(key=lambda e: (e[1], e[0]))
# w = 0
# ct = 0
# for c, d in b:
#     if c >= w:
#         w = d
#         ct += 1
# print(ct)

# def fib(n):
#     a = [0] * (n + 1)
#     a[1] = a[2] = 1
#     for i in range(3, n + 1):
#         a[i] = a[i - 1] + a[i - 2]
#     return a[n]
#
#
# def fibonacci(n):
#     return n - 2
#
#
# n = int(input())
# print(fib(n), fibonacci(n))

# a = int(input())
#
# b = [0] * (a+1)
# for i in range(2, a+1):
#     b[i] = b[i-1]+1
#     if i % 2 == 0:
#         b[i] = min(b[i], b[i//2]+1)
#     if i % 3 == 0:
#         b[i] = min(b[i], b[i//3]+1)
#
# print(b[a])

# def a(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#
#     a = [0] * (n + 1)
#     a[1] = 1
#     a[2] = 2
#
#     for i in range(3, n + 1):
#         a[i] = a[i - 1] + a[i - 2]
#
#     return a[n]
#
# n = int(input())
# print(a(n))

# a = int(input())
#
# for _ in range(a):
#     n, m = map(int, input().split())
#     b = 0
#
#     for num in range(n, m + 1):
#         b += str(num).count('0')
#
#     print(b)

# from itertools import combinations
#
# # 9번 반복하여 9개의 정수를 a 리스트에 저장
# a = [int(input()) for _ in range(9)]
#
# # a에서 7개의 원소를 뽑아 가능한 모든 조합을 생성
# #  생성된 조합을 b에 하나씩 대입하여 반복문을 수행
# for b in combinations(a, 7):
#     if sum(b) == 100:
#         # 정렬된 조합의 각 숫자를 하나씩 num에 대입하여 반복문을 수행
#         for num in sorted(b):
#             print(num)
#         break

# a, b = map(int, input().split())
# c = list(map(int, input().split()))
# d = []
# for i in range(a):
#     for j in range(i+1, a):
#         for z in range(j+1, a):
#             e = c[i] + c[j] + c[z]
#             if e > b:
#                 continue
#             else:
#                 d.append(e)
# print(max(d))

# while (1):
#     a, b = map(int, input().split())
#
#     if a == 0 and b == 0:
#         break
#
#     if a < b and b % a == 0:
#         print("factor")
#     elif a > b and a % b == 0:
#         print("multiple")
#     else:
#         print("neither")

# a, b = map(int, input().split())
# c = 0
# for i in range(1, a + 1):
#     if str(i).count(str(b)) > 0:
#         if i > 9:
#             c += list(str(i)).count(str(b))
#         else:
#             c += 1
#
# print(c)

a = int(input())
a_list = list(map(int, input().split()))

a_list.sort()

b = int(input())
b_list = list(map(int, input().split()))

for c in b_list:
    left = 0
    right = a - 1
    while left <= right:
        mid = (left + right) // 2
        if c > a_list[mid]:
            left = mid + 1
        elif c < a_list[mid]:
            right = mid - 1
        else:
            left = mid
            right = mid
            break

    if left == mid and right == mid:
        print(1)
    else:
        print(0)




