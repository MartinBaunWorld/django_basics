from setuptools import setup

setup(
    name='django_basics',
    version='0.1.4',
    description=(
        'Django functionality that I always end up needing'
    ),
    long_description=(
        'Django functionality that I always end up needing'
    ),
    author='Martin',
    author_email='m@pinehq.com',
    license='MIT',
    packages=[
        'django_basics',
        'django_basics.migrations',
    ],
    install_requires=[
        'django>=2',
        'django-ipware>=2',
    ],
    include_package_data=True,
    scripts=[]
)
