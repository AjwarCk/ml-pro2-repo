from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '.e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return list of requirements
    from requirments.txt file
    '''
    # Initilize  blank requirements list
    requirements=[]

    # Opening the file
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        # Remove hyphen_e_dot if present in requirements.
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements 

setup(
    name = 'ml-pro2',
    version = '0.0.1',
    author = 'Ajwar CK',
    author_email = 'ajwar.trn@outlook.com',
    packages = find_packages(),
    install_requires = get_requirements('requirments.txt') 
)