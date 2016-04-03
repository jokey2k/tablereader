from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="tablereader",
    packages=["tablereader"],
    version="1.0.3",
    description="Unified abstraction for handling xls, xlsx and CSV files in Python",
    author="Markus Ullmann",
    author_email="mail@markus-ullmann.de",
    url="http://github.com/jokey2k/tablereader",
    keywords=["encoding", "csv", "xlsx", "xls", "unicode"],
    license='BSD-3',
    install_requires=[
        'openpyxl>=2.3.4',
        'six',
        'xlrd'
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
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
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
