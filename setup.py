PACKAGE = "easycrawler"
NAME = "easy_crawler"
DESCRIPTION = "very easy crawler in python"
AUTHOR = "mcpoet"
AUTHOR_EMAIL = "marrowsky@gmail.com"
URL = "http://www.baidu.com"
VERSION = 1.0

from setuptools import setup, find_packages
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    packages=find_packages(exclude=["tests.*", "tests"]),
    package_data=find_package_data(
			PACKAGE,
			only_in_packages=False),
    zip_safe=False,
)
