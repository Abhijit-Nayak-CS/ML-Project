## In this command the automatically found all the packages in the intire ml applycation projects

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = [
            requirement.strip()
            for requirement in file_obj
            if requirement.strip()
            and not requirement.strip().startswith("#")
            and requirement.strip() != HYPEN_E_DOT
        ]

    return requirements



setup(
name='ML-Project',
version='0.0.1',
author='Abhijit-Nayak',
author_email='abhijitnayak104@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)







