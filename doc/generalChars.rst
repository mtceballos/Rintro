*******************************
Main features of R
*******************************

.. highlight:: r

.. _chars:


.. note::
  Before starting to work with R, it is advised to create a new dedicated directory where all the work should be included. In fact, if several projects are to be developed at the same time, every project should have its own directory.

For linux:

.. highlight:: console

::
  
  [user@pc]$ mkdir work
  [user@pc]$ cd work
  [user@pc work]$ R

.. warning::

 R is case-sensitive, thus in this example:

.. highlight:: r

::
  
  > a = 1
  > A = 2

variables :makevar:`a` and :makevar:`A` are different variables:

::

  > a == A					# is variable 'A' equal to variable 'a' ?
  [1] FALSE

.. _startR:

Starting R 
===========

For linux:

.. highlight:: console

::

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
  

.. highlight:: console

::

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
  
.. _exitR:

Quitting R
===========
.. highlight:: r

::
  
   > quit()
   Save workspace image? [y/n/c]:   	# possibility of saving info for next session
   > quit(save="no")                	# finish R without any question
   > Ctrl-D			    	# key combination equivalent to quit()

Using parenthesis in :command:`quit()` informs R that the command refers to a function and not to a variable.

.. _helpR:

Help in R
===========

::

  > help.start()			# general help displayed in a web browser
  > help("pp") 				# help on function "pp"
  > ?pp                         	# help on function "pp"
  > help.search("pp")      		# search for instances of the string "pp"
  > ??pp 				# search for instances of the string "pp"
  > apropos("pp", mode="function")  	# list available functions with "pp" in their names
  > example(topic)                      # run the R code from the *Examples* part of R's
                                        #   online help on topic; try for example example(plot)
  
:kbd:`Tab` key can be used to complete the commands:

::

  > Sys.<Tab><Tab>                     	# pressing <Tab> twice (after typing 'Sys.') to show 
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
::

  > R.version.string
  [1] "R version 3.0.1 (2013-05-16)"
  > capabilities()
      jpeg      png     tiff    tcltk      X11     aqua http/ftp  sockets 
      TRUE     TRUE     TRUE     TRUE     TRUE    FALSE     TRUE     TRUE 
    libxml     fifo   cledit    iconv      NLS  profmem    cairo 
      TRUE     TRUE     TRUE     TRUE     TRUE    FALSE     TRUE 
  > citation()
  
  To cite R in publications use:

    R Core Team (2013). R: A language and environment for statistical
    computing. R Foundation for Statistical Computing, Vienna, Austria.
    URL http://www.R-project.org/.
  ...
  ...

  > R.home()				# return the R 'home' directory
  [1] "/usr/lib64/R"
  > getwd() 				# return the working directory
  [1] "/home/user/R"
  > setwd("/home/user/newRdir")        	# set new working directory
  > dir()				# show content of current directory
  ...					# (different from 'ls()' command
  ...					# which lists objects in current workspace)
  
  > history(n)				# display the last 'n' commands (default = 25)
  ...
  ...                                   # (press "q" to EXIT)
  
  > source("filename.R")		# execute commands in the filename.R script
  
  > sink("register.txt")               	# divert R output to an external file 
  
  > sink()                             	# stop sink-ing (results return to console)
  
 
