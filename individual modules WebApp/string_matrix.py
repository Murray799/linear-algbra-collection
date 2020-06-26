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

def string_matrix(mis):
    mis = mis.strip("(")
    mis = mis.strip(")")
    # removes unnecessary elements from string
    mis = mis.split(";")
    # splits it into individual vector parts

    for element in range(len(mis)):
        mis[element] = string_vector(mis[element])
        # turns string in to list
    return mis
