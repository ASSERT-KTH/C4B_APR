#!/usr/bin/python3


def main():
    exp = int(input())-1
    data = [8, 4, 2, 6]
    print(data[exp%4])


if __name__ == "__main__": main()