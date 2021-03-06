import codecs
import os

from setuptools import find_packages, setup


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    author="Eldarion, Inc.",
    author_email="development@eldarion.com",
    description="kelctl",
    name="kelctl",
    long_description=read("README.rst"),
    version="0.0.2",
    license="Apache 2.0",
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        kelctl=kelctl.__main__:cli
    """,
    install_requires=[
        "PyYAML==3.12",
        "requests==2.18.4",
        "Click==6.7",
        "kel-cluster",
    ],
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
    ],
)
