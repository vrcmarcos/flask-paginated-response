# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='Flask-Paginated-Response',
    version='1.0.0',
    url='https://github.com/vrcmarcos/flask-paginated-response',
    license='MIT',
    author='Marcos Cardoso',
    author_email='vrcmarcos@gmail.com',
    description='Response maker for Flask with RFC Standards such as Link Headers',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.11.1',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
