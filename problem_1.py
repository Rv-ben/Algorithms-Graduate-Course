"""Let  X(1..n)  and  Y(1..n)  contain  two  lists  of  n  integers, 
each  sorted  in  nondecreasing order.  Give  the best (worst-case complexity)
algorithm that you  can think  for finding: 
(a) the largest integer  of all  2n combined  elements.
(b) the second  largest integer  of all  2n  combined  elements.
(c) the median  (or  the nthsmallest  integer)  of all  2n  combined  elements
"""

from random import randint

def find_kth_largest_int(X, Y, N, K):
    x_index = y_index = N - 1
    comparisons = 0

    while not comparisons == K:
        if X[x_index] >= Y[y_index]:
            x_index -= 1
        else:
            y_index -= 1
        
        comparisons += 1
        if comparisons == K:
            return X[x_index + 1] if y_index > x_index else Y[y_index + 1]


if __name__ == "__main__":
    N = randint(4, 7)
    X = [i for i in range(0, N)]
    Y = [i for i in range(0, N)]
    X.sort()
    Y.sort()

    print(N)
    print(X)
    print(Y)
    print(find_kth_largest_int(X, Y, N, 2))