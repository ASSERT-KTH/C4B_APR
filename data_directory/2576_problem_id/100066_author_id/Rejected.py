#! /usr/bin/env python


def compute_sets(a, b, k):
    if not(a >= k or b >= k):
        return -1

    awins = a // k
    bwins = b // k

    if awins == 0:
        if b % k != 0:
            print(-1)
            return -1

    elif bwins == 0:
        if a % k != 0:
            print(-1)
            return -1

    return awins + bwins


def main():

    import sys

    for line in sys.stdin:
        line = [int(x) for x in line.rstrip().split(" ")]
        k = line[0]
        a = line[1]
        b = line[2]
        print(compute_sets(a,b,k))


    # for x in range(0, 10):
    #     print("============================")
    #     print("test %s " % x)
    #     k = random.randint(1,10**4)
    #     while True:
    #         a = random.randint(0,10**4)
    #         b = random.randint(0,10**4)
    #         if a + b != 0:
    #             break
    #     if not(a >= k or b >= k):
    #         print(-1)
    #         continue


    #     awins = a // k
    #     bwins = b // k

    #     if awins == 0:
    #         if b % k != 0:
    #             print(-1)
    #             continue

    #     elif bwins == 0:
    #         if a % k != 0:
    #             print(-1)
    #             continue

    #     total_played = awins + bwins
    #     print("SCORE TO WIN ::: %s" % k)
    #     print("TOTAL POINTS ::: Misha: %s ::: Vanya %s" % (a, b))
    #     print("SETS WON ::: Misha: %s ::: Vanya %s" % (awins, bwins))
    #     print(total_played)

if __name__ == '__main__':
    main()