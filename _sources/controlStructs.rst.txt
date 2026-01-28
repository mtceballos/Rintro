*******************
Control Structures
*******************

Types
=======

.. role:: bmagenta
.. role:: bblue
.. role:: green
.. role:: red

Böhm and Jacopini's work [#f1]_ in 1966, showed that the computer programs can be developed using only 
three *control structures*:

1. :bmagenta:`Sequence Structure`: the instructions are executed in the sequential order they have been written, 
unless the contrary is specified. In R, this behaviour is inherent to the interactive execution (through the 
R interpreter) and it is also the way in which instructions are executed in a script.

2. :bmagenta:`Selection Structure`: different instructions can be executed depending on a condition. In R this is implemented
through:

.. code-block:: r
   :class: no-copybutton

   > if(cond) expr
   > if(cond) cons.expr  else  alt.expr
  
3. :bmagenta:`Repetition Structure`: the execution of a group of instructions can be repeated inside a loop. This can be 
accomplished by:

.. code-block:: r
   :class: no-copybutton

   > for (name in expr_1) expr_2
   > while (condition) expr
   > repeat expr
  
Every algorithm can be resolved using the control structures described above.
These structures can be nested so the use of braces "{...}" and proper
indentation make the blocks of instructions clearer:

.. code-block:: r

   for (x in seq(-3,3)) {
     if (x < 0) {
       print("Caso A:")
       y <- sqrt(-x)
       cat("y=",y,"\n")
     } else {
       print("Caso B:")
       y <- sqrt(x)
       cat("y=",y,"\n")
     }
   }

Control Flow: break, next, return
=================================

These three commands are used to alter the normal execution of the control
structures. From R *help*:

**break**: breaks out of a ‘for’, ‘while’ or ‘repeat’ loop (applies only to the innermost loop).

**next**: halts the processing of the current iteration and advances the
looping index (applies only to the innermost loop.)

**return**: returns a value in a function and exits it.


.. rubric:: Footnotes

.. [#f1] Böhm C., and Jacopini G,. Flow Diagrams, Turing Machines, and Languages with Only Two Formation Rules, Communications of the ACM, Vol 9., No. 5, 1966, 336–371.


