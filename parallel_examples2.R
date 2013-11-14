require(parallel)
require(doParallel)
library(foreach)
library(iterators)

parFun <- function(A, B){
  A%*%B
}

nCores <- 2
n <- 4000 # for this toy code, make sure n is divisible by nCores
a <- rnorm(n*n)
A <- matrix(a, ncol=n)

registerDoParallel(nCores)
systime <- system.time(
  result <- foreach(i = 1:nCores, .combine = cbind) %dopar% {
    rows <-  ((i - 1)*n/nCores + 1):(i*n/nCores)
    out <- parFun(A, A[, rows])
  }
)

print(paste("Cores = ", nCores))
print(systime)
