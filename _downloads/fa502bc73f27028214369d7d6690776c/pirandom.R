# estimate PI by using random numbers
#    A_squ = n = (2*r)²
#    A_cir = n_inside = pi * r²
#  
#    pi = n_inside/ r² = 4*n_inside/n
#
pirandom <- function(n) 		# define function
  {
      x <- runif(n,-1,1) 		# random numbers in [-1,1]
      y <- runif(n,-1,1) 		# random numbers in [-1,1]
      plot(x,y) # plot
      r <- sqrt(x*x+y*y) 		# distance to center
      rinside <- r[r<1] 		# inside circle with r=1?
      n_inside <- length(rinside)
      print(4*n_inside/n) 		# print pi estimation
 }
