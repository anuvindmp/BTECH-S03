class BlockMatrix:
    def __init__(self, size, block_size):
        self.size = size
        self.block_size = block_size
        self.num_blocks = size // block_size
        self.blocks = [[[0] * block_size for _ in range(block_size)] for _ in range(self.num_blocks ** 2)]

    def insert(self, row, col, value):
        block_row = row // self.block_size
        block_col = col // self.block_size
        inner_row = row % self.block_size
        inner_col = col % self.block_size
        self.blocks[block_row * self.num_blocks + block_col][inner_row][inner_col] = value

    def display(self):
        for i in range(self.num_blocks):
            for j in range(self.num_blocks):
                print("Block ({}, {}):".format(i, j))
                for row in range(self.block_size):
                    for col in range(self.block_size):
                        global_row = i * self.block_size + row
                        global_col = j * self.block_size + col
                        if global_row < self.size and global_col < self.size:
                            print(self.blocks[i * self.num_blocks + j][row][col], end=" ")
                        else:
                            print("0", end=" ")
                    print()
                print()
                
def conformal_decomposition(matrix):
     length = len(matrix)
     if length != len(matrix[0]):
          print(f"Invalid Dimension Error: Expected a square matrix but a Matrix({length}x{len(matrix[0])}) was given.")
          return None, None
     diamat = [[0]*length for i in range(length)]
     offdiamat = [[0]*length for i in range(length)]

     for i in range(length):
          for j in range(length):
               if i == j:
                    diamat[i][j] = matrix[i][j]
               else:
                    offdiamat[i][j] = matrix[i][j]
     return diamat, offdiamat


matrix = BlockMatrix(4, 2)
value = 1
for i in range(4):
    for j in range(4):
        matrix.insert(i, j, value)
        value += 1
print("Block Matrix:")
matrix.display()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Conformal Decomposition matrix:")
for i in mat:
     for j in i:
          print("{:>5}".format(j), end="")
     print()
diamat, offdiamat = conformal_decomposition(mat)
print("Diagonal Matrix: ")
for i in diamat:
     for j in i:
          print("{:>5}".format(j), end="")
     print()

print("Off-Diagonal Matrix: ")
for i in offdiamat:
     for j in i:
          print("{:>5}".format(j), end="")
     print()
