# -*- coding: utf-8 -*-
import numpy as np

"""
一，不全部拷贝。只是加引用
"""
a = np.arange(16)
b=a  #没有创建新的array

print(a.shape)
(16)
b.shape=4,4

print(a.shape)
(4,4)

print(b is a )
"""
True
"""


"""
二，浅拷贝
浅拷贝只是共享基础数据  并不拥有自己的数据。如果拷贝改变数据。被拷贝的数据也改变
"""

c = a.view()

print(c is a )
"""
False
"""

print(c.base is a )
"""
True
"""

print(c.flags.owndata)
"""
False
"""

c.shape=2,8

print(a.shape)
"""
(4L, 4L)
"""

c[0,0] = 1000

print(a)
"""
a 的数据也变了
[[1000    1    2    3]
 [   4    5    6    7]
 [   8    9   10   11]
 [  12   13   14   15]]
"""


"""
三，深拷贝
深拷贝出来的数组和原数组没有任何关系
"""
d = a.copy()

print(d is a )

"""
False
"""


print(d.base is a )
"""
False
"""

d[0,0] = 2000

print(a)
"""
数据没变
[[1000    1    2    3]
 [   4    5    6    7]
 [   8    9   10   11]
 [  12   13   14   15]]
"""
