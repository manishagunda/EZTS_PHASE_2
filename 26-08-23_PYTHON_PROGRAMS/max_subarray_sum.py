arr=list(map(int,input().split(" ")))
max_sum = float('-inf')  # Initialize max_sum with negative infinity
current_sum = 0
i = 0
j = 0
temp_start_idx = 0
for k in range(len(arr)):
    current_sum += arr[]
    if current_sum > max_sum:
        max_sum = current_sum
        i = temp_start_idx
        j = k
    if current_sum < 0:
        current_sum = 0
        temp_start_idx = k + 1
result=arr[i:j + 1]
print("Subarray with the largest sum:", result)