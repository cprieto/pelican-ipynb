from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name = 'pelican-ipynb',
    version = '1.0.0',
    description = 'Pelican plugin for Jupyter/IPython notebooks',
    url = 'https://github.com/danielfrg/pelican-ipynb',
    author = 'Daniel Rodriguez',
    author_email = 'df.rodriguez143@gmail.com',
    license = 'Apache License 2.0',
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Text Processing",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"],
    keywords = 'pelican markdown blog notebook ipython jupyter',
    packages = find_packages(exclude=['tests']),
    install_requires = [
        'pelican>=3.5',
        'jupyter', 'nbconvert>=4.0',
        'ipython>=4.0',
        'markdown>=2.6.1',
        'beautifulsoup4']
)
