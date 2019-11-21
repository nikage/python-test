import sys

m, n = sys.argv[1:]

matrix = [[j for j in range(int(n))] for i in range(int(m))]


for i in matrix:
    print(i)
