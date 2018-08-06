# Usage of the gevent library to speed up multiple delayed requests while calculating pi as accurately as possible.

I've profiled the code with
`python -m cProfile test.py`

Results with the first implementation run just on the 33 - 34 seconds and because they are being delayed 30 seconds on purpose.

Reading the [latest changelogs of v. 1.3](http://www.gevent.org/whatsnew_1_3.html#performance) found out:

```
gevent 1.3 uses Cython on CPython to compile several performance critical modules. As a result, overall performance is improved. Specifically, queues are up to 5 times faster, pools are 10-20% faster, and the gevent.local.local is up to 40 times faster.
```

---> Which elicits the next question, faster than what? Is this 40 times faster than before or faster than let's say than queues?

In any case, this means using gevent 1.3 vs using gevent 1.2 will also yield increase in performance. UsinUsing     `monkey.patch_socket()` and then threads and p



### Note
If we were to speed up the download as much as possible I will (and  I  know it's very obvious) probably not delay the requests - that would be the best optimisation :)

Also, on my research I found [this](https://stackoverflow.com/questions/15461995/python-requests-vs-pycurl-performance):
```
if you're doing a lot of networking, use PyCurl, otherwise use requests. PyCurl finishes small requests 2x-3x as fast as requests until you hit the bandwidth limit with large requests (around 520 MBit or 65 MB/s here), and uses from 3x to 10x less CPU power
```

Where they benchmarked the requests library vs pycurl. Since I have never used it and wanted to complete the task with just under 2h I did not look into it. Probably there is a better way to speed things up (that would require read the whole documentation, code different ways of doing this and benchmark) - just I'm not fully aware of it and wanted to keep it short.
