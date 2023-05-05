# d = [1, 3, 2, 5, 4]
# budget = 9


# def solution(d, budget):
#     answer = 0

#     return answer
# m = 0
# while m < budget:
#     for i in sorted(d):
#         i += i
#         m += i
#         print(i)
# my_string = "He11oWor1d"
# overwrite_string = "lloWorl"
# s = 2
# o = len(overwrite_string)
# m = len(my_string[s:])
# if m > o:
#     print(my_string[:s] + overwrite_string + my_string[o-m:])
# else:
#     print(my_string[:s] + overwrite_string)


# 배열 조각하기
# arr = [0, 1, 2, 3, 4, 5]
# query = [4, 1, 2]


# def solution(arr, query):
#     answer = []
#     return answer

# for i in range(len(query)):
#     if i % 2 == 0:
#         arr = arr[:query[i]+1]
#     elif i % 2 != 0:
#         arr = arr[query[i]:]
# print(arr)

# 백준 문자열
# n = int(input())
# r = []
# for i in range(n):
#     a = input()
#     r.append(a[0]+a[-1:])
# print('\n'.join(r))


# arr = [1, 1, 3, 3, 0, 1, 1]
# for ar in arr:
#     if ar == arr[0]:
#         print(ar)
#         arr.pop(0)
#         print(arr)
#     else:
#         pass
# print(arr)


# 프로그래머스 최소직사각형

# sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]


# def solution(sizes):
#     # 가로와 세로를 비교해서 세로길이가 가로길이보다 크면 돌리기
#     for i in range(len(sizes)):
#         if sizes[i][0] < sizes[i][1]:
#             sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
#     a = max(sizes, key=lambda x: x[0])[0]  # 가장 큰 가로값 반환
#     b = max(sizes, key=lambda x: x[1])[1]  # 가장 큰 세로값 반환
#     return a*b


# 백준 상수

# a, b = map(int, input().split())

# c = ''.join(list(reversed(str(a))))
# d = ''.join(list(reversed(str(b))))
# print(max(c, d))


# 숏코딩
# print(max(input()[::-1].split()))

