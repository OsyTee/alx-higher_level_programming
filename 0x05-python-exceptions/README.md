0x05-python-exceptions

Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.

Python lists:



Prototype: void print_python_list(PyObject *p);

Format: see example

If p is not a valid PyListObject, print an error message (see example)

Python bytes:



Prototype: void print_python_bytes(PyObject *p);

Format: see example

Line “first X bytes”: print a maximum of 10 bytes

If p is not a valid PyBytesObject, print an error message (see example)

Python float:



Prototype: void print_python_float(PyObject *p);

Format: see example

If p is not a valid PyFloatObject, print an error message (see example)

Read /usr/include/python3.4/floatobject.h

About:



Python version: 3.4

You are allowed to use the C standard library

Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c

You are not allowed to use the following macros/functions:

Py_SIZE

Py_TYPE

PyList_Size

PyList_GetItem

PyBytes_AS_STRING

PyBytes_GET_SIZE

PyBytes_AsString

PyBytes_AsStringAndSize

PyFloat_AS_DOUBLE

PySequence_GetItem

PySequence_Fast_GET_SIZE

PySequence_Fast_GET_ITEM

PySequence_ITEM

PySequence_Fast_ITEMS

NOTE:



The python script will be launched using the -u option (Force stdout to be unbuffered).

It is strongly advised to either use setbuf(stdout, NULL); or fflush(stdout) in your C functions IF you choose to use printf. The reason to that is that Pythonsprintand libCs printf don’t share the same buffer, and the output can appear disordered.
