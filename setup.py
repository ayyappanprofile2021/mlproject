#find_packages is a utility function that automatically discovers 
#all python packages in your project, so you don't have to list them
#manually in setup.py

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ req.replace("\n", " ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Ayyappan',
    author_email='ayyappanprofile@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)