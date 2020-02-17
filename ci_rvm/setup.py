'''
Setup of the package ci_rvm
'''

from setuptools import setup


PATHADD = 'ci_rvm/'
PACKAGEADD = PATHADD.replace("/", ".")

setup(
    name="ci_rvm",
    version="0.9.0.dev1",
    #packages=find_packages(),
    install_requires=['numpy', 'scipy', 'matplotlib', 'vemomoto_core_tools'], 
    packages=[PACKAGEADD[:-1]],
    packages=[PACKAGEADD[:-1]],
    package_data={
        '': ['*LICENSE*'],
    },

    # metadata to display on PyPI
    author="Samuel M. Fischer",
    description="An algorithm to find profile likelihood confidence intervals", 
    keywords="confidence interval, likelihood, profile likelihood", 
    url="https://github.com/vemomoto/vemomoto",
    project_urls={
        "Bug Tracker": "https://github.com/vemomoto/vemomoto",
        "Documentation": "https://vemomoto.github.io/ci_rvm",
        "Source Code": "https://github.com/vemomoto/vemomoto/tree/master/ci_rvm",
    },
    classifiers=[
        'License :: OSI Approved :: LGPL-3.0'
    ],
)
