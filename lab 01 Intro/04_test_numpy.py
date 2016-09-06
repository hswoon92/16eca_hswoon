# -*- coding: utf8 -*-
# 배열, 행렬 관련 기능을 담고 있는 numpy 모듈을 불러 들여 np 라는 이름 아래 연결함
import  numpy as np

r1 = np.array((1.0, 2.0))
print "r1 =", r1

r2 = np.array((-2.0, 1.0))
print  "r2 =", r2

r3 = r1 + r2
print  "r3 =", r3

# Numpy Quickstart tutorial, https://docs