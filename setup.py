from setuptools import find_packages,setup
from typing import List


HAPEN_E_DOT='-e .'

def get_requirements(filepath:str)->[str]:
    '''
    this function will return the list of the requirements
    '''
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HAPEN_E_DOT in requirements:
            requirements.remove(HAPEN_E_DOT)

    return requirements        

setup(
    name='mlproject',
    version='0.0.1',
    author='Junaid',
    author_email='junaidchandio2k17@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)