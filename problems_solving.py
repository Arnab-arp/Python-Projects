def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
    return


def two_sum(nums, target):
    num_indices = {}
    for index, num in enumerate(nums):
        difference = target - num
        if difference in num_indices:
            return [num_indices[difference], index]
        num_indices[num] = index
    return None


print(two_sum([2, 7, 11, 15], 9))
