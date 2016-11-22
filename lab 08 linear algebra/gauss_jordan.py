#-*- coding: utf8 -*-

# [2011112047] [한소운]

"""
가우스 조단법 모듈
python 의 list 의 list 를 이용하는 행렬로 구현함
"""

import matrix


def generate_mat_ai(mat_a):
    m_row, n_col = matrix.shape(mat_a)
    mat_ai = matrix.alloc_mat(m_row, n_col + m_row)
    for i_pivot in range(m_row):
        # copy mat_a
        for j_col in range(n_col):
            mat_ai[i_pivot][j_col] = mat_a[i_pivot][j_col]
        # make j
        mat_ai[i_pivot][n_col + i_pivot] = 1.0

    return mat_ai


def gauss_jordan(mat_a):
    mat_ai = generate_mat_ai(mat_a)

    for i_pivot in range(len(mat_ai)):
        matrix.row_mul_scalar(mat_ai, i_pivot, 1.0 / mat_ai[i_pivot][i_pivot])
        for j_row in range(len(mat_ai)):
            if i_pivot != j_row:
                matrix.row_mul_add(mat_ai, j_row, i_pivot, -mat_ai[j_row][i_pivot])

    inv_mat = matrix.alloc_mat(len(mat_ai), len(mat_ai), )

    for i in range(len(mat_ai)):
        for j in range(len(mat_ai)):
            inv_mat[i][j] = mat_ai[i][len(mat_ai) + j]

    del mat_ai[:]
    del mat_ai

    return  inv_mat


# Q: 필요한 memory를 더 절약할 수 있는 방법이 있을 것인가?


if "__main__" == __name__:
    A = [[3, 2, 1],
         [2, 3, 2],
         [1, 2, 3]]

    A_inverse = gauss_jordan(A)
    print("A inverse")
    matrix.show_mat(A_inverse)

    I_expected = matrix.mul_mat(A, A_inverse)
    print("I expected")
    matrix.show_mat(I_expected)
