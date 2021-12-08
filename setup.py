from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()


VERSION = "0.1.0"
PACKAGE_NAME = "arubabankapi"
AUTHOR = "Orson Oehlers"
AUTHOR_EMAIL = "orson@oehlers.net"
URL = "https://github.com/orson1282/arubabank-api"
LICENSE = "OSI Approved :: GNU General Public License v3 (GPLv3)"
DESCRIPTION = "Python wrapper for Aruba Bank Online API"
LONG_DESC_TYPE = "text/markdown"
PACKAGES = find_packages()

REQUIREMENTS = [
      "requests",
      "bs4",
      "lxml"
]

CLASSIFIERS=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers"
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=PACKAGES,
    install_requires=REQUIREMENTS,
    license=LICENSE,
    classifiers=CLASSIFIERS,
)
