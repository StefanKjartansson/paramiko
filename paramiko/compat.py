import six

if six.PY3:
    long = int
else:
    long = long


class PERM:
    o600 = 384
    o700 = 448
    o777 = 511
    o70 = 56
