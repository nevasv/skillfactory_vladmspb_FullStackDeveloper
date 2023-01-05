from setuptools import find_packages, setup

# pip install -e .
setup(
    name='modules',
    packages=find_packages(include='modules'),
    version='0.0.1',
    description='My first module',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    test_requires=['pytest = 4.4.2'],
    test_suite='tests',
)
##
'''
import modules
from modules.my_module import sumAendB
sumAebdB(3,8)
sumAendB(3, 8)
Out[5]: 11
'''
# # pip uninstall modules
