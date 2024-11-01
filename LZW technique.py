# get dictionary {key : character , value : ascii}
def getCharDictionary():
    # put ascii code for A-Z and a-z
    Dict = {chr(i): i for i in range(65, 91)}  # A-Z
    Dict.update({chr(i): i for i in range(97, 123)})  # a-z
    Dict[' '] = 32  # for spaces
    return Dict


# compression take string and return array of integers
def LZWcompression(string):
    # put ascii code for A-Z and a-z and for space
    Dict = getCharDictionary()
    # List carry compressed data <index>
    compressed = []
    # begin of string
    ind = 0
    # will be like ascii for longest match
    count = 128
    # initialize flag
    flag = True
    # loop for each char in the string
    while ind < len(string) and flag:
        # initialize value with recent char (that I'm pointing to now)
        value = string[ind]
        # will be like ascii for longest match that are in the Dict
        now = 0
        # check that value in the dictionary
        while value in Dict and flag:
            # put index of value (position)
            now = Dict[value]
            # check that we are not the last item
            if ind < len(string) - 1:
                # increase the longest match by the next value
                value += string[ind + 1]
                # increment ind to point to next char
                ind += 1
            # last item
            else:
                flag = False
                break
        # check now that it must be updated
        if now != 0:
            # put index of the longest match in the list
            compressed.append(now)
        # check boundary
        if ind < len(string):
            # add the count and the longest match to the Dict to check on it again
            Dict[value] = count
        # get next cell
        count += 1
    return compressed


# print codes in the compressed array in form of <integer>
def printTag(compressed):
    print("the compressed tags : ")
    for index in compressed:
        print(f"<{index}>")


# get dictionary {key : ascii , value : character}
def getCodeDictionary():
    # put ascii code for A-Z and a-z
    Dict = {i: chr(i) for i in range(65, 91)}  # A-Z
    Dict.update({i: chr(i) for i in range(97, 123)})  # a-z
    Dict[32] = ' '  # for spaces
    return Dict


# decompression take array of integers and return string
def LZWdecompression(compressed):
    # put ascii code for A-Z and a-z and space
    Dict = getCodeDictionary()
    count = 128  # will be like ascii for longest match
    result = ""  # decompressed string
    # if empty or not array
    if not compressed:
        return result
    # decompressed first item without inserting anything in Dict
    past = Dict[compressed[0]]
    # add it to the result
    result += past
    # Check for the longest match in the dictionary
    # begin from second item till end because I have already decompressed the first
    for ind in compressed[1:]:
        # if in directory so get corresponding string and stor eit in the string
        if ind in Dict:
            current = Dict[ind]
        # if not so I will use the past decompressed part to get where I'm now
        # it will be the past and the first character of it
        else:
            current = (past + past[0])
        # concatenate it with result
        result += current
        # Add a new entry to the dictionary
        Dict[count] = past + current[0]
        # increment count
        count += 1
        # the past will be recent decompressed part
        past = current
    return result


# print decompressed string 
def printString(string):
    print("the Decompressed string : " + string)


# Example : string
# Example : "ABABBABA"
# Example : "AAAAABBB"


string = input("Enter your string to compress it or EXIT to stop the program : ")
while string != "EXIT":
    print("_______________________________________________________")
    comp = LZWcompression(string)
    printTag(comp)
    print("_______________________________________________________")
    choice = input("Do you want to decompress it? Enter T or F : ")
    while choice != 'T' and choice != 'F':
        print("_______________________________________________________")
        print("Please enter T or F only for decompression")
        print("_______________________________________________________")
        choice = input("Do you want to decompress it? Enter T or F : ")
    if choice == 'T':
        print("_______________________________________________________")
        printString(LZWdecompression(comp))
        print("_______________________________________________________")
    else:
        print("_______________________________________________________")
    string = input("Enter your string to compress it or EXIT to stop the program : ")
print("_______________________________________________________")
print("\U0001F60D Thank you \U0001F970")
