import math

# _______________________________________________________________________
# Tag class definition to represent a single compressed element (Tag)
class Tag:
    def __init__(self, position, length, nextSymbol):
        self.position = position
        self.length = length
        self.nextSymbol = nextSymbol

# _______________________________________________________________________
# Function to compress a string using the LZ77 algorithm
def lz77Compression(st, searchWindowSize, lookAheadSize):
    compressed = []
    strLength = len(st)
    i = 0


    while i < strLength:
        # Define the search window boundaries
        start = max(0, i - searchWindowSize)
        end = i - 1

        # Initialize variables to track the best match
        minPosition = 0
        maxLength = 0

        # Determine the maximum allowed match length based on the presence of a next character
        maxMatchLength = lookAheadSize - 1 if i + lookAheadSize < strLength else lookAheadSize

        # Search through the window for the longest match
        for j in range(end, start - 1, -1):
            length = 0
            while (length < maxMatchLength and
                   i + length < strLength and
                   st[j + length] == st[i + length]):
                length += 1

            if length > maxLength:
                maxLength = length
                minPosition = i - j

            # If the longest possible match is found, break early
            if maxLength == maxMatchLength:
                break


        # Get the next symbol after the match (or null if at the end of the string)
        nextSymbol = st[i + maxLength] if i + maxLength < strLength else '\0'

        # Add a tag for the compressed data
        compressed.append(Tag(minPosition, maxLength, nextSymbol))

        # Move the current position forward by the length of the match + 1
        i += maxLength + 1

    return compressed


# _______________________________________________________________________
# Function to decompress the data from the compressed format (list of Tags)
def lz77Decompression(compressed):
    decompressed = ""

    for tag in compressed:
        position = tag.position
        length = tag.length
        nextSymbol = tag.nextSymbol
        start = len(decompressed) - position

        # Rebuild the matching substring from the decompressed string
        for i in range(length):
            decompressed += decompressed[start + i]

        # Add the next symbol if it's not a null character
        if nextSymbol != '\0':
            decompressed += nextSymbol

    return decompressed

# _______________________________________________________________________
# Function to calculate the compressed size based on the tags
def calculateCompressedSize(compressed):
    maxPosition = 0
    maxLength = 0
    numberOfTags = len(compressed)

    # Find the maximum values for position and length to determine bit size
    for tag in compressed:
        maxPosition = max(maxPosition, tag.position)
        maxLength = max(maxLength, tag.length)

    # Avoid log2(0) issues by setting at least 1 bit for small values
    positionBits = math.ceil(math.log2(maxPosition + 1)) if maxPosition > 0 else 1
    lengthBits = math.ceil(math.log2(maxLength + 1)) if maxLength > 0 else 1

    # Calculate total size (in bits): position bits + length bits + 8 bits for nextSymbol
    totalSize = (positionBits + lengthBits + 8) * numberOfTags

    print("Compressed size : ", end="")
    print(f"{totalSize} bits")
    print("_____________________________________")

# _______________________________________________________________________
# Function to print all compressed tags
def printTags(compressed):
    for tag in compressed:
        print(f"({tag.position},{tag.length},'{tag.nextSymbol}')")


# _______________________________________________________________________
# Main program execution
if __name__ == '__main__':
    # Input from the user
    st = input("Enter string: ")
    print("_____________________________________")

    searchWindowSize = int(input("Enter searchWindowSize: "))
    print("_____________________________________")

    lookAheadSize = int(input("Enter lookAheadSize: "))

    # Compression process
    compressed = lz77Compression(st, searchWindowSize, lookAheadSize)

    # Output compressed tags
    print("_____________________________________")
    print("Tags of compressed data: ")
    printTags(compressed)

    # Calculate and display the original and compressed sizes
    print("_____________________________________")
    print("Original size : ",end="")
    originalSize = 8 * len(st)
    print(f"{originalSize} bits")

    # Print compressed size
    calculateCompressedSize(compressed)

    # Decompression process and output
    print("Data after decompression: ")
    print(f"{lz77Decompression(compressed)}")

    print("_____________________________________")
    print("\U0001F60D The happy end \U0001F970")

# _______________________________________________________________________

# Example : string  search_window_size  look_ahead_size
# Example : abaababaabbbbbbbbbbbba  11  15
# Example : barbara-bar  4  4
# Example : abcabbcabbcabca  7  8
# Example : ABAABABABABABABABABABA  12  11
# EXample : ABCABCABC  3 6


#abaababaabbbbbbbbbbbba
