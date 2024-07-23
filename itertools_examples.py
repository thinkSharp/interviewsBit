from itertools import permutations
from functools import reduce
from collections import ChainMap, defaultdict

def test_permutation():
    S, K = input().split(' ')
    K = int(K)

    perm = permutations(S, K)
    print(perm)

    sorted_permutations = sorted(''.join(p) for p in perm)

    for perm in sorted_permutations:
        print(perm)

def test_chainmap():
    d1 = {'a': 1, 'b':2}
    d2 = {'c': 3, 'd':4}
    d3 = {'e': 5, 'f':6, 'a':7}

    c = ChainMap(d1, d2, d3)

    print(c)

    print(c['a'])
    print(c.values())
    print(c.keys())


def test_print_matching_index():
    A = input().split()
    N = len(A)
    B = input().split()
    M = len(B)
    # Your code goes here
    index_map = defaultdict(list)
    for idx, char in enumerate(A):
        index_map[char].append(idx)

    for char in B:
        if char in index_map:
            print(' '.join(map(str,index_map[char])))
        else:
            print(-1)
def test_print_matching_index_bad():
    A = input().split()
    N = len(A)
    B = input().split()
    M = len(B)
    # Your code goes here
    result = defaultdict(str)
    visted = []
    for i in range(M):
        for j in range(N):
            if B[i] in visted:
                continue
            if B[i] == A[j]:
                result[B[i]] += (str(j) + ' ')
        else:
            if len(result[B[i]]) == 0:
                result[B[i]] += (str(-1))
            visted.append(B[i])
            print(result[B[i]])


def build_in_functions():
    
    # Use map to print the square of each numbers 
    my_ints = [4, 6, 3, 9, 2, 8, 12]
    
    # Use filter to print only the names that are less than or equal to seven letters
    my_names = ["scaler", "interviewbit", "rishabh", "student", "course"]
    
    # Use reduce to print the product of these numbers
    my_numbers = [4, 6, 9, 23, 5]
    
    # Fix all three respectively. 
    map_result = list(map(lambda x: x*x, my_ints))
    filter_result = list(filter(lambda name: len(name) <= 7, my_names))
    reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 1)
    
    print(map_result)
    print(filter_result)
    print(reduce_result)
    return 0
if __name__ == '__main__':
    build_in_functions()