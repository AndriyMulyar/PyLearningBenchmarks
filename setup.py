from setuptools import setup, find_packages
from py_learning_benchmarks import __version__, __authors__

packages = find_packages()

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='py_learning_benchmarks',
    version=__version__,
    license='GNU GENERAL PUBLIC LICENSE',
    description='A python package allowing for the easy access and filterable retrieval of common machine learning benchmarks.',
    long_description=readme(),
    packages=packages,
    url='https://github.com/AndriyMulyar/PyLearningBenchmarks',
    author=__authors__,
    author_email='contact@andriymulyar.com',
    keywords='machine-learning benchmark datasets',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Science/Research'
    ],
    install_requires=[
        'scipy'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
    zip_safe=False

)
