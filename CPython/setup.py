from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension('xcorspc',
              ['xcorspc.pyx'])
]

for i in ext_modules:
    i.cython_directives = {'language_level': "3"}

setup(
  name = 'XCOR_C app',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
