h=[]
for x in range(0,5):
    h.append(int(input()))

def quicksort(arr):
    """ Quicksort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if not arr:
        return []

    return quicksort([x for x in arr if x < arr[0]]) \
        + [x for x in arr if x == arr[0]] \
        + quicksort([x for x in arr if x > arr[0]])
#h=quicksort(h)

t=0

for x in range(1,h[4]+1):
    if ((x%h[0]==0) or (x%h[1]==0) or (x%h[2]==0) or (x%h[3]==0)):
        
        t=t+1

print(t)