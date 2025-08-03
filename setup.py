from setuptools import setup, find_packages

setup(
    name="vulnscan",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "vulnscan = vulnscan.cli:main"
        ]
    },
    author="Gjvon Graves",
    description="Lightweight CLI tool for detecting basic web vulnerabilities (XSS, SQLi)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.6",
)
