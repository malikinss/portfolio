'''
TODO:
        A combination of n elements of k is a subset of these n elements of size k.

        Two combinations are called different if one of the combinations contains an element that does not contain the other.

        The number of combinations from n to k is the number of different combinations from n to k. 
        
        Let's denote this number as C(n, k).

EXAMPLE:

        Let n = 3, i.e. there are three elements (1, 2, 3).
        Let k = 2.
        All different combinations of 3 elements of 2: 
            (1, 2), (1, 3), (2, 3).
        There are three different combinations, so C(3, 2) = 3.

        It is easy to understand that C(n, 0) = 1, since there is only one way to choose 0 from n elements, namely, to choose nothing.

        It is also easy to understand that if k > n, then C(n, k) = 0, since it is impossible, for example, to choose five from three elements.

        To calculate C(n, k) in other cases, use the following  recurrence formula:
            C(n, k) = C(n - 1, k) + C(n - 1, k - 1).

        Implement a program that, given n and k, calculates C(n, k).

        Your program is given a string as input containing two integers n and k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).

        Your program should print a single number: C(n, k).
'''
def get_c(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return (get_c(n-1, k) + get_c(n-1, k-1))

n, k = map(int, input().split())

print(get_c(n, k))