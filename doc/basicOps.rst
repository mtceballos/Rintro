****************
Basic Operations
****************

.. _basicOps:

.. code-block:: r
  
   > a <- c(7+4,7-4,7*4,7/4) 	# elemental arithmetic operations
   > a
   [1] 11.00  3.00 28.00  1.75
 
   > length(a)			# return vector length
   [1] 4
   
   > c(min(a),max(a))		# calculate minimum and maximum value of the vector
   [1]  1.75 28.00
 
   > which.min(a)		# determine the location (index) of the minimum
   [1] 4
 
   > which.max(a)		# determine the location (index) of the maximum
   [1] 3
 
   > sort(a)			# sort vector values
   [1]  1.75  3.00 11.00 28.00
 
   > sum(a)			# calculate sum of all vector values
   [1] 43.75
 
   > cumsum(1:10)                # calculate cumulative sum
    [1]  1  3  6 10 15 21 28 36 45 55
 
   > cumprod(1:5)                # calculate cumulative product
   [1]     1     2     6    24   120   720  5040 40320
   
   > mean(a)			# calculate the mean value
   [1] 10.9375
 
   > median(a)			# calculate the median value
   [1] 7
 
   > var(a)			# calculate the variance
   [1] 146.1823
 
   > sd(a)			# calculate the standard deviation
   [1] 12.09059
 
   > quantile(a, 0.25)		# calculate first quantile (prob=25%)
      25% 
   2.6875 
 
There is a command to get basic statistical information in a simple way:

.. code-block:: r

   > summary(a)
       Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
     1.750   2.688   7.000  10.940  15.250  28.000 

Some important mathematical functions are ``exp()``, ``sin()``, ``cos()``,
``tan()``, ``log()``, ``log10()``,...

.. code-block:: r

   > ?Trig			# show information about trigonometric functions
   > ?exp			# help about 'exp()' function

R also includes Special functions of Mathematics: ``beta(a,b)``, 
``gamma(x)``,...

.. code-block:: r

   > ?Special			# help about Special mathematical functions
  
Operations in R can be *vectorized* helping to improve the code readability and
efficiency:

.. code-block:: r

   > a <- seq(10,30,10)
   > b <- seq(1:3)
   > a + b			# makes the sum of two vectors
   [1] 11 22 33
   
   > a * b			# vector product
   [1] 10 40 90
   > a / b                      # vector division
   [1] 10 10 10
   
   > a > 5			# logical operations
   [1] TRUE TRUE TRUE
   > b == 2
   [1] FALSE  TRUE FALSE

The vectorization can be also performed over matrices:

.. code-block:: r

   > m1 <- matrix(1:9, 3, 3)	# 3 x 3 matrix definition
   > m1
       [,1] [,2] [,3]
   [1,]    1    4    7
   [2,]    2    5    8
   [3,]    3    6    9
   
   > m2 <- matrix(11:19, 3, 3)	# 3 x 3 matrix definition
   > m2
       [,1] [,2] [,3]
   [1,]   11   14   17
   [2,]   12   15   18
   [3,]   13   16   19
   
   > m1 * m2 			# element-wise matrix multiplication
        [,1] [,2] [,3]
   [1,]   11   56  119
   [2,]   24   75  144
   [3,]   39   96  171
   
   > m1 %*% m2 			# true matrix multiplication
        [,1] [,2] [,3]
   [1,]  150  186  222
   [2,]  186  231  276
   [3,]  222  276  330
 
   
.. admonition:: Examples
   :class: dropdown

   .. code-block:: r

      # Some additional examples of matrix algebra:

      > v1 <- c(1,3,5)
      > v2 <- c(2,-1,3)

      > v1%*%v2                   # inner product
           [,1]
      [1,]   14

      > sqrt(v1%*%v1))            # vector modulus
         [,1]
     [1,] 5.91608

     > v1%o%v2                   # outer product
          [,1] [,2] [,3]
     [1,]    2   -1    3
     [2,]    6   -3    9
     [3,]   10   -5   15
     
     
     # Solving the system:
     #  4 x +   y  -2 z = 0
     #  2 x - 3 y + 3 z = 9
     # -6 x - 2 y +   z = 0
 
     > A <- matrix(c(4,2,-6,1,-3,-2,-2,3,1),nrow=3)  # system matrix
     > A
          [,1] [,2] [,3]
     [1,]    4    1   -2
     [2,]    2   -3    3
     [3,]   -6   -2    1
 
     > b <- c(0,9,0)
     > b
     [1] 0 9 0

     > x <- solve(A,b)           # computing vector x in A x = b
     > x
     [1]  0.75 -2.00  0.50
 
     > A%*%x                     # checking the solution
                   [,1]
     [1,]  1.110223e-16          # = 0 (within rounding error)
     [2,]  9.000000e+00          # = 9
     [3,] -5.551115e-17          # = 0 (within rounding error)
