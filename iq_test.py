"""
IQ Test

Bob is preparing to pass IQ test. The most frequent task in this test is to 
find out which one of the given numbers differs from the others. Bob observed 
that one number usually differs from the others in evenness. Help Bob — to 
check his answers, he needs a program that among the given numbers finds one 
that is different in evenness, and return a position of this number.

Keep in mind that your task is to help Bob solve a real IQ test, which means 
indexes of the elements start from 1 (not 0)
"""

def iq_test(numbers):
    even = [0, -1]
    odd = [0, -1]
    numbers_split = numbers.split(' ')
    for index, i in enumerate(numbers_split):
        if int(i)%2 == 0:
            even[0] += 1
            even[1] = index + 1
        else:
            odd[0] += 1
            odd[1] = index + 1
    if even[0] < 2:
        return even[1]
    else:
        return odd[1]


print(iq_test("2 4 7 8 10")) # 3 // Third number is odd, while the rest of the numbers are even

print(iq_test("1 2 1 1")) # 2 // Second number is even, while the rest of the numbers are odd