# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:51:06 2013

Compare serial vs. parallel processing for matrix multiplication

@author: Frank Cleary (frank@frankcleary.com)
"""

import pp
import time
import random

def randprod(n):
    "Waste time by creating and inefficiently multiplying an n x n matrix"
    random.seed(0)
    n = int(n)
    # Generate an n x n matrix of random numbers
    X = [[random.random() for _ in range(n)] for _ in range(n)]
    Y = [[None]*n]*n
    for i in range(n):
        for j in range(n):
            Y[i][j] = sum([X[i][k]*X[k][j] for k in range(n)])
    return Y

if __name__ == "__main__":
    test_n = [400]*4
    # Do 4 serial calculations:
    start_time = time.time()
    series_sums = [randprod(n) for n in test_n]
    elapsed = (time.time() - start_time)
    print "Time for standard processing: %.1f" % elapsed + " s"

    time.sleep(10) # provide a break in windows CPU usage graph    
    
    # Do the same 4 calculations in parallel
    par_start_time = time.time()
    n_cpus = 4
    job_server = pp.Server(n_cpus)
    jobs = [job_server.submit(randprod, (n,), (), ("random",)) for n in test_n]
    par_sums = [job() for job in jobs]
    par_elapsed = (time.time() - par_start_time)
    print "Time for parallel processing: %.1f" % par_elapsed + " s"
    
    print par_sums == series_sums