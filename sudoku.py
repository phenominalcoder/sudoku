from sudokuUtils import getMatrix
# Uncomment any one import line based on your choice of algorithm
from Naive import solver
# from MRV import solver
# from MRVPlus import solver

matrix = getMatrix(input("File path:"))
solver(matrix)