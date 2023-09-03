"""
Solution to the 165B problem on CodeForces.
"""
import sys
import math

cache = [1]

def updater(n: int, *inputs) -> None:
    global cache
    for i in range(1, len(cache)):
        for num in inputs:
            if i - num == 0:
                cache[i] = max(1, cache[i])
            elif cache[i-num] != 0:
                cache[i] = max(cache[i-num]+1, cache[i])

def main() -> None:
    """
    The main method.
    """
    global cache
    inputs = list(map(int, input().split()))

    # Initialize the cache
    cache = [0 for _ in range(inputs[0]+1)]
    updater(*inputs)
    print(cache[inputs[0]])


if __name__ == "__main__":
    main()