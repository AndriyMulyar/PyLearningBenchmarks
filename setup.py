from setuptools import setup
from ml_datasets import __version__, __authors__

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='ml_datasets',
    version=__version__,
    license='GNU GENERAL PUBLIC LICENSE',
    description='A package allowing for the easy access and filterable retrieval of common machine learning benchmarks.',
    long_description=readme(),
    packages=['ml_datasets', 'datasets'],
    url='https://github.com/AndriyMulyar/ml_datasets',
    author=__authors__,
    author_email='contact@andriymulyar.com',
    keywords='machine-learning benchmark datasets',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.5',
        # 'Natural Language :: English'
        # 'Topic :: Text Processing :: Linguistic',
        'Intended Audience :: Science/Research'
    ],
    install_requires=[
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
    zip_safe=False

)
