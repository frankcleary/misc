require(parallel)
require(doParallel)
library(foreach)
library(iterators)

n <- 4000

parFun <- function(n) {
  X <- matrix(rnorm(n*n), ncol=n)
  Y <- X %*% X
}

serial_time <- system.time(
  for (i in 1:4) {
    parFun(n)
  }
)

nCores <- 4
registerDoParallel(nCores)
par_time <- system.time(
    result <- foreach(i = 1:nCores) %dopar% {
      parFun(n)
  }
)
print(serial_time)
print(par_time)
