from setuptools import setup, find_packages
import setuptools
setup(
    name = "algokit",
    version = "0.0.3",
    keywords = ["pip", "algokit", "algorithm"],
    description = "common utilities and algorithm",
    long_description = "common utilities and algorithm",

    url = "https://github.com/wkgreat/algokit",
    author = "ke wang",
    author_email = "wkgreat@outlook.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)