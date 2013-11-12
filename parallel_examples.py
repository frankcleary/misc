# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:51:06 2013

@author: Frank
"""

import numpy
import pp
import time

def randprod(n):
    "Waste time by creating and multiplying a random n x n matrix"
    x = numpy.random.rand(n)
    return numpy.sum(x)

if __name__ == "__main__":
    test_n = [1e8]*4
    start_time = time.time()
    randlist = [randprod(n) for n in test_n]
    elapsed = (time.time() - start_time)
    print "Time for standard processing: %.1f" % elapsed + " s"

    time.sleep(1) # provide a break in windows CPU usage graph    
    
    par_start_time = time.time()
    ncpus = 4
    job_server = pp.Server(ncpus)
    jobs = [job_server.submit(randprod, (n,), (), ("numpy",)) for n in test_n]
    sums = [job() for job in jobs]
    par_elapsed = (time.time() - par_start_time)
    print "Time for parallel processing: %.1f" % par_elapsed + " s"
    