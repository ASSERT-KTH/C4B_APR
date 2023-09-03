import sys
import string

def main():
    n = int(sys.stdin.readline())
    print(("".join([str(i) for i in range(1, 100)]))[n - 1])

if __name__ == "__main__":
    main()