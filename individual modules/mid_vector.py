def mid(lis_vec):
    # input must be list of vectors
    new_vec = []
    add = 0

    for vec_row in range(len(lis_vec[0])):
        for element in lis_vec:
            add += element[vec_row]
        new_vec.append(add / len(vec_row))
        add = 0

    return new_vec
