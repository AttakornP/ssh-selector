from setuptools import setup

setup(
    name = 'ssh-server',
    version = '0.0.1',
    author = 'CartoonMed',
    author_email = 'attakornpks@gmail.com',
    scripts = ['bin/ssh-server'
    ],

    packages =[
      'src'
    , '.'
    ],
    
    install_requires = [
        'pyyaml'
    ],
)
