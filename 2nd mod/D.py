# import time
#
# i = int(input())
# start = time.time()
# simple = [2]
# for k in range(3, 5000000):
#     is_simple = True
#     for d in simple:
#         if k % d == 0:
#             is_simple = False
#             break
#     if is_simple:
#         simple.append(k)
#         if len(simple) > i:
#             break
# print(simple[i-1])
# print(time.time() - start)

#5.389760255813599

#8.290905952453613
#7.551726341247559

import time

start = time.time()
x = int(input())
simple = [2]
for i in range(3, 5000000, 2):
    is_simple = True
    for d in simple:
        if (i % d == 0):
            is_simple = False
            break
    if is_simple:
        simple.append(i)
        if (len(simple) > x):
            print(i)
            break
print(time.time() - start)
