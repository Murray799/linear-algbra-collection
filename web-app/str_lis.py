def string_vector(lis):
    lis = lis.strip("[")
    lis = lis.strip("]")
    # removes unnecessary elements from string
    lis = lis.split(",")
    # split in to individual numbers
    for element in range(len(lis)):
        lis[element] = float(lis[element])
        # turns string in to numbers
    return lis
