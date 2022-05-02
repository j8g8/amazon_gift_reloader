#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['selenium']

test_requirements = ['pytest>=3', ]

setup(
    author="justin gilbert",
    author_email='234jmg@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="reloads amazon giftcard balance",
    entry_points={
        'console_scripts': [
            'amazon-gift-reload=amazon_gift_reload.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='amazon_gift_reload',
    name='amazon_gift_reload',
    packages=find_packages(
        include=['amazon_gift_reload', 'amazon_gift_reload.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/gilbertoid/amazon_gift_reload',
    version='0.1.0',
    zip_safe=False,
)
