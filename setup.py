#coding=utf-8
from setuptools import find_packages, setup

#formwork setup
setup(
    name='project name',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_script',
        'pymysql',
    ],
)