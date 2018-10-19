from setuptools import setup, find_packages

setup(
    # Application name:
    name="fast_tsne",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Damien Marlier",
    author_email="damienmarlier@tessatherapeutics.com",

    # Packages
    packages=find_packages(),

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/Tessa-Therapeutics/FIt-SNE/",

    # license="LICENSE.txt",
    description="FIt-SNE",

    zip_safe=False
)
