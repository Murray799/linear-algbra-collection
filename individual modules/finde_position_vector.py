def finde_position_vector(point_1, point_2):
    for element in range(len(point_1)):
        point_2[element] = point_2[element] - point_1[element]
        # goes through each element of the two points then subtracts them  

    return point_2
