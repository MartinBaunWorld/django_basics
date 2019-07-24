from setuptools import setup

setup(
    name='django_basics',
    version='0.1.0',
    description=(
        'Django functionality that I always end up needing',
    ),
    long_description='',
    author='Martin',
    author_email='m@pinehq.com',
    packages=[
        'django_basics',
    ],
    install_requires=[
        'django=<2.2',
        'django-ipware==2.1.0',
    ],
    scripts=[]
)
