# -*- coding: utf8 -*-
# 그래프, 수학 기능을 담고 있는 pylab 모듈의 모든 기능을 불러들임
from pylab import *

# data 준비 시작
# normal distribution center at x=0 and y=5
# x = 0, y = 5 점을 중심으로 한 정규 분포 생성
x = randn(100000)
y = randn(100000) + 5

# 2차원 히스토그램
# 40개의 구간을 생성
H, xedges, yedges = histogram2d(x, y, bins=40)

# histogram 을 표시할 범위를 지정
# yedges 최소 최대값, xedges 최소 최대값으로 정함
extent = (yedges[0], yedges[-1], xedges[-1], xedges[0])
# data 준비 끝

# 그래프 준비 시작
# histogram 을 표시
# bitmap 으로 취급하여 표시함
plt.imshow(H, extent=extent, interpolation='nearest')
colorbar()
# 그래프 준비 끝

# 그래프 표시
show()

# http://matplotlib.org/examples/pylab_examples/hist2d_log_demo.html
