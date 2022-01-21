#!/usr/bin/env python3
from setuptools import find_packages, setup

NAME = "msvc"
DESCRIPTION = "multilingual speech valence classifier."
URL = "https://github.com/michen00/MSVC"
EMAIL = "michael.chen.0@gmail.com"
AUTHOR = "Michael I Chen"
VERSION = "0.1.0"
REQUIRED = [
    "daal",
    "daal4py",
    "ffmpeg",
    "joblib",
    "matplotlib",
    "numpy",
    "pandas",
    "pydub",
    "pysoundfile",
    "scikit-learn-intelex",
    "scikit-learn",
    "seaborn",
    "streamlit-webrtc",
    "streamlit",
    "swifter",
    "tensorflow-hub",
    "tensorflow",
    "torchaudio",
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    include_package_data=True,
)

# adapted from https://github.com/navdeep-G/setup.py/blob/master/setup.py
