from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads requirements.txt and returns a list of dependencies.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
       requirements = [req.replace("\n", "").strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name="customer-intelligence-ml",
    version="0.0.1",
    author="Deepak",
    author_email="your_email@example.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)