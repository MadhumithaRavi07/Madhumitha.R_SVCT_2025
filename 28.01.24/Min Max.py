def miniMaxSum(arr):
    arr.sort()
    total_sum = sum(arr)
    min_sum = total_sum - arr[-1]
    max_sum = total_sum - arr[0]
    
    print(min_sum, max_sum)

# Example usage:
input_values = input().split()
arr = list(map(int, input_values))

miniMaxSum(arr)
