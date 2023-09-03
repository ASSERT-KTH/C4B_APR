# -*- coding: utf-8 -*-
# @Author: HaonanWu
# @Date:   2017-02-28 16:12:00
# @Last Modified by:   HaonanWu
# @Last Modified time: 2017-02-28 16:19:40

from math import *
n,m,z=map(int,raw_input().split())
print(z//(n*m//gcd(n,m)))