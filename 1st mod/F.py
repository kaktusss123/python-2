# n = input()
# beg = int(n[0]) + int(n[1]) + int(n[2])
# end = int(n[3]) + int(n[4]) + int(n[5])
# if (beg == end):
#     print(n)
# elif (beg < end):
#     difference = end - beg
#     if (difference < int(n[5])):
#         print(n[:5] + str(int(n[5]) - difference))
#     elif (difference < int(n[5]) + int(n[4])):
#         difference -= int(n[5])
#         print(n[:4] + str(int(n[4]) - difference) + '0')
#     else:
#         difference -= (int(n[5]) + int(n[4]))
#         print(n[:3] + str(int(n[3]) - difference) + '00')
# else:
#     difference = beg - end
#     if (difference < 9 - int(n[5])):
#         print(n[:5] + str(int(n[5]) + difference))
#     elif (difference < 18 - (int(n[5]) + int(n[4]))):
#

print(3 // 2)
n = input()
print(n[3:6])