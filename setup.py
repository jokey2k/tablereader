from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name="tablereader",
    packages=find_packages(".", exclude=["tablereader.tests"]),
    version="1.1.1",
    description="Unified abstraction for handling xls, xlsx and CSV files in Python",
    author="Markus Ullmann",
    author_email="mail@markus-ullmann.de",
    url="https://github.com/jokey2k/tablereader",
    keywords=["encoding", "csv", "xlsx", "xls", "xlsm", "unicode"],
    license='BSD-3',
    install_requires=[
        'openpyxl>3.0.2',
        'six==1.11.0',
        'xlrd2==1.3.4'
    ],
    platform="any",
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Text Editors :: Text Processing",
        "Topic :: Text Processing :: Filters",
        "Topic :: Utilities",
    ],
    long_description=readme(),
)
