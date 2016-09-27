# -*- coding: utf8 -*-
"""
일정 하중 아래 허용응력과 안전률을 고려한 봉의 최소 직경
"""
# 수학 관련 기능을 담은 모듈을 읽어들임
import math

import root_finding


def problem_to_solve(radius_m):
    """
    안전률을 고려한 허용 응력
    :param radius_m:
    :return:
    """

    # 안전률
    safety_factor = 2.0

    # 허용 최대 응력
    stress_max_Pa = 207e6

    # 하중
    force_N = 100

    result = circular_section_stress(radius_m, force_N) - stress_max_Pa / safety_factor

    return result

def circular_section_stress(r_m, force_N):
    """
    원형 단면의 응력을 계산
    :param r_m:
    :param force_N:
    :return:
    """
    area_m2 = r_m * r_m * math.pi
    stress_Pa = force_N / area_m2
    return stress_Pa


def main():
    # 2분법을 이용하여 허용 응력과 안전률을 고려한 최소 직경을 구함
    # 더 적은 초기값
    x_l_init = root_finding.epsilon_global * 2
    # 더 큰 초기값
    x_h_init = 1.0
    # 2분법 호출
    result = root_finding.bisection(problem_to_solve, x_l_init, x_h_init, 1e-9)
    # 결과 표시
    print "result =", result


if "__main__" == __name__:
    main()