def solve(n, operations):
    total_candies = 0

    for operation in operations:
        start_index, end_index, candies_added = operation
        total_candies += (end_index - start_index + 1) * candies_added

    average_candies = total_candies // n
    return average_candies

# Example usage:
n, m = map(int, input().split())
operations = [list(map(int, input().split())) for _ in range(m)]

result = solve(n, operations)
print(result)

