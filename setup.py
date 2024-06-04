from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of reqirements 
    '''

    requirements=[]

    with open(file_path) as file_obj:
        reqirements= file_obj.readlines()
        requirements =[req.replace('\n',"")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requiremenets.remove(HYPEN_E_DOT)
    return requirements    





setup(
name ='MLProject',
version = '0.0.1',
author = 'Prashant',
authoe_email = 'prashant.singh081997@gmail.com',
packages = find_packages(),
install_requries =get_requirements('requirements.txt')

)