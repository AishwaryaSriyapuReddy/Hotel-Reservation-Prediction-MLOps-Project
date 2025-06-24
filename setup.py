from setuptools import setup,find_packages

with open('requirements.txt') as f:
    requirements=f.read().splitlines()
    
setup(
    name="MLOPS PROJECT 1",
    version="0.1",
    author="Aishwarya",
    packages=find_packages(), # automatically detects src, utils and config and make them as packages
    install_requires=requirements, #Install all requirements
)