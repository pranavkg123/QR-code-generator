def length_of_longest_substring(s: str) -> int:

    char_index_map = {}
    max_length = 0
    start = 0  # The start index of the current substring.

    # Loop through the string.
    for end in range(len(s)):
        # If the character is already in the current substring, update the start index.
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1
        
        # Update the last seen index of the character.
        char_index_map[s[end]] = end
        
        # Update the max_length of the substring without repeating characters.
        max_length = max(max_length, end - start + 1)
    
    return max_length


# Test the function
input_string = "abcabcbb"
result = length_of_longest_substring(input_string)
print(f"The length of the longest substring without repeating characters is: {result}")

    