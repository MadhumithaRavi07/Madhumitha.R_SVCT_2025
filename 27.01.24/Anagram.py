def anagram(s):
    length = len(s)

    # If the length of the string is not even, it's not possible to split into two equal parts
    if length % 2 != 0:
        return -1

    # Split the string into two equal parts
    mid = length // 2
    s1 = s[:mid]
    s2 = s[mid:]

    # Count the occurrences of each character in both substrings
    char_count_s1 = [0] * 26
    char_count_s2 = [0] * 26

    for char in s1:
        char_count_s1[ord(char) - ord('a')] += 1

    for char in s2:
        char_count_s2[ord(char) - ord('a')] += 1

    # Calculate the minimum number of characters to change
    changes = 0
    for i in range(26):
        changes += abs(char_count_s1[i] - char_count_s2[i])

    return changes // 2  # Since each change affects two characters

# Example usage:
test_cases = int(input())
for _ in range(test_cases):
    s = input()
    result = anagram(s)
    print(result)
