import streamlit as st
import numpy as np
from sympy import Matrix


page_config = st.set_page_config(
    page_title = "CMatrix",
    page_icon = "🎛",
    layout = "wide"

)

st.sidebar.title("CMatrix")
st.sidebar.image("img.png")
st.sidebar.info("A simple Website to perform the matrix operations.")
st.sidebar.markdown("---")
st.sidebar.info("## Operations:")
st.sidebar.info(
    '''
    - Addition
    - Subtraction
    - Multiplication
    - Inverse
    - Transpose
    - Determinant
    - Trace
    - Adjoint
    - calar Multiplication
    '''
)

st.sidebar.markdown("---")

def matrix_input(name = "Matrix", rows = 3, cols = 3):
    st.write(f"Enter values for {name}")
    matrix = []

    for i in range(rows):
        row = []
        cols_container = st.columns(cols)
        for j in range(cols):
            val = cols_container[j].number_input(f"{name}[{i+1}, {j+1}]", key = f"{name}_{i}_{j}", value = 0.8)
            row.append(val)
        matrix.append(row)
    return np.array(matrix)

st.title("CMatrix: Operate Your Matrices!!")

list_operations = ["Addition", "Subtraction", "Multiplication", "Inverse", "Transpose", "Determinant", "Trace", "Adjoint", 'Scalar Multiplication']
operations = st.selectbox("Choose Operations", list_operations)


def addition(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        return "Matrices should have same shape."
    return np.add(matrix1, matrix2)

def subtraction(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        return "Matrices should have same shape."
    return np.subtract(matrix1, matrix2)

def multiplication(matrix1, matrix2):
    if matrix1.shape[1] != matrix2.shape[0]:
        return "Columns of Matrix A should be equal to rows of Matrix B."
    return np.dot(matrix1, matrix2)

def transpose(matrix1):
    return np.transpose(matrix1)

def adjoint(matrix1):
    if matrix1.shape[0] != matrix1.shape[1]:
        return "Matrix is not a Square Matrix."
    return np.array(Matrix(matrix1).adjugate()).astype(np.float64)

def determinant(matrix1):
    if matrix1.shape[0] != matrix1.shape[1]:
        return "Matrix is not a Square Matrix."
    return np.linalg.det(matrix1)

def inverse(matrix1):
    if matrix1.shape[0] != matrix1.shape[1]:
        return "Matrix is not a Square Matrix."
    return np.linalg.inv(matrix1)

def trace(matrix1):
    if matrix1.shape[0] != matrix1.shape[1]:
        return "Matrix is not a Square Matrix."
    return np.trace(matrix1)

def scalar_multiplication(matrix1, scalar):
    return np.array(matrix1 * scalar)

if operations in ["Addition", "Subtraction", "Multiplication"]:

    matrix_cols  = st.columns(2)
    with matrix_cols[0]:
        st.subheader("Matrix A")
        rows_A = st.number_input("Rows_A", min_value = 1, max_value = 6, value = 2)
        cols_A = st.number_input("Cols_A", min_value = 1, max_value = 6, value = 2)
        A = matrix_input("A", int(rows_A), int(cols_A))
    with matrix_cols[1]:
        st.subheader("Matrix B")
        rows_B = st.number_input("Rows_B", min_value = 1,max_value = 6, value = 2)
        cols_B = st.number_input("Cols_B", min_value = 1,max_value = 6, value = 2)
        B = matrix_input("B", int(rows_B), int(cols_B))

    if st.button("Calculate:"):
        try:
            if operations == "Addition":
                st.write(addition(A, B))
            elif operations == "Subtraction":
                st.write(subtraction(A, B))
            elif operations == "Multiplication":
                st.write(multiplication(A, B))
        except Exception as e:
            st.error(e)
    
elif operations in ["Transpose", "Adjoint", "Determinant", "Inverse", "Trace", "Scalar Multiplication"]:

    st.subheader("Matrix A")
    rows_A = st.number_input("Rows_A", min_value = 1, max_value = 6, value = 2)
    cols_A = st.number_input("Cols_A", min_value = 1, max_value = 6, value = 2)
    A = matrix_input("A", int(rows_A), int(cols_A))

    
    if operations == "Scalar Multiplication":
        scalar = st.number_input("Enter Scalar:")

    if st.button("Calculate"):
        try:
            if operations == "Transpose":
                st.write(transpose(A))
            elif operations == "Adjoint":
                st.write(adjoint(A))
            elif operations == "Determinant":
                st.write(determinant(A))
            elif operations == "Inverse":
                st.write(inverse(A))
            elif operations == "Trace":
                st.write(trace(A))
            elif operations == "Scalar Multiplication":
                st.write(scalar_multiplication(A, scalar))
        except Exception as e :
            st.write(e)




