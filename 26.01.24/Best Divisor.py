import math

def get_digit_sum(number):
    return sum(map(int, str(number)))

def best_divisor(n):
    best_div = 1
    max_digit_sum = 1

    for i in range(2, n + 1):
        if n % i == 0:
            digit_sum = get_digit_sum(i)
            if digit_sum > max_digit_sum or (digit_sum == max_digit_sum and i < best_div):
                max_digit_sum = digit_sum
                best_div = i

    return best_div

if __name__ == '__main__':
    n = int(input().strip())
    result = best_divisor(n)
    print(result)
