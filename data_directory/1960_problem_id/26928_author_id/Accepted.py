# ---------------------------------------------------------------------------------------------------- #
#! /usr/local/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright © 2017 pmxt <pmxt@Manjunathas-MacBook-Air.local>
# ---------------------------------------------------------------------------------------------------- #

l = list()

for i in range(5):
    ll = list(map(int, input().rstrip().split()))
    if sum(ll) == 1:
        for j in range(5):
            if (ll[j] == 1):
                a, b = i + 1, j + 1
                break

print(abs(3 - a) + abs(3 - b))