from Matrix import Matrix
from Vector import Vector

m1 = Matrix([[0.29, -0.01, 0.04], [-0.01, -0.18, 0.02], [0.04, 0.02, 0.01]])
m2 = Matrix([[29, -1, 4], [-1, -18, 2], [4, 2, 1]])
m3 = Matrix([[29, -1, 4], [-1, -18, 2], [4, 2, 0]])
e1 = Matrix([[1]])
e2 = Matrix([[1, 0], [0, 1]])
e1000 = Matrix([[(1 if i == j else 0) for j in range(1000)]
                for i in range(1000)])
v3_1 = Vector([0, 0, 0])
v3_2 = Vector([1, 4, -3])
v1_1 = Vector([1])
v1_2 = Vector([0])
v2_1 = Vector([1, 200])
v2_2 = Vector([0, 0.5])
v2_3 = Vector([0, 0.05])
v1000 = Vector([0 for i in range(1000)])
