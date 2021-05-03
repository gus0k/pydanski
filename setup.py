from setuptools import find_packages, setup

install_packages = [
        "numpy == 1.20.0",
        "matplotlib == 3.4.1",
        "scikit-learn == 0.24.1",
        "pandas == 1.2.3",
        "category-encoders == 2.2.2",
        "coolname == 1.1.0",
    ]

dev_packages = [
        "black == 21.4b2",
        "isort == 5.8.0",
        "ipython == 7.23.0",
        ]

setup(
    name="pydanski",
    version="0.0.1",
    url="https://github.com/tryolabs/pydanski",
    author="Diego Kiedanski",
    author_email="dkiedanski@tryolabs.com",
    description="Simple library with random python utils",
    packages=find_packages(),
    install_requires=install_packages,
    extras_require={
        "dev": dev_packages,
        }
)
