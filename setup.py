from setuptools import setup, find_packages

setup(
    author='Ethan Frana',
    author_email='efrn11@gmail.com',
    maintainer='Ethan Frana',
    name='fancyBanner',
    version='0.9.9',
    packages=find_packages(exclude='tests, fb_old, fb_wrap'),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)

