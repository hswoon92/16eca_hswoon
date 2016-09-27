# -*- coding: utf8 -*-
# [2011112047] [한소운]
"""
1변수 방정식의 근을 찾는 방법 중 sequential method 를 사용하여
어떤 함수 f(x)의 근을 찾고자 함
"""

# 1변수 방정식의 근을 찾는 함수를 모아둔 root_finding 모듈을 불러들임
import root_finding

print dir(root_finding)


def func(x):
    """
    근을 구하고자 하는 함수
    이 경우는 x * x - 3.0 =0 을 만족하는 x 를 찾게 되며 이러한 x는 3 ** 0.5 즉 3 의 제곱근임
    :param x:
    :return:
    """
    #
    return 1.0 * x * x - 3.0


# end of func()
# inspired by Scratch example

# func()의 근을 찾기 위해 root_finding 모듈의 sequential() 함수를 사용
print root_finding.sequential(func, 0.01)

# bisection method 로 구하는 법은?

# Newton Raphson method 로 구하는 법은?

