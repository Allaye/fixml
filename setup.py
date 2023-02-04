

from setuptools import find_packages, setup

with open("requirements.txt", "r") as f:
    requirements = f.readlines()
    requirements = [i.strip() for i in requirements]

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="fixml",
    version="0.0.1",
    author="Kolade Gideon",
    author_email="Gideon.kolade@kolade.io",
    description="An all in one, one drop package to fix domain problems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/allaye/fixml",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Science/Research/Developers/Humans",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
)