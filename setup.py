
from distutils.core import setup
import sys


if sys.version_info <= (3,):
    raise Exception('Python 3 required')


setup(
    name = 'wddx',
    py_modules = ['wddx'],
    version = '0.2.0',
    author = 'Leon Matthews',
    author_email = 'python@lost.co.nz',
    url = 'http://lost.co.nz/',
    license='LICENSE.txt',

    requires=['Pylons>=0.97'],

    description='A Python decoder for the WDDX XML serialisation format.',
    long_description=open('README.txt').read(),

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: XML',
        ],
    )