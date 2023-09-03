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
    once_changed = 0
    cnt = 0
    acc = ''
    for lit in s:
        acc += lit
        if 'VK' in acc:
            cnt += 1
            acc = ''
        if 'KK' in acc or 'VV' in acc and not once_changed:
            once_changed = 1
            acc = ''
    return cnt+once_changed

if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    r = calc_substr(s, 'VK')
    sys.stdout.write('%s' % r)


# vim:ts=4:sts=4:sw=4:tw=85:et: