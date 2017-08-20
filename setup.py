from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='lebot-cerebro',
      version='0.1.0dev',
      description='Core engine for LeBot',
      long_description=readme(),
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
          'spacy',
          'scikit-learn',
          'scipy',
          'numpy',
          'pandas'
      ],
      include_package_data=True,
      zip_safe=False)
