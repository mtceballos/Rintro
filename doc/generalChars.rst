*******************************
Main features of R
*******************************

.. highlight:: r

.. _chars:


.. note::
  Before starting to work with R, it is advised to create a new dedicated directory where all the work should be included. In fact, if several projects are to be developed at the same time, every project should have its own directory.

For Linux, MacOS:

.. code-block:: console
   :class: no-copybutton

   [user@pc]$ mkdir work
   [user@pc]$ cd work
   [user@pc work]$ R

.. warning::

 R is case-sensitive, thus in this example:


.. code-block:: r  

   > a = 1
   > A = 2

variables :makevar:`a` and :makevar:`A` are different variables:

.. code-block:: r  
   :class: no-copybutton

   > a == A					# is variable 'A' equal to variable 'a' ?
   [1] FALSE

.. _startR:

Starting R 
==========

For linux:

.. code-block:: r
   :class: no-copybutton

   [user@pc]$ R				# invoke R
    
   R version 4.5.1 (2025-06-13) -- "Great Square Root"
   Copyright (C) 2025 The R Foundation for Statistical Computing
   Platform: aarch64-apple-darwin20
   
   R is free software and comes with ABSOLUTELY NO WARRANTY.
   You are welcome to redistribute it under certain conditions.
   Type 'license()' or 'licence()' for distribution details.

     Natural language support but running in an English locale

   R is a collaborative project with many contributors.
   Type 'contributors()' for more information and
   'citation()' on how to cite R or R packages in publications.

   Type 'demo()' for some demos, 'help()' for on-line help, or
   'help.start()' for an HTML browser interface to help.
   Type 'q()' to quit R.

   >                               	#  R command line prompt 
  

.. code-block:: r
   :class: no-copybutton

   [user@pc]$ R --silent           	#  Suppress welcome message
   [user@pc]$ R --help             	#  Show R options
   
   Usage: R [options] [< infile] [> outfile]
     or: R CMD command [arguments]
    
   Start R, a system for statistical computation and graphics, with the
   specified options, or invoke an R tool via the 'R CMD' interface.
    
   Options:
     -h, --help            Print short help message and exit
     --version             Print version info and exit
     --encoding=ENC        Specify encoding to be used for stdin
   ...
   ...
   Please use 'R CMD command --help' to obtain further information about
   the usage of 'command'.
    
   Options --arch, --no-environ, --no-init-file, --no-site-file and --vanilla
   can be placed between R and CMD, to apply to R processes run by 'command'

Report bugs at <https://bugs.R-project.org>.
  
.. _exitR:

Quitting R
==========
   You can use ``quit()`` or ``q()``.

.. code-block:: r
   :class: no-copybutton
  
   > q()
   Save workspace image? [y/n/c]:   	# possibility of saving info for next session
   > q(save="no")                	# finish R without any question
   > Ctrl-D			    	# key combination equivalent to quit()

Using parenthesis in :command:`quit()` informs R that the command refers to a function and not to a variable.

.. _helpR:

Help in R
=========


.. code-block:: r  
   :class: no-copybutton

   > help.start()			# general help displayed in a web browser
   > help("pp") 			# help on function "pp"
   > ?pp                         	# help on function "pp" (you know the exact name)
   > help.search("pp")      		# search for instances of the string "pp"
   > ??pp 				# fuzzy search for instances of the string "pp"
   > apropos("pp", mode="function")  	# list available functions with "pp" in their names
   > example(topic)                     # run the R code from the *Examples* part of R's
                                        # online help on topic; try for example example(plot)
  
:kbd:`Tab` key can be used to complete the commands:

.. code-block:: r  
   :class: no-copybutton

   > Sys.<Tab><Tab>     # pressing <Tab> twice (after typing 'Sys.') to show 
                        # available Sys options
   Sys.chmod        Sys.glob         Sys.setFileTime  Sys.umask
   Sys.Date         Sys.info         Sys.setlocale    Sys.unsetenv
   Sys.getenv       Sys.localeconv   Sys.sleep        Sys.which
   Sys.getlocale    Sys.readlink     Sys.time         
   Sys.getpid       Sys.setenv       Sys.timezone     
  
   > Sys.Date()
   [1] "2030-01-01"

.. _usefulComms:

Other useful commands
=====================

.. code-block:: r  
   :class: no-copybutton

   > R.version.string
   [1] "R version 4.5.1 (2025-06-13)"

   > capabilities()
        jpeg         png        tiff       tcltk         X11        aqua 
        TRUE        TRUE        TRUE        TRUE        TRUE        TRUE 
    http/ftp     sockets      libxml        fifo      cledit       iconv 
        TRUE        TRUE       FALSE        TRUE        TRUE        TRUE 
         NLS       Rprof     profmem       cairo         ICU long.double 
        TRUE        TRUE        TRUE        TRUE        TRUE       FALSE 
     libcurl 
        TRUE

   > citation()
   To cite R in publications use:

     R Core Team (2025). _R: A Language and Environment for Statistical
     Computing_. R Foundation for Statistical Computing, Vienna, Austria.
     <https://www.R-project.org/>.
    
   A BibTeX entry for LaTeX users is
    
     @Manual{,
       title = {R: A Language and Environment for Statistical Computing},
       author = {{R Core Team}},
       organization = {R Foundation for Statistical Computing},
       address = {Vienna, Austria},
       year = {2025},
       url = {https://www.R-project.org/},
     }

   We have invested a lot of time and effort in creating R, please cite it
   when using it for data analysis. See also ‘citation("pkgname")’ for
   citing R packages.

   > R.home()				# return the R 'home' directory
   [1] "/usr/lib64/R"

   > getwd() 				# return the working directory
   [1] "/home/user/R"

   > setwd("/home/user/newRdir")       	# set new working directory

   > dir()				# show content of current directory
   ...					# (different from 'ls()' command
   ...					# which lists objects in current workspace)
    
   > history(n)				# display the last 'n' commands (default = 25)
   ...
   ...                                  # (press "q" to EXIT)
   
   > source("filename.R")		# execute commands in the filename.R script
   
   > sink("register.txt")               # divert R output to an external file 
    
   > sink()                             # stop sink-ing (results return to console)


.. admonition:: R for research in Astronomy
   :class: dropdown

   R is a powerful programming language and environment for statistical
   computing and data analysis that has become increasingly important in modern
   astrophysics. However, **when you first install R, you gain access to only
   its base functionality**, which includes fundamental statistical and
   graphical capabilities. The true strength of R lies in its extensive
   ecosystem of additional packages—specialized collections of functions, data,
   and documentation created by the R community. These packages extend R's
   capabilities far beyond its default installation, covering virtually every
   area of astronomical data analysis and computational astrophysics. From
   handling FITS files and astronomical catalogs with ``FITSio`` and
   ``astrodatR``, to performing sophisticated time series analysis of variable
   stars and exoplanet transits with ``astroTS``, to creating
   publication-quality plots and sky maps with ``ggplot2`` and ``mapproj``, the
   availability of thousands of well-documented packages on repositories like
   `CRAN (Comprehensive R Archive Network) <https://cran.r-project.org/>`_
   makes R an incredibly versatile tool for astrophysical research. Learning
   how to discover, install, and use these packages effectively is therefore a
   fundamental skill that will enable you to tackle everything from photometric
   data reduction and spectral analysis to cosmological simulations and survey
   data mining, transforming R from a basic statistical calculator into a
   comprehensive platform for astronomical research.
 
.. admonition:: A first glipmse of R in action
   :class: dropdown

   Try the following code:

   .. code-block:: r  

      # load a specific data set
      > data(cars)   

      # get info about the data set
      > ?cars

   .. code-block:: r  

      # show data
      > cars

   .. code-block:: r  

      # display the structure of the data object
      > str(cars)

   .. code-block:: r  

      # plot data
      > plot(cars)

   .. code-block:: r  

      # fit a linear model
      > linear_model <- lm( dist ~ speed , data=cars )

   .. code-block:: r  

      # display summary of the fitting result
      > summary(linear_model)

   .. code-block:: r  

      # display model coefficients
      > coef(linear_model)

   .. code-block:: r  

      # plot residuals against speed 
      > plot( resid(linear_model) ~ speed , data=cars )

      # Note: plot() is a generic function: it acts as a dispatcher that
      # examines the class of the object you pass to it. R looks for a
      # specific method plot.classname(). 
      # In this case: graphics:::plot.data.frame(cars)

