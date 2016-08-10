def vecIntoMatrix(Vec, dim):
    width = dim[0]
    height = dim[1]
    mat = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            mat[i][j] = Vec[(i)*width +j]
    return mat

def vecToString(vec):
    t = ""
    for i in range(len(vec)): t += str(vec[i])+" "
    return t

def matToString(matrix):
    height = len(matrix)
    width = len(matrix[0])
    t = ""
    for i in range(height):
        string = ""
        for j in range(width):
            string += str(matrix[i][j])
        t += string + "\n"
    return t

def matToVector(matrix):
    height = len(matrix)
    width = len(matrix[0])
    vec = [0]*height*width
    for i in range(width):
        for j in range(height):
            vec[i*height + j] = matrix[j][i]
    return vec

def matToStringFile(matrix, filename):
    t = matToString(matrix)
    f = open(filename, "w")
    f.write(t)
    f.close
