# coding: utf-8
import sys

__author__ = 'buyvich'


def calc_substr(s, sub):
    """
    >>> calc_substr('KV', 'VK')
    0
    >>> calc_substr('VK', 'VK')
    1
    >>> calc_substr('VV', 'VK')
    1
    >>> calc_substr('V', 'VK')
    0
    >>> calc_substr('VKKKKKKKKKVVVVVVVVVK', 'VK')
    3
    >>> calc_substr('KVKV', 'VK')
    1
    >>> calc_substr('VKKKK', 'VK')
    2
    """
    max_cnt = s.count(sub)
    for i in range(len(s)):
        l = list(s)
        for k in 'VK':
            l[i] = k
            tmp_cnt = ''.join(l).count(sub)
            max_cnt = max(max_cnt, tmp_cnt)
    return max_cnt


if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    r = calc_substr(s, 'VK')
    sys.stdout.write('%s' % r)


# vim:ts=4:sts=4:sw=4:tw=85:et: