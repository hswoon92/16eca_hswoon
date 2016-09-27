# -*- coding: utf8 -*-
# [2011112047] [한소운]
"""
1변수 방정식의 근을 찾는 방법 중 Newton-Raphson method 를 사용하여
어떤 함수 g(x)의 근을 찾고자 함
아래 예는 Newton-Raphson method 를 사용하기 곤란한 경우임
"""
# "Newton's method," Wikipedia. [Online]. Available: http://en.wikipedia.org/wiki/newton's_method.

# 1변수 방정식의 근을 찾는 함수를 모아둔 root_finding 모듈을 불러들임

import root_finding as rf
help(root_finding)


def g(x):
    # 근을 구하고자 하는 함수
    return x ** 3 - 2 * x + 2


def dgdx(x):
    # g(x) 의 x 에 대한 미분
    return 3.0 * x ** 2.0 - 2.0


if "__main__" == __name__:
    # 주어진 초기값에서 시작하여 g(x) = 0 인 x 를 찾고자 함
    # 생각보다 시간이 많이 걸릴 수 있음
    x_nr = rf.newton(g, dgdx, 0)
    print('x = %g, f(%g) = %g' % (x_nr, x_nr, g(x_nr)))
