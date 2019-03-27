from setuptools import setup, find_packages
from setuptools.command.install import install


setup(name='mtinkerer',
      version='0.1.0',
      description='modernized GUI lib for tkinter',
      author='Lukas Gutiérrez',
      classifiers = [
            'Develope Status :: 1 - Planning',
            'Topic :: Software Development :: User Interfaces',
            'Topic :: Scientific/Engineering :: Astronomy',
            'Programming Language :: Python :: 3.7'
            ],
      author_email='lukasgutierrezlisboa@gmail.com',
      packages = find_packages())
