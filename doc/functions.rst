*********
Functions
*********

.. highlight:: r

Functions are fundamental building blocks in R programming that allow you to
encapsulate reusable code, making your programs more organized, maintainable,
and efficient. Rather than writing the same code repeatedly, you can define a
function once and call it whenever needed. This promotes the DRY principle
(Don't Repeat Yourself) and makes it easier to update logic in one place rather
than searching through your entire codebase. Functions also improve code
readability by giving meaningful names to operations and help break down
complex problems into smaller, manageable pieces.

When defining a function in R, you specify formal parameters (also called
formal arguments) in the function signature. These are placeholders that define
what inputs the function expects to receive. For example, in the function
definition

::

  > calculate_bmi <- function(weight, height) {
  +   weight / (height^2)
  + }

the formal parameters are ``weight`` and ``height``. These are essentially
variable names that will be used within the function body, but they don't have
actual values until the function is called.

.. note::

   The ``+`` symbol appears in continuation lines when defining multiline
   functions in the R console to indicate that R is waiting for additional
   input to complete an incomplete expression, signaling that the command is
   not yet finished and more code is expected before execution.

.. warning::

   Unlike Python, where indentation is syntactically significant and defines
   code blocks, R does not use indentation to determine program structure. In
   R, code blocks are delimited by curly braces ``{}``, and the interpreter
   completely ignores whitespace and indentation when parsing your code. This
   means you could write an entire function on a single line or use
   inconsistent indentation without causing syntax errors. However, while R
   doesn't enforce indentation, following consistent indentation conventions is
   still considered essential for code readability and maintainability. Proper
   indentation helps you and other programmers quickly understand the logical
   structure of your code, identify nested blocks, and spot errors more easily,
   even though the R interpreter itself pays no attention to it.


When you call a function, you provide actual arguments (or actual parameters)
that correspond to the formal parameters. These are the concrete values that
get passed into the function. For instance, when you call

::

  > calculate_bmi(70, 1.75)
  [1] 22.85714

the actual arguments are 70 and 1.75. At runtime, R binds these actual values
to the formal parameters: ``weight`` becomes 70 and ``height`` becomes 1.75
within that specific function execution. This distinction between formal and
actual parameters is important because the formal parameters exist only as a
template in the function definition, while actual arguments are the real data
being processed.

Default arguments provide a powerful way to make functions more flexible and
user-friendly. When you assign a default value to a formal parameter in the
function definition, that parameter becomes optional when calling the function.
For example, ``greet <- function(name, greeting = "Hello")`` defines a function
where ``greeting`` has a default value of "Hello". You can call this function
as ``greet("Alice")``, and it will use the default greeting, or you can
override it with ``greet("Alice", "Good morning")``. Default arguments are
particularly useful for parameters that typically have a standard value but
occasionally need to be changed, reducing the verbosity of function calls while
maintaining flexibility. They also make functions backward-compatible when
adding new parameters, since existing code that calls the function without the
new parameter will continue to work using the defaults.

Variable scope
==============

Variable scope in R determines where a variable can be accessed and modified
within your code. R uses lexical scoping, which means that the availability of
a variable depends on where it was defined in the structure of your code.

When you create a variable inside a function, it exists only within that
function's local environment and cannot be accessed from outside. This is
called a local variable. For example, if you define ``x <- 10`` inside a
function, that ``x`` is separate from any ``x`` that might exist in your global
environment. When the function finishes executing, local variables are
discarded.

Variables defined outside of any function, in your main R session, are global
variables. Functions can read global variables if no local variable with the
same name exists. However, if you assign a value to a variable inside a
function, R creates a new local variable rather than modifying the global one,
unless you explicitly use the superassignment operator ``<<-`` or the
``assign()`` function with specific parameters.

R searches for variables following a hierarchical path: it first looks in the
current local environment, then in the parent environment where the function
was defined, continuing upward through enclosing environments until it reaches
the global environment, and finally searches loaded packages. This nested
environment structure means that inner functions can access variables from
outer functions that enclose them.

Understanding scope is crucial for avoiding bugs, particularly when variable
names clash between different environments, and for writing functions that
behave predictably without unintended side effects on global variables.
