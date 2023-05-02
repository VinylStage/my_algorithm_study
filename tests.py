import math

# '''dictionary'''

# dict_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
#             'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

# s = "one4seveneight"


# def solution1(s):
#     for k, v in dict_num.items():
#         s = s.replace(k, str(v))
#     return int(s)


# '''list and enumerate'''

# list_num = ['zero', 'one', 'two', 'three', 'four',
#             'five', 'six', 'seven', 'eight', 'nine']


# def solution2(s):
#     for i, n in enumerate(list_num):
#         s = s.replace(n, str(i))
#     return int(s)

# 두 자연수 n, m
# 최대공약수 g
# 최소 공배수 l

# a = n // g
# n = g * a
# b = m // g
# m = g * b
# l = g * a * b
# answer = []
# n = 3
# m = 12
# if n % m == 0:
#     answer.append(m)
# elif m % n == 0:
#     answer.append(n)
# else:
#     answer.append(0)
# g = answer[0]
# a = n // g
# b = m // g
# l = g * a * b
# answer.append(l)
# if
# print(answer)


# 두 자연수 n, m
# 최대공약수 gcd
# 최소 공배수 lcm

# a = n // gcd
# n = gcd * a
# b = m // gcd
# m = gcd * b
# lcm = gcd * a * b

# import math

# n = 3
# m = 12

# gcd = math.gcd(n, m)
# a = n // gcd
# b = m // gcd
# lcm = gcd * a * b

# arr1 = [[1, 2], [2, 3]]
# arr2 = [[3, 4], [5, 6]]

# '''행렬의 덧셈'''

# '''zip사용'''


# def solution1(arr1, arr2):
#     answer = [[x+y for x, y in zip(i, j)]for i, j in zip(arr1, arr2)]
#     return answer


# '''for문'''


# def solutio2(arr1, arr2):
#     for i in range(len(arr1)):
#         for j in range(len(arr2[0])):
#             arr1[i][j] += arr2[i][j]
#     return arr1


# print(solutio2(arr1, arr2))

# '''list comprehension 변환'''


# def solution3(arr1, arr2):
#     answer = [[arr1[i][j] + arr2[i][j]
#                for j in range(len(arr1[0]))] for i in range(len(arr1))]
#     return answer


# '''short'''


# def sumMatrix(arr1, arr2):
#     return [list(map(sum, zip(*x))) for x in zip(arr1, arr2)]


# height = input()
# name = input()
# weight = input()
# info = [name, height, weight]
# for i, ifo in range(6), info:
#     print(i, ifo)

# a = [3, 4]
# b = [5, 6]
# for x, y in zip(a, b):
#     print(x, y)


# for i in zip(arr1, arr2):
#     print(i)
# for i in arr1:
#     for j in arr2:
#         print(f'this is i{i}and this is j{j}')
# for x in zip(arr1, arr2):
#     print([list(map(sum, zip(*x))) for x in zip(arr1, arr2)])

# 백준 커트라인

# n, k = map(int, input().split())
# a = input().split()
# print(sorted(map(int, a), reverse=True)[k-1])


# 프로그래머스 나머지가 1이 되는 수 찾기

# n = 10

"""정답"""

# def measure(n):
#     answer = []
#     for i in range(1, n+1):
#         if n % i == 1:
#             answer.append(i)
#     return answer

"""숏"""

# def measure_short(n):
#     return [i for i in range(1, n+1) if n % i == 1][0]


# 백준 영수증

"""정답"""

# total = int(input())
# n = int(input())
# total_cost = 0
# for i in range(n):
#     p, c = map(int, input().split())
#     total_cost += p*c
# if total_cost == total:
#     print('Yes')
# else:
#     print('No')


"""리스트컴프리헨션 사용"""

# total = int(input())
# types = int(input())
# total_cost = sum([int(a)*int(b)
#                  for a, b in [input().split() for _ in range(types)]])
# print("Yes" if total_cost == total else "No")

# string1 = int('0b1100000010101100', 2)
# string2 = int('0b1011011110010001', 2)
# string3 = int('0b1101010101110100', 2)
# s = chr(string1)
# r = chr(string2)
# h = chr(string3)
# print(s+r+h)


"""백준 행렬의 덧셈"""

# a = [[1, 2, 3], [2, 2, 2], [0, 1, 0]]
# b = [[3, 3, 3], [4, 4, 4], [5, 5, 100]]

# for n in range(len(a)):
#     for i, j in zip(a, b):
#         print(i, j)


"""프로그래머스 피자 나눠 먹기(2)"""

# a = n // g
# b = 6 // g
# l = g*a*b

# n = 4


# def solution(n):
#     g = math.gcd(n, 6)
#     return g*(n//g)*(6//g) // 6


# print(solution(n))

"""백준 팰린드롬인지 확인하기"""

# 비효율적으로 보임
# a = str(input())
# print(1 if ''.join(list(reversed(a))) == a else 0)

# 슬라이싱 사용
# a = str(input())
# print(1 if a[::-1] == a else 0)

# 미친사람코드
# a=input();print(+(a[::-1]==a))


"""크레인 인형뽑기 게임"""

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
temp = []
answers = 0

for m in moves:
    for b, c in enumerate(board):
        if board[b][m - 1] == 0:
            pass
        elif board[b][m - 1] != 0:
            temp.append(board[b][m - 1])
            board[b][m - 1] = 0
            break

print(board)
print(temp)

"""꼬리 문자열"""

# str_list = ["abc", "def", "ghi"]
# ex = 'ef'

"""answer"""

# def solution(str_list, ex):
#     answer = []
#     for i in str_list:
#         if ex not in i:
#             answer.append(i)
#     return ''.join(answer)`

"""List Comprehensions"""

# def solution(str_list, ex):
#     return ''.join([i for i in str_list if ex not in i])

"""Lambda Comprehensions"""

# def solution(str_list, ex):
#     return ''.join(filter(lambda x: ex not in x, str_list))
