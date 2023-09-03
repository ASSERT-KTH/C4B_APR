# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:25:33 2017

@author: forgeguest
"""
print(''.join('.{}'.format(c) for c in [char for char in str(input()).lower() if char not in 'aeiouy']))