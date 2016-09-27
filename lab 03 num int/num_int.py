# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이 사용되었다는 점을 표시하는 것임

# 수학 관련 기능을 담고 있는 math 모듈에서 exp 함수를 불러들임
from math import exp


def rect0(f, xi, xe, n=100):
    """
    0차 수치 적분
    xi ~ xe 사이를 n 개의 구획으로 나눔
    한 구획 안에서는 f(x) 가 상수일 것이라고 가정함
    :param f: 적분될 함수
    :param xi: 정적분 시작 지점
    :param xe: 정적분 끝 지점
    :param n: 구획을 나누는 갯수
    :return: f(x) 를 xi ~ xe 구간에서 정적분한 근사값
    """
    # 초기화 시작
    # n개로 나눈 각 구획의 길이를 정함
    delta_x = (float(xe) - float(xi)) / n

    # 각 구획 중간 지점 x 값의 list 를 만듦
    # k = 0, 1, 2, ..., (n-1)
    x = [xi + delta_x * (0.5 + k) for k in xrange(n)]

    # 적분 결과를 저장할 변수를 초기화
    result = 0.0

    # 초기화 끝

    # 주 반복문 main loop
    # 각 구획별로 연산을 반복 실시
    # k = 0, 1, 2, ..., (n-1)
    for k in xrange(n):
        # k 번째 x 값을 위에서 만든 list 에서 찾음
        xk = x[k]
        # k 번째 구획의 넓이를 직사각형의 면적으로 구함
        area_k = f(xk) * delta_x
        # 적분 결과에 누적시킴
        result += area_k
    # 주 반복문 끝

    # 적분 결과를 반환함
    return result


def trapezoid1(f, xi, xe, n=100):
    """
    1차 수치 적분
    xi ~ xe 사이를 n 개의 구획으로 나눔
    한 구획 안에서는 f(x) 가 1차 직선일 것이라고 가정함
    :param f: 적분될 함수
    :param xi: 정적분 시작 지점
    :param xe: 정적분 끝 지점
    :param n: 구간을 나누는 갯수
    :return: f(x) 를 xi ~ xe 구간에서 정적분한 근사값
    """
    # 초기화 시작
    # n개로 나눈 각 구획의 길이를 정함
    delta_x = (float(xe) - float(xi)) / n

    # 적분 구획 시작 지점 k 번째 x 초기화
    xk = xi
    # 적분 구획 시작 지점 함수값 k 번째 f(x) 초기화
    fxk = f(xk)

    # 적분 결과를 저장할 변수를 초기화
    result = 0.0
    # 초기화 끝

    # 주 반복문 main loop
    # 각 구획별로 연산을 반복 실시
    # k = 0, 1, 2, ..., (n-1)
    for k in xrange(n):
        # 적분 구획 끝 지점 k+1 번째 x 계산
        xk1 = xk + delta_x
        # 적분 구획 끝 지점 k+1 번째 f(x) 계산
        fxk1 = f(xk1)
        # k 번째 구획의 면적을 사다리꼴 공식으로 계산
        area_k = (fxk + fxk1) * delta_x * 0.5
        # 적분 결과에 누적시킴
        result += area_k

        # 현재 구획의 끝점이 다음 구획의 시작점이 됨
        # k+1 번째 x 값을 다음 구획 시작점의 x 값으로 지정
        xk = xk1
        # k+1 번째 f(x) 값을 다음 구획 시작점의 f(x) 값으로 지정
        fxk = fxk1
    # 주 반복문 끝

    # 적분 결과를 반환함
    return result


def simpson2(f, xi, xe, n=100, b_verbose=False):
    """
    2차 수치 적분
    xi ~ xe 사이를 n 개의 구획으로 나눔
    인접한 두 구획 안에서는 f(x) 가 2차 함수일 것이라고 가정함
    :param f: 적분될 함수
    :param xi: 정적분 시작 지점
    :param xe: 정적분 끝 지점
    :param n: 구획을 나누는 갯수
    :param b_verbose: 함수 실행 중 상세 내용 표시 여부
    :return: f(x) 를 xi ~ xe 구간에서 정적분한 근사값
    """
    # 초기화 시작

    if b_verbose:
        print "n =", n
        print "n%2 =", n % 2

    # n이 홀수라면 1 증가 시켜서 짝수로 만듦
    if (n % 2):
        n += 1

    # n 개로 나눈 각 구획의 길이를 정함
    delta_x = (float(xe) - float(xi)) / n

    # 적분 구획 시작 지점 k번째 x 초기화
    xk = xi
    # 적분 구획 시작 지점 함수값 k번째 f(x) 초기화
    fxk = f(xk)

    # 적분 결과를 저장할 변수를 초기화
    result = 0.0

    # 초기화 끝

    # 주 반복문 main loop
    # 두 구획씩 묶어 연산을 반복 실시
    # k = 0, 2, 4, ..., (n-1)
    for k in xrange(0, n, 2):
        # 적분 구획 중간 지점 k+1 번째 x 계산
        xk1 = xk + delta_x
        # 적분 구획 중간 지점 k+1 번째 f(x) 계산
        fxk1 = f(xk1)

        # 적분 구획 끝 지점 k+2 번째 x 계산
        xk2 = xk1 + delta_x
        # 적분 구획 끝 지점 k+2 번째 f(x) 계산
        fxk2 = f(xk2)

        # k 번째, k+1 번째 두 구획의 면적의 합을 simpson 공식으로 계산
        area_k = (fxk + 4 * fxk1 + fxk2) * (delta_x / 3.0)

        # 적분 결과에 누적시킴
        result += area_k

        # 현재 구획의 끝점이 다음 구획의 시작점이 됨
        # k+2 번째 x 값을 다음 구획 시작점의 x 값으로 지정
        xk = xk2
        # k+2 번째 f(x) 값을 다음 구획 시작점의 f(x) 값으로 지정
        fxk = fxk2
    # 주 반복문 끝

    # 적분 결과를 반환함
    return result



# 적분 될 함수
def f(x):
    return exp(x)


# 적분된 함수
def g(x):
    return exp(x)


# main() 함수를 정함
def main():
    """
    위 0, 1, 2차 함수의 적분
    :return:
    """
    # rect0 함수의 도움말을 표시
    # 도움말은 def rect0() 바로 아래의 문자열
    help(rect0)
    # 적분 구간 시작점
    x_begin = 0.0
    # 적분 구간 끝점
    x_end = 1.0
    # 적분 구간을 몇개의 구획으로 나눌 것인가
    n_interval = 8

    # 이론적 엄밀해
    exact = (g(x_end) - g(x_begin))
    print "exact solution =", exact

    # 함수 rect0 를 호출하여 수치 적분을 계산
    integration_0 = rect0(f, x_begin, x_end, n_interval)
    print "integration_0 =", integration_0, "err =", integration_0 - exact

    # 함수 trapezoid1 를 호출하여 수치 적분을 계산
    integration_1 = trapezoid1(f, x_begin, x_end, n_interval)
    print "integration_1 =", integration_1, "err =", integration_1 - exact

    # 함수 simpson2 를 호출하여 수치 적분을 계산
    integration_2 = simpson2(f, x_begin, x_end, n_interval)
    print "integration_2 =", integration_2, "err =", integration_2 - exact

    # 적분 결과를 그림으로 표시하기 위하여 pylab 모듈로 부터 특정 기능을 불러 들임
    from pylab import fill, bar, show, xlim, ylim, grid
    # 엄밀해 그림 시작
    n_plot = 100
    delta_x_plot = (float(x_end) - x_begin) / n_plot
    x = [x_begin + k * delta_x_plot for k in xrange(n_plot)]
    y = [f(x[k]) for k in xrange(n_plot)]
    x += [x_end, x_end, x_begin]
    y += [f(x_end), 0.0, 0.0]

    fill(x, y)
    # 엄밀해 그림 끝

    # rect0()
    # 0차 적분 그림 시작
    n_plot = n_interval
    delta_x_plot = (float(x_end) - x_begin) / n_plot
    x = [x_begin + k * delta_x_plot for k in xrange(n_plot)]
    y = [f(xk + 0.5 * delta_x_plot) for xk in x]
    x += [x_end]
    y += [0]

    bar(x, y, width=delta_x_plot, color='g', alpha=0.3)
    # 0차 적분 그림 끝

    # trapezoid1()
    # 1차 적분 그림 시작
    n_plot = n_interval
    delta_x_plot = (float(x_end) - float(x_begin)) / n_plot
    x = [x_begin + k * delta_x_plot for k in xrange(n_plot)]
    y = [f(xk) for xk in x]
    x += [x_end, x_end, x_begin]
    y += [f(x_end), 0.0, 0.0]

    fill(x, y, color='r', alpha=0.2)
    # 1차 적분 그림 끝

    xlim((x_begin, x_end))
    ylim((0.0, ylim()[1]))

    grid()
    show()

if "__main__" == __name__:
    # 이 .py 파일이 import 될 때는 아래의 내용이 실행되지 않음

    # 앞에서 정한 main() 함수를 실행시킴
    main()
