# Student name: Joseph Difilippo

def issorted(A) :
    """Returns True if A is sorted in non-decreasing order,
    and returns False if A is not sorted.

    Keyword arguments:
    A - a Python list.
    """
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True


def randomlist(length, low=0, high=100) :
    """Generates and returns a Python list of random integer values.
    The integers in the list are generated uniformly at random from
    the interval [low, high], inclusive of both end points.

    Keyword arguments:
    length - the length of the list.
    low - the lower bound for the random integers.
    high - the upper bound for the random integers.
    """

    return [random.randint(low, high) for i in range(length)]

  


def insertionsort(A) :
    """Implementation of the insertion sort algorithm.

    Keyword arguments:
    A - a Python list.
    """
    
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key




def heapsort(A) :
    """Implementation of the heapsort algorithm.

    Keyword arguments:
    A - a Python list.
    """
    
    heapsize = len(A)
    
    def left(i) :
        return 2*i 
    
    def right(i) :
        return 2*i + 1
    
    def maxheapify(A, i) :
        nonlocal heapsize
        l = left(i)
        r = right(i)
        if (l < heapsize and A[l] > A[i]):
            largest = l
        else:  largest = i
        if (r < heapsize and A[r] > A[largest]):
            largest = r
        if (largest != i):
            A[i], A[largest] = A[largest], A[i]
            maxheapify(A, largest)
        
    def buildmaxheap(A) :
        nonlocal heapsize
        for i in range(heapsize // 2 -1, -1, -1):
            maxheapify(A, i)

    buildmaxheap(A)
    for i in range (len(A)-1, 0, -1):
        A[0],A[i] = A[i],A[0]
        heapsize = heapsize - 1
        maxheapify(A,0)


if __name__ == "__main__" :


    import random
    import heapq
    
    A = [4,6,2,4,5]
    print("Expected output False:")
    print(issorted(A))
    print()

    A = [3,4,4,5,6,7]
    print("Expected output True:")
    print(issorted(A))
    print()

    A = randomlist(6,0,76)
    print("unsorted list: ", A)
    insertionsort(A)
    print("sorted list: ", A)
    print()

    A = randomlist(8,1,76)
    print("unsorted list: ", A)
    heapsort(A)
    print("heapsort: ", A)
    print()

