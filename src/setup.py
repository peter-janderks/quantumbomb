from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='foqiproject',
      description='Package for simulation quantum bomb circuits',
      long_description=readme(),
      classifiers=[
        'Programming Language :: Python :: 3.5',
        'Topic :: Quantum Computing',
      ],
      url='https://github.com/peter-janderks/quantumbomb',
      author='Peter-Jan Derks and Thomas Oud',
      packages = find_packages(),
      include_package_data=True)
