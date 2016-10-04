# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에한글이 사용되었다는 점을 표시하는 것임
from math import cos, atan, sqrt, exp


def fwd_euler(f,x_init, t_start, t_end, delta_t):
    """
    상미분 방정식의 초기값 문제를 위한 전진 오일러법

    t[k] 와 t[k+1] 사이에는 dx/dt 가 상수일 것으로 가정함

    dx/dt 로 t[k] 에서의 값을 사용

    delta_t_sec 가 작은 값이 되지 않으면 오차가 커지는 경향이 있음

    :param f: dx/dt = f(x,y)
    :param x_init: x_init: x의 초기값
    :param t_start: t_start: 초기 시간
    :param t_end: t_end: 끝 시간
    :param delta_t: delta_t: 시간 간격
    :return: 시간, x의 list
    """
    # t_start ~ t_end 사이를 delta_t 간격으로 나눈 갯수. 소수점 아래는 버림? 반올림?
    m_time_step = int((t_end - t_start) * 1.0 / delta_t)

    # 상태의 갯수 == 초기 상태 벡터의 길이
    n_states = len((x_init))

    # time step 인덱스 k를 순서 대로 나열하여 tuple 로저장
    #  0, 1, .... m_time_step-1
    list_k = tuple(range(m_time_step))

    # time step tk 를 순서대로 나열하여 tuple 로 저장(list 와 달리 이후 변경 불가)
    list_t = tuple(([t_start + delta_t * i for i in list_k]))

    # 예를 들어 t_start, t_end, delta-t 이 0.0, 1.0, 0.1 로 주어졌다면
    #  m_time_step 은 10
    #        list_t 에는 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 가 저장될 것이며
    #        len(list_t) == 10

    # 각 time step 에서의상태 변수 값을 저장할 list 를 미리 할당(allocate) 시작
    # list_x 를 초기화 함
    # list_x[0] == k = 0 일때의 x 값 == 초기값 x_init
    list_x = [tuple(x_init)]

    # 행 할당 반복문 시작
    #    list_x[0] 는 위에서 이미 초기값 x_init 로 정함
    #    k = [1, 2, ..., n-1] 인 경우 x wmr
    #         list_x[1], list_x[2], ..., list_x[n-1] 의 값은 아직 알 수 없음
    #         따라서 0.0 을 n_states 개 담은 list 를 만듦
    for k in list_t[1:]:
        list_x.append([0.0] * n_states)
    # 행 할당 반복문 종료

    # 이렇게 하면 m_time_step x n_states 의 크기를 갖는 2차원 배열 공간이 준비됨

    # python 의 경우, 위와 같이 미리 할당하지 않고 각 time step 마다 state x 를 append 할 수도 있음
    # 다른 프로그래밍 언어의 경우 자료를 저장하기전에 저장할장소를 할당할 필요가 있을 경우가 많음

    # 상태 변수 저장할 공간 할당 끝

    # 상태 변수를 x0로 초기화
    xk = x_init

    # time step 반복문 시작
    for k in list_k[:-1]:
        # 이번 time step 에서의 기울기 dx/dt = f(x) 를 계산하여 sk 라는 변수에 저장
        sk = f(xk, list_t[k])

        # 다음 time step 에서의 상태 x[k+1] 을 저장할 공간을 xk1이라는 이름으로 지정
        xk1 = list_x[k + 1]

        # 각 상태 반복문
        for i in xrange(n_states):
            # 전진 오일러법을 적용
            xk1[i] = xk[i] + sk[i] * delta_t
        # 각 상태 반복문 끝

        # xk 값을 다음 상태 값으로 갱신
        xk = xk1
    # time step 반복문 끝

    # 각 time step 별 시간, 상태 값을 반환
    return list_t, list_x


# fwd_euler() 함수 끝


def mod_euler(f, x_init, t_start, t_end, delta_t):
    """
    상미분 방정식의 초기값 문제를 위한 수정 오일러법

    t[k] 와 t[k+1] 사이에는 dx/dt 가 선형으로 변화할 것으로 가정함

    dx/dt 로 t[k] 에서의 값을 사용

    :param f: dx/dt = f(x,y)
    :param x_init: x_init: x 의 초기값
    :param t_start: t_start: 초기 시간
    :param t_end: t_end: 끝 시간
    :param delta_t: 시간 간격
    :return: 시간, x 의 list

    Examples
    --------
    >>> list_t, list_x = mod_euler(lambda x, t:[(math.sin(math.pi*t) - x[0])*0.5],[0],0.0, 0.5, 0.1)
    >>> print  list_t
    [0.0, 0.10000000000000001, 0.20000000000000001, 0.30000000000000004, 0.40000000000000002, 0.5]
    >>> print list_x
    [[0], [0.0077254248593736849], [0.029382595321196049], [0.062135518400607666], [
    """

    # 각 time step 에서의 상태 변수 값 x 와 시간 값 t 를 저장할 list 를 시작
    # 내용이 될 변수를 [ ] 로 감싸면 list 로 인식됨
    # 한 time step 마다 하나씩 덧붙임
    # 이런 방식은 Python의 list 형의 특성을 이용

    # x_list[0] 은 상태 변수의 초기값으로 바뀌지 않을 것이므로 tuple 형으로 저장
    x_list = [tuple(x_init)]  # init x buffer
    t_list = [t_start]

    # k 번째 time step 의 시간 tk 초기화
    tk = t_start
    # k + 1 번째 time step 의 시간 tk1 초기화
    tk1 = tk + delta_t

    # t_list 의 마지막 요소가 매개변수로 주어졌던 t_end 값을 가지도록 delta_t의 1/2 값 만큼 증가 시킴
    t_end += ((-0.5) * delta_t)

    # time step 반복문 시작
    while tk1 < t_end:
        # x_list 에 마지막으로 추가된 요소로 k번째 time step의 상태 변수를 정함
        xk = x_list[-1]

        # step 1: 전진 Euler 법과 같음. 이번 time step 에서의 기울기로 delta_t 만큼 전진
        sk = f(xk, tk)
        # xk 의 모든 요소 x에 기울기 sk[i] 와 delta_t 의 곱을 더한 결과를 list 로 준비
        # 3행이 필요한 for 문 대신 이와같이 list comprehension 을 이용하면 한 행으로 쓸 수 있음
        xk1_p = [(x + sk[i] * delta_t) for i, x in enumerate(xk)]

        # step 2: 위에서 예측한 상태 변수 값 xk1_p 으로 k +1 번째 time step 에서의 기울기를 추정
        sk1_p = f(xk1_p,tk1)

        # step 3: k번째 time step 과 k + 1 번째 time step 사이에서는 기울기가 선형적으로 변화 했을 것으로 가정하여
        #         sk 와 sk1_p의 산술 평균 값으로 대표 기울기 sk_c를 계산
        sk_c = [(0.5 * (s + sk1_p[i])) for (i, s) in enumerate(sk)]

        # step 4: 위에서 구한 평균 기울기와 k 번째 time step 로 k + 1 번째 time step의 상태 변수를 계산
        xk1_c = [(x + sk_c[i] * delta_t) for i, x in enumerate(xk)]

        # k + 1 번째 time step 의 상태 변수를 x_list에 추가
        x_list.append(xk1_c)

        # tk1 값을 t_list 에 추가
        t_list.append(tk1)

        # tk, tk1 을 각각 delta_t 만큼 증가
        tk = tk1
        tk1 += delta_t

    return t_list, x_list


def runge_while(f, x_init, t_init, t_end, delta_t):
    """
    상미분 방정식의 초기값 문제를 위한 Runge Kutta 법

    t[k] 와 t[k+1] 사이에서 4개의 기울기를 구해 가중 평균을 계산함

    :param f: dx/dt = f(x,t)
    :param x_init: x_init: x 의 초기값
    :param t_init: t_start: 초기 시간
    :param t_end: t_end: 끝 시간
    :param delta_t: 시간 간격
    :return: 시간, x 의 list

    Examples
    --------
    >>> list_t, list_x = runge_while(lambda x, t:[(math.sin(math.pi*t) - x[0])*0.5],[0],0.0, 0.5, 0.1)
    >>> print list_t
    [0.0,
    >>> print list_x
    [[0],
    """

    # 각 time step 에서의 상태 변수 값 x 와 시간 값 t 를 저장할 list를 시작
    # 한 time step 마다 하나씩 덧붙임

    # x_list[0] 은 상태 변수의 초기값으로 바뀌지 않을 것이므로 tuple 형으로 저장
    x_list = [x_init] # init x buffer
    t_list = [t_init]

    # 기울기를 t + delta_t / 2 지점에서 구하기 위해 시간 증분 값을미리 준비
    delta_t_half = 0.5 * delta_t
    # 가중 평균 계산을 위해 6으로 나누기 때문에 계수를 미리 준비
    delta_t_sixth = delta_t / 6.0

    # k 번째 time step 의 시간 tk 초기화
    tk = t_init
    # k + 1/2 번째 time step 의 시간 tk_half 초기화
    tk_half = tk + delta_t_half
    # k + 1 번째 time step 의 시간 tk1 초기화
    tk1 = tk + delta_t

    # t_list 의 마지막 요소가 매개변수로 주어졌던 t_end 값을 가지도록 delta_t 의 1/2 값 만큼 증가 시킴
    t_end += ((-0.5) * delta_t)

    # time step 반복문 시작
    while tk1 < t_end:
        # x_list 에 마지막으로 추가된 요소로 k 번째 time step의 상태 변수를 정함
        xk = x_list[-1]

        # step 1 : 전진 Euler 법과 같음. k 번째 time step 에서의 기울기 k1
        k1 = f(xk, tk)

        # step 2 : 위에서 계산한 기울기로 k + 1/2 번째 time step 의 상태 변수를 추정하여 기울기 k2를 계산
        xk1_p = [(xk[i] + k * delta_t_half) for (i, k) in enumerate(k1)]
        k2 = f(xk1_p, tk_half)

        # step 3 : 위에서 계산한 기울기 k2 로 k + 1/2 번째 time step 의 상태 변수를 추정하여 기울기 k3를 계산
        xk2_p= [(xk[i] + k * delta_t_half) for (i, k) in enumerate(k2)]
        k3 = f(xk2_p, tk_half)

        # step 4 : 기울기 k3 로 k + 1 번째 time step 의 상태 변수를 추정하여 기울기 k4를 계산
        xk3_p = [(xk[i] + k * delta_t) for (i, k) in enumerate(k3)]
        k4 = f(xk3_p, tk1)

        # step 5 : k1, k2, k3, k4 의 가중 평균을 이용하여 k + 1 에서의 상태변수를 계산
        xk1_c = [x + delta_t_sixth * (k1[i] + 2 * (k2[i] + k3[i]) + k4[i]) for (i, x) in enumerate(xk)]

        # k + 1 번째 time step 의 상태 변수를 x_list 에 추가
        x_list.append(xk1_c)

        # tk1 값을 t_list 에 추가
        t_list.append(tk1)

        # 시간 값을 전진
        tk = tk1
        tk_half += delta_t
        tk1 += delta_t

    return  t_list, x_list


# 미분방정식을 위한 계수
tau = 0.5
m_kg = 10.0
c_newton_per_meter_per_sec = 100.0
k_newton_per_meter = 1000.0


def func(xk, tk):
    """
    dx/dt = f(x, t) 를 만족시키는 x(t)를 구하고자 하는 f(x, t)

    m d2x/dt2 + dx/dt + k = u

    :param xk: x(tk) 에서의 상태변수
    :param tk: 시간 tk
    :return: 시간 tk 에서의 dx/dt
    """
    # 계단 입력 u(t) = 1 if 0 <= t
    u = 1

    y1, y2 = xk[0], xk[1]

    # 기울기 계산
    y1dot = y2
    y2dot = (u - (k_newton_per_meter * y1 + c_newton_per_meter_per_sec * y2)) / m_kg

    return (y1dot, y2dot)


def exact(t):
    """
    1 자유도 진동계 엄밀해
    Ref : Rao, Mechanical Vibration, 2nd ed,
         ISBN 0-201-55693-6, Example 4.3
    """
    # 계단 입력
    u = 1
    # 고유진동수 (rad/sec)
    wn = sqrt(k_newton_per_meter / m_kg)
    # 감쇠율
    zeta = c_newton_per_meter_per_sec / (2.0* m_kg * wn)

    s = sqrt(1.0 - zeta * zeta)
    s1 = 1.0 / s

    # 감쇠진동수 (rad/sec)
    wd = wn * s
    # 위상 (rad)
    phi = atan(zeta * s)

    # 엄밀해
    y1 = (u / k_newton_per_meter) * (1.0 - s1 * exp(-zeta * wn * t) * cos(wd * t - phi))

    return (y1)


def main():
    help(fwd_euler)

    ti = 0.0
    te = 2.0
    delta_T = 0.01
    x0 = (0.0, 0.0)
    vT, vX = fwd_euler(func, x0, ti, te, delta_T)
    t_list_mod_euler, x_list_mod_euler = mod_euler(func, x0, ti, te, delta_T)
    t_list_runge, x_list_runge = runge_while(func, x0, ti, te, delta_T)

    delta_T = 0.001
    vT01, vX01 = fwd_euler(func, x0, ti, te, delta_T)

    # exact solution
    vXexact = tuple([exact(tk) for tk in vT])

    # 그래프 그리기 관련 기능 등을 담고 있는 pylab 모듈을 불러 들임
    import pylab

    pylab.plot(vT, vX, 'b', label='fwd Euler(0.01)')
    pylab.plot(vT01, vX01, 'g', label='fwd Euler(0.001)')
    pylab.plot(t_list_mod_euler, x_list_mod_euler, '*', label='Modified Euler(0.01)')
    pylab.plot(t_list_runge, x_list_runge, 'x-', label='Runge(0.01)')
    pylab.plot(vT, vXexact, 'ko-', label='exact')
    pylab.legend(loc=0)
    pylab.grid(True)
    pylab.ylabel('x')
    pylab.xlabel('t')
    pylab.show()

    vP, vV = zip(*vX)
    vP01, vV01 = zip(*vX)
    p_list_mod_euler, v_list_mod_euler, zip(*x_list_mod_euler)
    p_list_runge, v_list_runge = zip(*x_list_runge)

    pylab.plot(vP, vV, label='fwd Euler (0.01)')
    pylab.plot(vP01, vV01, label='fwd Euler(0.001)')
    pylab.plot(p_list_mod_euler, v_list_mod_euler, label='Modified Euler(0.01)')
    pylab.plot(p_list_runge,v_list_runge, label='Runge(0.01)')
    pylab.legend(loc=0)
    pylab.grid(True)
    pylab.ylabel('xdot')
    pylab.xlabel('x')
    pylab.show()


if "__main__" == __name__:
    main()


