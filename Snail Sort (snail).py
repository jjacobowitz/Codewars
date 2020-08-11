"""
Snail Sort

Given an n x n array, return the array elements arranged from outermost 
elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next 
array consecutively:
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest; 
the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an 
array [[]].
"""
import numpy as np

# Original solution without numpy
# def snail(snail_map):
#     steps = 2*len(snail_map) - 1
#     snail = []
#     while True:
#         # top; right to left
#         if steps != 0:
#             snail.extend(snail_map[0])
#             snail_map.remove(snail_map[0])
#             steps -= 1
#         else:
#             break
        
#         # right; top to bottom        
#         if steps != 0:
#             for i in range(0, len(snail_map)):
#                 snail.append(snail_map[i].pop(-1))
#             steps -= 1
#         else:
#             break
        
#         # bottom; left to right
#         if steps != 0:
#             tmp = snail_map[-1]
#             tmp.reverse()
#             snail.extend(tmp)
#             snail_map.remove(snail_map[-1])
#             steps -= 1
#         else:
#             break

#         # left; bottom to top        
#         if steps != 0:
#             for i in range(len(snail_map)-1, 0, -1):
#                 snail.append(snail_map[i].pop(0))
#             steps -= 1
#         else:
#             break
#     return snail

def snail(snail_map):
    snail = []
    snail_map = np.array(snail_map)
    while True:
        snail.extend(snail_map[0])
        snail_map = np.delete(snail_map, 0, 0)
        if len(snail_map) != 0:
            snail_map = np.rot90(snail_map)
        else:
            return snail


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(array) == [1,2,3,6,9,8,7,4,5])

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print(snail(array) == [1,2,3,4,5,6,7,8,9])

array = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]
print(snail(array) == [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10])

array = [[ 1,  2,  3,  4,  5,  6],
                  [20, 21, 22, 23, 24,  7],
                  [19, 32, 33, 34, 25,  8],
                  [18, 31, 36, 35, 26,  9],
                  [17, 30, 29, 28, 27, 10],
                  [16, 15, 14, 13, 12, 11]]
print(snail(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 
                       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                       31, 32, 33, 34, 35, 36])