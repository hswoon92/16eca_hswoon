#-*- coding: utf8 -*-

# [2011112047] [한소운]

"""
가우스 소거법 모듈
python 의 list 의 list 를 이용하는 행렬고 구현함
"""
import matrix


def upper_triangle(mat_a_vec_b):
    m_row, n_col = matrix.shape(mat_a_vec_b)

    for i_pivot in range(m_row -1):
        pivot = float(mat_a_vec_b[i_pivot][i_pivot])
        for j_row in range(i_pivot + 1, m_row):
            ratio = -(mat_a_vec_b[j_row][i_pivot] / pivot)
            matrix.row_mul_add(mat_a_vec_b, j_row, i_pivot, ratio, i_pivot)


def back_substitution(mat_a_vec_b):
    m_row = len(mat_a_vec_b)
    x = matrix.alloc_vec(m_row)

    for i_row in range(len(mat_a_vec_b) - 1, -1, -1):
        s = mat_a_vec_b[i_row][-1]

        for kCol in range(i_row + 1, len(mat_a_vec_b)):
            s -= mat_a_vec_b[i_row][kCol] * x[kCol]

        x[i_row] = s / mat_a_vec_b[i_row][i_row]

    return x


def gauss_elimination(mat_a, b):
    """
    1차 다원 연립 방정식 Ax = b 에서 x 를 구함
    A: 계수 행렬
    b: 상수 벡터
    """
    m_row, n_col = matrix.shape(mat_a)
    mat_a_vec_b = matrix.alloc_mat(m_row, n_col + 1)

    for i in range(m_row):
        for j in range(n_col):
            mat_a_vec_b[i][j] = mat_a[i][j]
        mat_a_vec_b[i][-1] = b[i]

    upper_triangle(mat_a_vec_b)

    x = back_substitution(mat_a_vec_b)

    del mat_a_vec_b[:]
    del mat_a_vec_b

    return x

def main():
    A = [[3, 2, 1],
         [2, 3, 2],
         [1, 2, 3]]
    b = [1,
         2,
         3]

    x = gauss_elimination(A, b)

    Ax = matrix.mul_mat_vec(A, x)
    print Ax, '==', b



if "__main__" == __name__:
    main()
