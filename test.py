import gevent
from urllib.request import urlopen
from decimal import Decimal, getcontext
from collections import Counter
from time import time
# If we were to speed up the download as much as possible I will probably not
# delay the requests - that would be the best optimization :)


# assuming we want the size of the response and not the size of
# the output saved on disk which might be different
class Exercise(object):

    calls = []

    def download_from_url(self):
        gevent.sleep(0)
        from hashlib import sha256
        url = "http://slowwly.robertomurray.co.uk/delay/3000/url/https://www.python.org/"
        response = urlopen(url)
        return (sha256(response.read()).hexdigest(),
                response.info()['Content-Length'])

    def call_download(self):
        beg = time()
        self.calls = [self.download_from_url() for i in range(0, 10)]
        gevent.sleep(0)
        ms = time() - beg
        assert len(self.calls) == 10
        count = Counter([hash for (hash,y) in self.calls])

        if list(count.values())[0] is not 10:
            print("Something is wrong, all data should be the same")
        else:
            print("All data downloaded is the same and the lenght is: {}.\
        It took {}ms to complete".format(self.calls[0][1], ms))

    def pi(self):
        # code taken from https://docs.python.org/3/library/decimal.html#recipes
        """Compute Pi to the current precision.

        >>> print(pi())
        3.141592653589793238462643383

        """
        getcontext().prec += 1000000  # extra digits for intermediate steps
        three = Decimal(3)      # substitute "three=3.0" for regular floats
        lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
        while s != lasts:
            lasts = s
            n, na = n+na, na+8
            d, da = d+da, da+32
            t = (t * n) / d
            s += t
            if len(self.calls) is 10:
                break
            gevent.sleep(0)
        getcontext().prec -= 2

        # since it will be difficult to view I also added it on a text file
        with open('result_of_pi.txt', 'w') as f:
            f.write('{}'.format(+s))
        f.close()
        print('Calculated pi with {}'.format(round(+s, 20)))


if __name__ == '__main__':
    ex = Exercise()

    first = gevent.spawn(ex.pi)
    second = gevent.spawn(ex.call_download)
    gevent.joinall([
        second,
        first,
    ])
