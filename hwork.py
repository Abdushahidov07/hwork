# task1
# def potatoes(a):
#     a = a.lower() 
#     cnt = 0
#     b = 'potato'
#     f = len(b)
    
#     for i in range(len(a) - f + 1):
#         if a[i:i + f] == b:
#             cnt += 1
            
#     return cnt

# print(potatoes(input()))

# task2
# def five(a):
#     cnt = 0
#     for i in a:
#         if i > 5:
#             cnt+=i
#     print(cnt)
# five(list(map(int,input().split())))

# task3

# def stuttering(a):
#     print(f"{a[0]}{a[1]}... {a[0]}{a[1]}... {a}?")
# stuttering(input())

# task4

# def discard(a, b):
#     print(a-(a//100*b))
# discard(int(input()),int(input()))

# task5

# def end_corona(a, b, c):
#     if a <= b:
#         return 0

#     days = 0
#     while c > 0:
#         c -= (a - b)
#         days += 1
#     print(days)
# end_corona(int(input()),int(input()),int(input()))
