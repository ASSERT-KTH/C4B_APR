def get_namee():
    nth = int(input())
    queue = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

    if nth < len(queue):
        return queue[nth-1]

    while len(queue) < nth:
        first_elem = queue.pop(0)
        queue.append(first_elem)
        queue.append(first_elem)

    return queue[nth-1]


if __name__ == '__main__':
    print(get_namee())