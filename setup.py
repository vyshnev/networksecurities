"""
The setup.py is a essesntial part of packageing and distributing python projects.
It is used by setuptools to define the configuration of your projects, such as metadata,
dependencies and more.
"""

from setuptools import find_packages,setup
from typing import List

def get_requirements()-> List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #read lines from file
            lines = file.readlines()
            #process each line
            for line in lines:
                requirement= line.strip()
                #ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

print(get_requirements())

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Vyshnev',
    author_email='vyshnevnandanam@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)