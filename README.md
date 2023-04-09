# Python CCF Code
## Source - [PyCCF](https://bitbucket.org/cgrier/python_ccf_code)

There are two folders here -

* PurePython:
`PYCCF.py` is the actual software. `sample_runcode.py` is a script that contains a demonstration of how to use `PYCCF.py`. It will output three data files and one plot to the current directory. `sample_lc1.dat` and `sample_lc2.dat` are required to run the `sample_runcode.py` script. To compile the `Cython` code, please follow the following steps:

```
python sample_runcode.py
```

* CPython:
This version is 5~10 times faster than the PurePython version. `PYCCF.py` is the actual python CCF software; `xcorspc.pyx` is a `Cython` `XCOR` function; you have to install `Cython` and a `C` compiler (e.g., `GCC`). `setup.py` is a configuration file; use this file to compile the Cython `XCOR` function.  `sample_runcode.py` is a script that contains a demonstration. It will output three data files and one plot to the current directory. `sample_lc1.dat` and `sample_lc2.dat` are required to run the `sample_runcode.py` script. To compile the `Cython` code, please follow the following steps:

1.
```
python setup.py build_ext --inplace
```
and check if the compiling is finished without errors.

2.
```
python sample_runcode.py
```
