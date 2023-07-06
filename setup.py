from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:

    '''
        This Function will Return the List of Requiremnts
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


# Meta Data Information about the Project

setup(
name = 'mlproject',
version = '0.0.1',
author = "Sanjay",
author_email = "sanjaymanyam1112@gmail.com",
packages = find_packages(),
install_requires = ['pandas', 'numpy', 'seaborn']

)
