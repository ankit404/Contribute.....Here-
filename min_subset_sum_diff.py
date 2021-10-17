"""
Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.

Example 1: 
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.

Example 2: 
Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.

Example 3: 
Input: {1, 3, 100, 4}
Output: 92
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.
"""

import functools

def partition(num):
    cache = {}
    def partition_recursive(s1, s2, i):
        nonlocal num
        nonlocal cache

        if i == len(num):
            return abs(s1 - s2)

        if (i, s1) not in cache:
            diff1 = partition_recursive(s1+num[i], s2, i+1)
            diff2 = partition_recursive(s1, s2+num[i], i+1)
            cache[i, s1] = min(diff1, diff2)
        return cache[i, s1]


    return partition_recursive(0, 0, 0)


if __name__ == "__main__":
    print(partition([1, 2, 3, 9]))
    print(partition([1, 2, 7, 1, 5]))
    print(partition([1, 3, 100, 4]))
    print(partition(list(range(500))))