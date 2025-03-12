def prob(data):
    # Calculate the frequency of each character in the data
    freq = {}
    for char in data:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq  # Return raw frequencies


def getting_binary(freq):
    # Start with the dictionary of frequencies
    code = {}

    # Convert the frequency dictionary to a sorted list of tuples (character, frequency)
    freq = sorted(freq.items(), key=lambda item: item[1])

    while len(freq) > 1:
        # Pop the two smallest items (characters with the lowest frequencies)
        first_char, first_freq = freq.pop(0)
        second_char, second_freq = freq.pop(0)

        # Create a new node with combined frequency and characters
        new_freq = first_freq + second_freq
        new_char = first_char + second_char

        # Update the Huffman codes for both first and second characters
        for char in first_char:
            code[char] = '0' + code.get(char, '')
        for char in second_char:
            code[char] = '1' + code.get(char, '')

        # Add the new node back into the frequency list
        freq.append((new_char, new_freq))

        # Sort the list again by frequency to maintain order
        freq = sorted(freq, key=lambda item: item[1])
    return code


def standard_huffman_comp(code, string):
    binary = ""
    for char in string:
        binary += code[char]

    return binary


def standard_huffman_decomp(code, binary):
    reversed_code = {codes: char for char, codes in code.items()}
    string = temp = ""
    for binary_char in binary:
        temp += binary_char
        if temp in reversed_code:
            string += reversed_code[temp]
            temp = ""
    return string


# Example usage
data = "banana"
freq = prob(data)  # Get the frequency of characters
codes = getting_binary(freq)
huffman_binary = standard_huffman_comp(codes, data)  # Get the Huffman codes
huffman_string = standard_huffman_decomp(codes, huffman_binary)
print(huffman_binary)
