#!/usr/bin/env python3
from setuptools import find_packages, setup

NAME = "msvc"
DESCRIPTION = "multilingual speech valence classifier."
URL = "https://github.com/michen00/MSVC"
EMAIL = "michael.chen.0@gmail.com"
AUTHOR = "Michael I Chen"
VERSION = "0.1.0"
REQUIRED = [
    "daal==2021.4.0",
    "daal4py==2021.4.0",
    "ffmpeg>=1.4",
    "joblib==1.1.0",
    "matplotlib==3.5.1",
    "numpy==1.22.0",
    "pandas==1.3.5",
    "pydub==0.25.1",
    "pysoundfile>=0.9",
    "scikit-learn-intelex==2021.4.0",
    "scikit-learn==1.0.2",
    "seaborn==0.11.2",
    "streamlit-webrtc==0.34.2",
    "streamlit==1.4.0",
    "swifter==1.0.9",
    "tensorflow-hub==0.12.0",
    "tensorflow>=2.3.0",
    "torchaudio>=0.10",
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
