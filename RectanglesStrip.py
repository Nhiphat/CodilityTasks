# There are N rectangles numbered from 0 to N-1. The K-th rectangle has size A[K] × B[K].
#
# We want to arrange as many rectangles as possible into a strip. The rectangles can be arranged into a strip if they all share a side of the same length (which becomes the height of the strip). Note that rectangles can be rotated.
#
# Write a function:
#
# def solution(A, B)
#
# that, given two arrays A and B of N integers each, returns the maximum number of rectangles that can be arranged into a strip.
#
# Examples:
#
# 1. Given A = [2, 3, 2, 3, 5] and B = [3, 4, 2, 4, 2], the function should return 3. Choosing the 0th, 2nd and 4th rectangles we can obtain the following strip of height 2 (note that the 0th rectangle was rotated):

A = [2, 3, 2, 3, 5]
B = [3, 4, 2, 4, 2]
C = [2, 3, 1, 3]
D = [2, 3, 1, 3]

def solution(A, B):
    countMax = 0
    for i in range(len(A)):
        count = 0
        k = 0
        piv = 0
        for j in range(len(A)):
            if i != j:
                if k == 0:
                    if A[i] == A[j] or A[i] == B[j]:
                        piv = A[i]
                        k += 1
                        count += 1
                    else:
                        if B[i] == A[j] or B[i] == B[j]:
                            piv = B[i]
                            k += 1
                            count += 1
                if piv == A[j] or piv == B[j]:
                    count += 1
        if count > countMax:
            countMax = count
    return countMax


print(solution(A, B))
print(solution(C, D))
