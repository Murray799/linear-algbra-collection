def string_lis(lis):
    new_lis = []
    for pos in range(len(lis)):
        # goes throug each element of string
        if pos == len(lis):
            break
        # if at the end ends vefore Index error

        if lis[pos] == "[" or lis[pos] == ",":
            # if start stop flag
            if pos != 0:
                new_lis.append(float(temp))
                # add to temp if start flag as float
            temp = ""
            #wipe temp
            pass

        else:
            temp += lis[pos]
            # if not falg then part of number add it to tamp
            
    return new_lis
