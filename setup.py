#!/usr/bin/env python

"""
Automatic Summarizer project
"""

from setuptools import find_packages, setup


setup(
    name='automatic_summarizer',
    version='1.0.0',
    license='No license',
    author='Leandro Rezende Rodrigues <leandro2r>',
    author_email='leandro.l2r@gmail.com',
    description='Automatic Summarizer project from UnB',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django<1.12',
        'django-cleanup<2.2',
        'mysql-python<1.3',
        'pdfminer==20140328',
        'gensim<2.4',
        'textblob<0.14.0',
        'PyYaml',
    ],
    extras_require={
        'dev': [
            'flake8',
            'django-nose',
        ]
    },
    entry_points={
        'console_scripts': [
            'automatic_summarizer=manage:main',
        ],
    },
    platforms='any',
    classifiers=[
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    keywords=[]
)
