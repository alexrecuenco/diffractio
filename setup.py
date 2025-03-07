#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst', encoding='utf8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', encoding='utf8') as history_file:
    history = history_file.read()

# requirements = [
#     'Click>=6.0', 'numpy', 'scipy', 'matplotlib','nbsphinx',
# ]

requirements = [
    'screeninfo', 'Pillow', 'numexpr', 'pandas', 'py_pol',
    'ipywidgets', 'ipympl', 'opencv-python', "psutil"
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
]

setup(
    author="Luis Miguel Sanchez Brea",
    author_email='optbrea@ucm.es',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="Optical Diffraction and Interference (scalar and vectorial)",
    entry_points={
        'console_scripts': [
            'diffractio=diffractio.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    # long_description=readme + '\n\n' + history,
    long_description=readme,
    include_package_data=True,
    keywords=[
        'diffractio', 'optics', 'diffraction', 'interference',
        'BPM', 'WPM', 'CZT', 'RS', 'VRS'
    ],
    name='diffractio',
    packages=find_packages(include=['diffractio']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://bitbucket.org/optbrea/diffractio/src/master/',
    version='0.3.1',
    zip_safe=False,
)
