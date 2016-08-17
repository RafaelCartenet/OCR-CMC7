# converts a vector into a matrix according to dimensions dim.
def vecIntoMatrix(Vec, dim):
    width = dim[0]
    height = dim[1]
    mat = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            mat[i][j] = Vec[(i)*width +j]
    return mat

# converts vector to string
def vecToString(vec):
    t = ""
    for i in range(len(vec)): t += str(vec[i])+" "
    return t

# con
def matToVector(matrix):
    height = len(matrix)
    width = len(matrix[0])
    vec = [0]*height*width
    for i in range(width):
        for j in range(height):
            vec[i*height + j] = matrix[j][i]
    return vec
