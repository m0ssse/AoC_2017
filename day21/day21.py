def generate_rules(rules):
    res = {}
    for line in rules:
        mat, mat_out = line.split(" => ")
        mat = s_to_mat(mat)
        for _ in range(4):
            flip_h = mat_to_s(["".join(row) for row in flip_horizontal(mat)])
            flip_v = mat_to_s(["".join(row) for row in flip_horizontal(mat)])
            res[flip_h] = mat_out
            res[flip_v] = mat_out
            res[mat_to_s(["".join(row) for row in mat])] = mat_out
            mat = rotate_matrix(mat)
    return res

def convert_rules(rules):
    rules_2x2 = {}
    rules_3x3 = {}

def mat_to_bin(mat):

def rotate_matrix(mat):
    return flip_horizontal(transpose(mat))

def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat))]

def flip_horizontal(mat):
    return [row[::-1] for row in mat]

def flip_vertical(mat):
    return [row[:] for row in mat][::-1]

def s_to_mat(s):
    return s.split("/")

def mat_to_s(mat):
    return "/".join(mat)

def divide(mat, n):
    k = len(mat)//n
    res = []
    for i in range(k):
        new_row = []
        for j in range(k):
            submat = [row[j*n:(j+1)*n] for row in mat[i*n:(i+1)*n]]
            new_row.append(submat)
        res.append(new_row)
    return res
    
fname = "day21_input.txt"
with open(fname) as file:
    rules = generate_rules([line.strip() for line in file])

M = [".#..", "....", "....", "...."]
MM = divide(M, 2)
print(MM)