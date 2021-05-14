from setuptools import setup, find_packages
import foo


setup(
    name='foo',
    version=foo.__version__,
    entry_points={
        'console_scripts': [
            'foo-bar = foo.cli:bar',
            'foo-xpto = foo.cli:xpto'
        ]
    },
    author='André Freitas',
    author_email='p.andrefreitas@gmail.com',
    packages=find_packages('.'),
    install_requires=['requests==2.25.1']
)
