# -*- coding: utf-8 -*-
import numpy as np

"""
一，根据数组索引 获取 数据
"""
a = np.arange(12)**2

i = np.array([1,2,3,5,7,1,9])
print (a[i])

"""
[ 1  4  9 25 49  1 81]
"""

j = np.arange(12).reshape(2,2,3)
print(j)
"""
[[[ 0  1  2]
  [ 3  4  5]]

 [[ 6  7  8]
  [ 9 10 11]]]
"""

print(a[j])
"""
这里会生成和 j 一样维度的数组。并且数据为 a中对应序数的索引值
[[[  0   1   4]
  [  9  16  25]]

 [[ 36  49  64]
  [ 81 100 121]]]
"""

b = np.arange(24).reshape(2,3,4)
print(b)
"""
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
"""
j = np.array([[1,1,1,1],[0,1,1,1]])

print(b[j])
"""
[[[[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]]

  [[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]]

  [[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]]

  [[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]]]


 [[[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]]

  [[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]]

  [[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]]

  [[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]]]]
"""