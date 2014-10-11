import math


class PrimeChecker(object):

    def run(self, **kwargs):
        return self._is_prime(**kwargs)

    def _is_prime(self, value=0):
        if math.floor(value) != value:
            raise ValueError('%s should be an integer.' % value)
        if value < 2:
            return False
        for test in range(2, int(math.floor(math.sqrt(value)))+1):
            if value % test == 0:
                return False
        return True

if __name__ == '__main__':
    checker = PrimeChecker()
    for i in range(0, 10):
        print '%s : %s' % (i, checker.run(**{'value': i}))