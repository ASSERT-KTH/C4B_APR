# ---------------------------------------------------------------------------------------------------- #
#! /usr/local/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright © 2017 pmxt <pmxt@Manjunathas-MacBook-Air.local>
# ---------------------------------------------------------------------------------------------------- #

from math import sqrt

l = list()

for i in range(5):
    ll = list(map(int, input().rstrip().split()))
    if sum(ll) == 1:
        for j in range(5):
            if (ll[j] == 1):
                a, b = i + 1, j + 1
                break

dist = sqrt((pow(abs(3 - a), 2)) + (pow(abs(3 - b), 2)))

if (dist == (int(dist) + 0.0)):
    print(int(dist))
else:
    print(int(dist) + 1)