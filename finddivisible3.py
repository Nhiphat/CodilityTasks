def hello():
    print('hello')


hello()

S = [0, 2, 2]


def checkDivisibleThree(s):
    sum = 0
    for i in range(0, 3):
        sum = sum + s[i]
    if sum % 3 == 0:
        return True
    return False


def count(s):
    count = 0
    for i in range(0, 3):
        for j in range(0, 10):
            s1 = s.copy()
            if s1[i] == j:
                continue
            s1[i] = j
            check = checkDivisibleThree(s1)
            if check:
                print(s1)
                count += 1

    return count


print(count(S))
