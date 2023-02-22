from sudokuUtils import getMatrix
from Naive import solver
# from MRV import solver
# from MRVPlus import solver

matrix = getMatrix(input("File path:"))
solver(matrix)