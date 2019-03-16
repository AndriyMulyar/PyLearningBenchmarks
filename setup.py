from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
__version__ = "0.0.1"
__authors__ = "Andriy Mulyar"

packages = find_packages()

def readme():
    with open('README.md') as f:
        return f.read()

class PyTest(TestCommand):
    """
    Custom Test Configuration Class
    Read here for details: https://docs.pytest.org/en/latest/goodpractices.html
    """
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = "-s"

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)

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
        'numpy',
	'pandas'
    ],
    tests_require=['pytest'],
    cmdclass={"pytest": PyTest},
    include_package_data=True,
    zip_safe=False

)
