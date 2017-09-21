# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open as opn
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with opn(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='lebot-cerebro',
      version='0.1.0dev7',
      description='Core engine for LeBot',
      long_description=long_description,
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ],
      keywords=['Chat Bot, AI'],
      url='https://github.com/Le-Bot/cerebro',
      author='LeBot',
      author_email='sanket.upadhyay@infoud.co.in',
      license='MIT',
      packages=['cerebro']+find_packages(),
      package_data={'': ['*.csv'], 'cerebro.data': ['datasets/*.csv']},
      install_requires=[
          'scikit-learn',
          'scipy',
          'numpy',
          'pandas',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
