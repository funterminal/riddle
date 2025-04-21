from setuptools import setup, find_packages

setup(
    name="riddle",
    version="0.1",
    description="A minimalistic tool to run commands from a TOML file",
    author="Calestial Ashley",
    author_email="calestialashley@gmail.com",
    maintainer="Calestial Ashley",
    maintainer_email="calestialashley@gmail.com",
    url="https://github.com/funterminal/riddle.git",
    packages=find_packages(),
    install_requires=[
        'tomli',
    ],
    entry_points={
        'console_scripts': [
            'riddle=riddle:main',
        ],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    license="MIT",
)
