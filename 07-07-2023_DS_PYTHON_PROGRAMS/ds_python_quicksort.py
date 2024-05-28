def quick_sort(a):
    if len(a)<=1:
        return a
    pivot=a[0]
    left_a=[i for i in a if i<pivot]
    right_a=[i for i in a if i>pivot]
    return quick_sort(left_a)+[pivot]+quick_sort(right_a)

a=[56,32,78,43,67,89]
answer=quick_sort(a)
print(answer)

