from setuptools import setup


try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()


setup(name='lebot-cerebro',
      version='0.1.0dev3',
      description='Core engine for LeBot',
      long_description=read_md('README.md'),
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
      packages=['cerebro'],
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
