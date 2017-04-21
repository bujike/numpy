# -*- coding: utf-8 -*-
import numpy as np
a = np.arange(15).reshape(3,5)
print a
"""
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
"""
print a.ndim

"""
2
"""

print a.shape

"""
(3,5)
"""

print a.size

"""
15
"""

print a.dtype

"""
int32 (由个人cpu位数而定)
"""

print a.itemsize

"""
4
"""

print type(a)

"""
<type 'numpy.ndarray'>
"""